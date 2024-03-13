## Dynamically Allocate Static IP

Change the main.tf to allocate a new Elastic IP:

```hcl
resource "aws_eip" "static_ip" {
  tags = {
    Name = "RailsAppEIP"
  }
}

resource "aws_eip_association" "static_ip_association" {
  instance_id   = aws_instance.rails_instance.id
  allocation_id = aws_eip.static_ip.id
}
```

Terraform output:

```
aws_eip_association.static_ip_association: Creation complete after 1s [id=eipassoc-0d3b898a6e68257e2]

Apply complete! Resources: 14 added, 0 changed, 0 destroyed.

Outputs:

instance_public_ip = "54.212.10.8"
```

Verify the static IP:

```
$ aws ec2 describe-addresses --allocation-ids eipassoc-0d3b898a6e68257e2 --region us-west-2

An error occurred (InvalidAllocationID.NotFound) when calling the DescribeAddresses operation: The allocation ID 'eipassoc-0d3b898a6e68257e2' does not exist
```

Replace the eipassoc- part with eipalloc-<same-id-in-terraform-output>:

```
$ aws ec2 describe-addresses --allocation-ids eipalloc-0ccdc7299ad299954 --region us-west-2

{
    "Addresses": [
        {
            "InstanceId": "i-08541a065a7d7b6ff",
            "PublicIp": "18.236.28.57",
            "AllocationId": "eipalloc-0ccdc7299ad299954",
            "AssociationId": "eipassoc-0d3b898a6e68257e2",
            "Domain": "vpc",
            "NetworkInterfaceId": "eni-0b32cc25b563782fb",
            "NetworkInterfaceOwnerId": "875721448715",
            "PrivateIpAddress": "10.0.10.239",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "RailsAppEIP"
                }
            ],
            "PublicIpv4Pool": "amazon",
            "NetworkBorderGroup": "us-west-2"
        }
    ]
}
```
