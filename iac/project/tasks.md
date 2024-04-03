## Custom Image

[ ] Install dependencies
[ ] Install Postgresql database
[ ] Start Postgresql service
[ ] Check AWS secrets - retain only one PEM file for one EC2 instance
[ ] Test base image created by Packer locally
[ ] How to automate testing of base images created by Packer
[ ] How to test image in isolation?
[ ] What is the image life cycle?
[ ] How to manage the image life cycle?
[ ] MOTD - Message of the day
[ ] Create inbound rule for SSH on port 2222
[ ] How to remove hard coded values of versions for Postgres, Redis etc from the playbook
[ ] What is -wizard* - How to cleanup EC2 instance (delete everything things in use will not be deleted)
[ ] Run Goss auto add for services on the server. Save tests in goss.yaml file.
[ ] Configure ufw firewall
[ ] Setup SSL
[ ] Firewall with IP tables setup
[ ] Disable root and SSH login
[ ] Passwordless login using pem file
[ ] Create an entry in ~/.ssh/config for host name
[ ] Default stack: Caddy, Puma, Redis, Postgresql, Rails 7.1, Ruby 3.3.0
[ ] Track all versions for a working image - document in release notes
[ ] Is the ansible.cfg inside ansible folder being used by Packer? If not, delete it.
[ ] How much memory will redis use by default?
[ ] Design experiments to find minimal packages (run on EC2 micro instances). Document in table on content site.
[ ] How to reduce the verbosity of Goss health check JSON response?
[ ] Manually add any missing Goss tests
[ ] Packages playbook must have minimal packages - needs review

## Application Deployment

[ ] Create Rails application database
[ ] Create Rails application database user
[ ] Install Rails framework dependencies
[ ] Upload application code
[ ] Run Rails web application
[ ] Setup log rotation
[ ] Production log file is not being created - needs a fix
[ ] Setup hourly database backups to S3

## Provisioning Server

[ ] Generate PEM file that is unique to every customer
[ ] PEF file downloader micro service using Go or Node
[ ] Create deploy user with sudo access
[ ] Implement JSON health check endpoint using ok*computer gem
[ ] Admin dashboard setup for Sidekiq (Does this require a playbook?)
[ ] ActiveAdmin dashboard setup
[ ] Add *.pem to gitignore
[ ] Instructions to install aws-sdk for JavaScript
[ ] Deploy blog and todo app before top 8 OS Rails apps
[ ] Health check for image processing, background job processor
[ ] When is EC2 snapshots useful?
[ ] Document aws-sdk version in VERSIONS.md
[ ] Optimize time to go live
[ ] Get static IP for EC2 instance when Terraform provisions an instance
[ ] Restrict IP address allowed to access port 3306 for database
[ ] Verify all versions are latest
[ ] Automate manual testing by creating EC2 image using Terraform from base image
[ ] JavaScript to download PEM file, chmod 400 and provide command to connect to EC2 instance from laptop
[ ] Setup background job processing with Redis
[ ] Retain only one AWS Secrets in AWS for one Rails app
[ ] Take todo, blog app used for teaching and provision it
[ ] Include simple app with ok*computer and health check to deploy Rails Docs app
[ ] Add virtual host
[ ] Restart Puma after code update
[ ] Bootstrap initial app - load initial data
[ ] How to setup a new Rails app with a new domain, SSL, a new EC2 instance, a new database and a new database user?
[ ] Upload code
[ ] Setup environment variables for database, Rails etc
[ ] Setup Rails master key to decrypt credentials
[ ] run bundle install, create database, migrate database
[ ] Rails credentials must be correct. Write a test to verify credentials.
[ ] Use Cloud Init for handling first and subsequent boots. Customer specific tasks and post deployment checks.

## Chore

[ ] Delete unused VPCs
[ ] Upgrade Ruby version to latest
[ ] Set billing cap to new AWS account ($100)
[ ] Programmatically download Vault secrets (AWS keys)
[ ] How to access log files?
[ ] Create a troubleshooting guide for customers. Troubleshooting should be one type of content.
[ ] Refer Capistrano and Kamal
[ ] Manage CRON jobs
[ ] Revise packages playbook - refer notes (terminal history)
[ ] Watch Hashicorp youtube videos for testing IaC
[ ] Virtual host - asset host ex: media.example.com
[ ] Find the old github repos with notes on IaC product - extract action items

[ ] Breakdown the tasks and write it down. Make the tasks actionable and concrete
[ ] Start checking off action items to build momentum
[ ] Extract action items from Moonshine github repo, ansible rails playbook github repot

[x] Learn about secrets management using Ansible vault

[ ] S3 policy is needed for database backups - Move to next folder (day 2 ops)

[ ] 
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
