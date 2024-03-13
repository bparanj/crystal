output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.rails_instance.public_ip
}

output "aws_account_id" {
  value = data.aws_caller_identity.current.account_id
}
