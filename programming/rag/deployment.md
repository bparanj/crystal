For a prototype with low traffic, a t2.small or even t2.micro could work fine. I suggested t2.medium initially thinking of the RAG application's memory requirements for:

1. Language Model API calls
2. Vector store operations
3. Both Streamlit and FastAPI running
4. Nginx

But if you're:
- Using API-based LLMs (like OpenAI) rather than running models locally
- Have a modest-sized vector store
- Expecting low concurrent traffic

You could start with:
```hcl
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.small"  # 2GB RAM, 1 vCPU
}
```

Or even:
```hcl
default     = "t2.micro"  # 1GB RAM, 1 vCPU
```

The t2.micro is free-tier eligible and costs significantly less. You can always:
1. Monitor the memory/CPU usage
2. Check for OOM (Out of Memory) errors in logs
3. Upgrade instance size if needed

## Packer Template

```hcl
packer {
  required_plugins {
    amazon = {
      version = ">= 1.2.1"
      source  = "github.com/hashicorp/amazon"
    }
    ansible = {
      version = ">= 1.1.0"
      source  = "github.com/hashicorp/ansible"
    }
  }
}

variable "region" {
  type    = string
  default = "us-west-2"
}

variable "instance_type" {
  type    = string
  default = "t2.medium"
}

source "amazon-ebs" "ubuntu" {
  ami_name      = "rag-application-{{timestamp}}"
  instance_type = var.instance_type
  region        = var.region

  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["099720109477"] # Canonical's AWS account ID
  }

  ssh_username = "ubuntu"

  tags = {
    Name        = "RAG Application"
    Environment = "Production"
    Builder     = "Packer"
  }
}

build {
  name = "rag-app"
  sources = [
    "source.amazon-ebs.ubuntu"
  ]

  # Install Python for Ansible
  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y python3"
    ]
  }

  # Use Ansible for configuration
  provisioner "ansible-local" {
    playbook_file = "./playbook.yml"
    role_paths = [
      "./roles/common",
      "./roles/rag_app"
    ]
    extra_arguments = ["--extra-vars", "ansible_python_interpreter=/usr/bin/python3"]
  }
}
```

## Ansible Provisioner

1. Uses Ansible for configuration management instead of shell scripts and file provisioners
2. Organizes configuration into roles and templates
3. Uses handlers for service management
4. Provides better error handling and idempotency

Directory structure should be:

```
.
├── packer.pkr.hcl
├── playbook.yml
└── roles/
    ├── common/
    │   └── tasks/
    │       └── main.yml
    └── rag_app/
        ├── handlers/
        │   └── main.yml
        ├── tasks/
        │   └── main.yml
        └── templates/
            ├── fastapi.service.j2
            ├── nginx.conf.j2
            └── streamlit.service.j2
```

To use:
1. Set up the directory structure as shown
2. Replace the repository URL in the Ansible tasks
3. Run:

```bash
packer init .
packer build .
```

## Playbook

```yml
# playbook.yml
---
- name: Configure RAG Application
  hosts: localhost
  become: yes
  roles:
    - common
    - rag_app

# roles/common/tasks/main.yml
---
- name: Install system dependencies
  apt:
    name: "{{ packages }}"
    state: present
    update_cache: yes
  vars:
    packages:
      - python3-pip
      - python3-venv
      - nginx
      - git

- name: Enable nginx service
  systemd:
    name: nginx
    enabled: yes
    state: started

# roles/rag_app/tasks/main.yml
---
- name: Clone RAG application repository
  git:
    repo: "https://github.com/your-username/your-rag-repo.git"
    dest: /home/ubuntu/rag-app
  become_user: ubuntu

- name: Create Python virtual environment
  command:
    cmd: python3 -m venv venv
    chdir: /home/ubuntu/rag-app
    creates: /home/ubuntu/rag-app/venv
  become_user: ubuntu

- name: Install Python requirements
  pip:
    requirements: "{{ item }}"
    virtualenv: /home/ubuntu/rag-app/venv
  loop:
    - /home/ubuntu/rag-app/backend/requirements.txt
    - /home/ubuntu/rag-app/frontend/requirements.txt
  become_user: ubuntu

- name: Create FastAPI service
  template:
    src: fastapi.service.j2
    dest: /etc/systemd/system/fastapi.service
  notify: reload systemd

- name: Create Streamlit service
  template:
    src: streamlit.service.j2
    dest: /etc/systemd/system/streamlit.service
  notify: reload systemd

- name: Configure Nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/sites-available/default
  notify: restart nginx

# roles/rag_app/templates/fastapi.service.j2
[Unit]
Description=FastAPI Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/rag-app/backend
Environment="PATH=/home/ubuntu/rag-app/venv/bin"
ExecStart=/home/ubuntu/rag-app/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target

# roles/rag_app/templates/streamlit.service.j2
[Unit]
Description=Streamlit Frontend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/rag-app/frontend
Environment="PATH=/home/ubuntu/rag-app/venv/bin"
ExecStart=/home/ubuntu/rag-app/venv/bin/streamlit run streamlit_app.py --server.port 8501
Restart=always

[Install]
WantedBy=multi-user.target

# roles/rag_app/templates/nginx.conf.j2
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}

# roles/rag_app/handlers/main.yml
---
- name: reload systemd
  systemd:
    daemon_reload: yes

- name: restart nginx
  systemd:
    name: nginx
    state: restarted

- name: enable and start services
  systemd:
    name: "{{ item }}"
    enabled: yes
    state: started
  loop:
    - fastapi
    - streamlit
```

## Terraform Provisioner

```hcl
# provider.tf
provider "aws" {
  region = var.region
}

# variables.tf
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.medium"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

variable "ami_id" {
  description = "AMI ID for the RAG application"
  type        = string
}

# vpc.tf
data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# security.tf
resource "aws_security_group" "rag_app" {
  name        = "rag-app-${var.environment}"
  description = "Security group for RAG application"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTP"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS"
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Consider restricting to your IP
    description = "SSH"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "rag-app-sg"
    Environment = var.environment
  }
}

# ec2.tf
resource "aws_key_pair" "rag_app" {
  key_name   = "rag-app-key"
  public_key = file("~/.ssh/id_rsa.pub")  # Make sure this exists
}

resource "aws_instance" "rag_app" {
  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id                   = data.aws_subnets.default.ids[0]
  vpc_security_group_ids      = [aws_security_group.rag_app.id]
  associate_public_ip_address = true
  key_name                   = aws_key_pair.rag_app.key_name

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
  }

  tags = {
    Name        = "rag-app-${var.environment}"
    Environment = var.environment
  }
}

# outputs.tf
output "public_ip" {
  description = "Public IP of the RAG application"
  value       = aws_instance.rag_app.public_ip
}

output "public_dns" {
  description = "Public DNS of the RAG application"
  value       = aws_instance.rag_app.public_dns
}
```