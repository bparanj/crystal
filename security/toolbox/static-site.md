Provide instructions to use Bleve for full text search in Hugo static site that uses md files.

Using Bleve for full-text search in a Hugo static site involves a few steps: indexing the Markdown files, integrating the search index into the Hugo site, and implementing the search functionality on the client side. Here’s a comprehensive guide to achieve this:

### Step 1: Install Bleve

First, you need to install Bleve. If you haven't installed it yet, you can do so by running:

```bash
go get github.com/blevesearch/bleve/v2
```

### Step 2: Create a Bleve Index

Next, create a script to index your Markdown files. Here's an example of a Go script that indexes the content of your Hugo site:

```go
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/blevesearch/bleve/v2"
	"github.com/russross/blackfriday/v2"
)

type Document struct {
	Title   string
	Content string
	Path    string
}

func main() {
	// Define the index path
	indexPath := "hugo_index.bleve"

	// Open or create the index
	index, err := bleve.Open(indexPath)
	if err == bleve.ErrorIndexPathDoesNotExist {
		mapping := bleve.NewIndexMapping()
		index, err = bleve.New(indexPath, mapping)
		if err != nil {
			log.Fatalf("Failed to create index: %v", err)
		}
	} else if err != nil {
		log.Fatalf("Failed to open index: %v", err)
	}

	// Walk through the content directory
	err = filepath.Walk("content", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && strings.HasSuffix(info.Name(), ".md") {
			fmt.Println("Indexing:", path)
			content, err := ioutil.ReadFile(path)
			if err != nil {
				return err
			}

			// Convert Markdown to plain text
			plainText := string(blackfriday.Run(content))

			// Create a document
			doc := Document{
				Title:   info.Name(),
				Content: plainText,
				Path:    path,
			}

			// Index the document
			err = index.Index(path, doc)
			if err != nil {
				return err
			}
		}
		return nil
	})

	if err != nil {
		log.Fatalf("Failed to walk content directory: %v", err)
	}

	fmt.Println("Indexing completed successfully.")
}
```

Save this script as `index.go`, and run it using:

```bash
go run index.go
```

This script will create a Bleve index named `hugo_index.bleve` that contains all your Markdown content converted to plain text.

### Step 3: Serve the Index

You need a way to serve the Bleve index to your Hugo site. This typically involves creating a small HTTP server. Here’s an example using Go:

```go
package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/blevesearch/bleve/v2"
)

var index bleve.Index

func searchHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query().Get("q")
	if query == "" {
		http.Error(w, "Query parameter 'q' is missing", http.StatusBadRequest)
		return
	}

	search := bleve.NewSearchRequest(bleve.NewQueryStringQuery(query))
	searchResults, err := index.Search(search)
	if err != nil {
		http.Error(w, "Failed to execute search", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(searchResults)
}

func main() {
	var err error
	index, err = bleve.Open("hugo_index.bleve")
	if err != nil {
		log.Fatalf("Failed to open index: %v", err)
	}

	http.HandleFunc("/search", searchHandler)
	log.Println("Starting server on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Save this script as `server.go`, and run it using:

```bash
go run server.go
```

### Step 4: Integrate Search into Hugo Site

You need to add a search interface to your Hugo site. Here’s an example of how to do it:

#### Add a Search Form

Add a search form to your Hugo site's HTML, for example in `layouts/partials/header.html`:

```html
<form id="search-form">
  <input type="text" id="search-input" placeholder="Search..." />
  <button type="submit">Search</button>
</form>
```

#### Add JavaScript to Perform the Search

Create a JavaScript file, for example `static/js/search.js`, to handle the search requests:

```javascript
document.getElementById('search-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var query = document.getElementById('search-input').value;
  fetch('/search?q=' + encodeURIComponent(query))
    .then(response => response.json())
    .then(data => {
      var results = document.getElementById('search-results');
      results.innerHTML = '';
      data.hits.hits.forEach(hit => {
        var item = document.createElement('div');
        item.innerHTML = '<a href="' + hit.id + '">' + hit.fields.Title + '</a>';
        results.appendChild(item);
      });
    });
});
```

#### Add a Search Results Container

Add a container for displaying search results, for example in `layouts/_default/baseof.html`:

```html
<div id="search-results"></div>
```

### Step 5: Build and Deploy Your Site

Build your Hugo site and ensure the search server is running. You can now perform searches on your site using the form you added.

By following these steps, you can integrate Bleve for full-text search in your Hugo static site, leveraging the power of a search engine while maintaining the simplicity and performance of a static site.


https://blevesearch.com/
https://github.com/blevesearch/bleve

To use Bleve for full-text search in a Hugo static site that uses Markdown (md) files, you can follow these instructions:

1. Install Bleve:
   - Make sure you have Go installed on your system.
   - Open a terminal and run the following command to install Bleve:
     ```
     go get -u github.com/blevesearch/bleve
     ```

2. Create a new Hugo site (if you haven't already):
   - Open a terminal and navigate to the directory where you want to create your Hugo site.
   - Run the following command to create a new Hugo site:
     ```
     hugo new site mysite
     ```
   - Replace "mysite" with your desired site name.

3. Configure Hugo to generate a JSON index:
   - Open the `config.toml` file in your Hugo site's root directory.
   - Add the following configuration to enable JSON output:
     ```toml
     [outputs]
       home = ["HTML", "RSS", "JSON"]
     ```

4. Create a new Hugo theme or modify an existing one:
   - If you're creating a new theme, run the following command in your site's root directory:
     ```
     hugo new theme mytheme
     ```
   - Replace "mytheme" with your desired theme name.
   - If you're modifying an existing theme, navigate to the theme's directory.

5. Create a template for the search index:
   - Inside your theme's `layouts/_default` directory, create a new file named `index.json.json`.
   - Add the following content to the file:
     ```html
     {{- $.Scratch.Add "index" slice -}}
     {{- range where .Site.Pages "Kind" "page" -}}
       {{- $.Scratch.Add "index" (dict "title" .Title "tags" .Params.tags "categories" .Params.categories "contents" .Plain "permalink" .Permalink) -}}
     {{- end -}}
     {{- $.Scratch.Get "index" | jsonify -}}
     ```

6. Generate the Hugo site:
   - Open a terminal and navigate to your Hugo site's root directory.
   - Run the following command to generate the static site:
     ```
     hugo
     ```
   - The generated site will be located in the `public` directory.

7. Implement search functionality using Bleve:
   - Create a new Go file, e.g., `search.go`, in your project directory.
   - Add the following code to the file:
     ```go
     package main

     import (
       "encoding/json"
       "fmt"
       "io/ioutil"
       "log"
       "os"

       "github.com/blevesearch/bleve"
     )

     func main() {
       // Load the JSON index file
       jsonFile, err := os.Open("public/index.json")
       if err != nil {
         log.Fatal(err)
       }
       defer jsonFile.Close()

       // Read the JSON data
       jsonData, err := ioutil.ReadAll(jsonFile)
       if err != nil {
         log.Fatal(err)
       }

       // Parse the JSON data
       var docs []map[string]interface{}
       err = json.Unmarshal(jsonData, &docs)
       if err != nil {
         log.Fatal(err)
       }

       // Create a new Bleve index
       mapping := bleve.NewIndexMapping()
       index, err := bleve.New("myindex.bleve", mapping)
       if err != nil {
         log.Fatal(err)
       }
       defer index.Close()

       // Index the documents
       for _, doc := range docs {
         err = index.Index(doc["permalink"].(string), doc)
         if err != nil {
           log.Fatal(err)
         }
       }

       // Perform a search
       query := "search query"
       searchRequest := bleve.NewSearchRequest(bleve.NewQueryStringQuery(query))
       searchResult, err := index.Search(searchRequest)
       if err != nil {
         log.Fatal(err)
       }

       // Print the search results
       fmt.Println("Search Results:")
       for _, hit := range searchResult.Hits {
         fmt.Printf("Title: %s\nPermalink: %s\nScore: %f\n\n", hit.Fields["title"], hit.ID, hit.Score)
       }
     }
     ```

8. Build and run the Go program:
   - Open a terminal and navigate to the directory containing the `search.go` file.
   - Run the following command to build the program:
     ```
     go build search.go
     ```
   - Run the generated executable:
     ```
     ./search
     ```

   The program will load the JSON index file, create a Bleve index, and perform a search based on the specified query. The search results will be printed in the terminal.

9. Integrate the search functionality into your Hugo site:
   - Modify your Hugo templates to include a search input field and a search results section.
   - Use JavaScript to make an HTTP request to the Go program's endpoint, passing the search query as a parameter.
   - Parse the JSON response and display the search results on your Hugo site.

You have now set up Bleve for full-text search in your Hugo static site. When you generate your site using Hugo, it will create a JSON index file containing the content of your Markdown files. The Go program will then use Bleve to create a search index and perform searches based on user queries.

Customize the search functionality according to your specific requirements, such as handling user input, displaying search results, and styling the search interface.

Here's an updated version of the Packer template using HCL (HashiCorp Configuration Language) instead of JSON:

```hcl
source "amazon-ebs" "hugo_search_index_server" {
  region        = "us-west-2"
  source_ami    = "ami-0d1c7c4de1f4a1e2c"
  instance_type = "t2.micro"
  ssh_username  = "ubuntu"
  ami_name      = "hugo-search-index-server-${formatdate("YYYYMMDD-hhmmss", timestamp())}"
}

build {
  sources = ["source.amazon-ebs.hugo_search_index_server"]

  provisioner "ansible" {
    playbook_file = "server-config.yml"
  }
}
```

Save this HCL configuration as `packer-template.pkr.hcl`.

Here's an explanation of the changes:

- The `builders` block is replaced with the `source` block, which defines the source configuration for the Amazon EBS builder.
- The `source_ami` should be set to the appropriate Ubuntu 22.04 AMI ID for your region.
- The `ami_name` now uses the `formatdate` function to generate a timestamp-based name for the AMI.
- The `provisioners` block is replaced with the `build` block, which specifies the build configuration.
- Inside the `build` block, the `sources` attribute specifies the source configuration to use, referencing the defined `source` block.
- The `provisioner` block remains the same, specifying the Ansible playbook to use for provisioning.

The rest of the setup remains the same as before. You'll still use the Ansible playbook (`server-config.yml`) to configure the server and deploy the Hugo static site with the search index server.

To build the server image using the HCL configuration, run the following command:

```bash
packer build packer-template.pkr.hcl
```

Packer will build an AMI based on Ubuntu 22.04, provision it using the Ansible playbook, and create a new AMI.

You can then use Terraform to deploy the server image to EC2 as described in the previous response.

Replace the `source_ami` with the appropriate Ubuntu 22.04 AMI ID for your region, and ensure that you have the necessary AWS credentials and permissions configured for Packer and Terraform to interact with your AWS account.

To use HashiCorp Configuration Language (HCL) instead of JSON for the Packer template, you need to create an HCL-based Packer template file. Here’s how you can create and use an HCL template to set up an Ubuntu 22.04 server for deploying a Hugo static site with a search index server.

### Step 1: Ansible Playbook
The Ansible playbook remains the same as provided earlier:

**ansible/playbook.yml**:
```yaml
---
- name: Setup Ubuntu server for Hugo static site with search index server
  hosts: all
  become: yes
  vars:
    hugo_version: "0.101.0"
    hugo_bin_path: "/usr/local/bin/hugo"
    hugo_site_path: "/var/www/hugo-site"
    bleve_index_path: "/var/www/hugo-site/search_index.bleve"
    go_version: "1.18.2"
    go_tarball: "go{{ go_version }}.linux-amd64.tar.gz"
    go_install_path: "/usr/local"
    go_bin_path: "{{ go_install_path }}/go/bin/go"

  tasks:
    - name: Update and upgrade apt packages
      apt:
        update_cache: yes
        upgrade: yes

    - name: Install required packages
      apt:
        name:
          - wget
          - unzip
          - git
          - gcc
          - make
        state: present

    - name: Install Hugo
      get_url:
        url: "https://github.com/gohugoio/hugo/releases/download/v{{ hugo_version }}/hugo_extended_{{ hugo_version }}_Linux-64bit.tar.gz"
        dest: "/tmp/hugo.tar.gz"
      notify:
        - extract_hugo

    - name: Extract and install Hugo binary
      unarchive:
        src: "/tmp/hugo.tar.gz"
        dest: "/usr/local/bin/"
        remote_src: yes
      notify:
        - cleanup_hugo_tar

    - name: Create Hugo site directory
      file:
        path: "{{ hugo_site_path }}"
        state: directory
        owner: www-data
        group: www-data
        mode: '0755'

    - name: Install Go
      get_url:
        url: "https://golang.org/dl/{{ go_tarball }}"
        dest: "/tmp/{{ go_tarball }}"
      notify:
        - extract_go

    - name: Set Go environment variables
      shell: |
        echo "export PATH=$PATH:{{ go_install_path }}/go/bin" >> /etc/profile
        echo "export GOROOT={{ go_install_path }}/go" >> /etc/profile
        echo "export GOPATH=/usr/local/go" >> /etc/profile

    - name: Clone Bleve server repository
      git:
        repo: "https://github.com/blevesearch/bleve"
        dest: "/tmp/bleve"

    - name: Build and install Bleve
      shell: |
        cd /tmp/bleve
        {{ go_bin_path }} build -o /usr/local/bin/bleve
      environment:
        GOPATH: "/usr/local/go"
        GOROOT: "{{ go_install_path }}/go"
      notify:
        - cleanup_bleve_repo

    - name: Configure Bleve index server
      copy:
        content: |
          #!/bin/bash
          bleve create -index {{ bleve_index_path }}
        dest: /usr/local/bin/initialize_bleve_index.sh
        mode: '0755'

    - name: Start and enable Bleve index server
      systemd:
        name: bleve
        enabled: yes
        state: started
        daemon_reload: yes
      notify:
        - setup_bleve_service

  handlers:
    - name: extract_hugo
      unarchive:
        src: "/tmp/hugo.tar.gz"
        dest: "/usr/local/bin"
        remote_src: yes

    - name: cleanup_hugo_tar
      file:
        path: "/tmp/hugo.tar.gz"
        state: absent

    - name: extract_go
      unarchive:
        src: "/tmp/{{ go_tarball }}"
        dest: "{{ go_install_path }}"
        remote_src: yes

    - name: cleanup_bleve_repo
      file:
        path: "/tmp/bleve"
        state: absent

    - name: setup_bleve_service
      copy:
        content: |
          [Unit]
          Description=Bleve Index Server
          After=network.target

          [Service]
          ExecStart=/usr/local/bin/bleve server -index {{ bleve_index_path }}
          Restart=always

          [Install]
          WantedBy=multi-user.target
        dest: /etc/systemd/system/bleve.service
```

### Step 2: Packer Template in HCL

Create a Packer template using HCL for building the server image.

**packer/template.pkr.hcl**:
```hcl
variable "aws_access_key" {
  type    = string
  default = ""
}

variable "aws_secret_key" {
  type    = string
  default = ""
}

variable "region" {
  type    = string
  default = "us-east-1"
}

source "amazon-ebs" "ubuntu" {
  access_key    = var.aws_access_key
  secret_key    = var.aws_secret_key
  region        = var.region
  source_ami_filter {
    filters = {
      "virtualization-type" = "hvm"
      "name"                = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"
      "root-device-type"    = "ebs"
    }
    owners      = ["099720109477"]
    most_recent = true
  }
  instance_type = "t2.micro"
  ssh_username  = "ubuntu"
  ami_name      = "hugo-bleve-{{timestamp}}"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "ansible" {
    playbook_file = "ansible/playbook.yml"
  }
}
```

### Step 3: Terraform Configuration

Use Terraform to deploy the Packer-built image to an EC2 instance.

**terraform/main.tf**:
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "hugo_bleve" {
  ami           = var.ami_id
  instance_type = "t2.micro"
  key_name      = var.key_name

  tags = {
    Name = "Hugo-Bleve-Server"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo systemctl enable bleve",
      "sudo systemctl start bleve"
    ]
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file(var.private_key_path)
    host        = self.public_ip
  }
}

variable "ami_id" {}
variable "key_name" {}
variable "private_key_path" {}
```

### Step 4: Putting It All Together

1. **Build the Image with Packer**:
   ```bash
   packer build packer/template.pkr.hcl
   ```

2. **Deploy the Image with Terraform**:
   - Initialize Terraform:
     ```bash
     terraform init
     ```
   - Apply the configuration:
     ```bash
     terraform apply -var "ami_id=ami-xxxxxxxx" -var "key_name=your-key-name" -var "private_key_path=/path/to/your/private/key"
     ```

By following these steps, you will set up an automated pipeline to create an Ubuntu 22.04 server image with Hugo and a Bleve search index server using Ansible, Packer, and Terraform. This setup helps maintain a consistent and reproducible environment for your Hugo static site.
