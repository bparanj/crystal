## Purpose of Subnet

The purpose of a subnet is to partition a network into smaller, manageable segments, improving network performance and security by limiting broadcast traffic and providing a way to organize resources efficiently.

Organizing resources efficiently means arranging network resources in a way that optimizes their use, accessibility, and management, leading to improved performance and easier administration.

## Design Decisions

Deciding on the number of subnets in an AWS VPC involves considering several factors:

1. **Purpose of Subnets**: Subnets can be public or private. Public subnets are used for resources that must be accessible from the internet, like web servers. Private subnets are for resources that shouldn't be directly accessed from the internet, like databases.

2. **Availability Zones (AZs)**: Distributing subnets across multiple AZs provides high availability and fault tolerance. Each subnet resides entirely within one AZ.

3. **Size of the VPC**: The CIDR block assigned to your VPC will determine the maximum IP address space available and, by extension, how many subnets you can create and their sizes.

4. **Service Separation**: You might separate services into different subnets for security, performance, or organizational reasons. For example, web servers, application servers, and database servers might each reside in their own subnets.

5. **Growth and Scalability**: Anticipate future growth. Creating more subnets than currently needed can provide flexibility for scaling your architecture.

6. **Compliance and Security Requirements**: Certain regulations or security best practices may necessitate separating resources into different subnets.

7. **Network ACLs and Security Groups**: Different subnets can have different network access control lists (NACLs) and security groups for tailored access and security settings.

### Key Takeaways:
- Use public subnets for internet-facing resources and private subnets for internal resources.
- Distribute subnets across multiple AZs for higher availability.
- Plan for current and future needs, considering scalability and organizational requirements.
- Separate resources based on function, compliance, and security needs.

By evaluating these considerations, you can determine an appropriate number of subnets for your VPC that balances flexibility, scalability, and security.
