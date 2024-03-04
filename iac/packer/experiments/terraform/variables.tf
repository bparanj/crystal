variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.medium"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-03b2bc56d1503c131" # Consider using a data source to dynamically fetch AMI (refer: dynamically-fetch-ami-id.md)
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_cidr_block" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "availability_zone" {
  description = "Availability zone for the subnet"
  type        = string
  default     = "us-west-2a" # Consider fetching dynamically based on region if possible
}

variable "key_name" {
  description = "Name of the AWS key pair"
  type        = string
  default     = "deployer-key"
}

variable "security_group_name" {
  description = "The name of the security group"
  type        = string
  default     = "rails-sg"
}

variable "ssh_cidr_blocks" {
  description = "CIDR blocks for SSH access"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "http_cidr_blocks" {
  description = "CIDR blocks for HTTP access"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "https_cidr_blocks" {
  description = "CIDR blocks for HTTPS access"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "postgres_cidr_blocks" {
  description = "CIDR blocks for PostgreSQL access"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "redis_cidr_blocks" {
  description = "CIDR blocks for Redis access"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "route_table_name" {
  description = "The name tag for the route table"
  type        = string
  default     = "rails-public-route-table"
}

variable "route_table_cidr_block" {
  description = "The CIDR block for the default route in the route table"
  type        = string
  default     = "0.0.0.0/0"
}
