## IaC Terms

Infrastructure as Code (IaC) is a key practice in modern software development and operations, utilizing code to manage and provision infrastructure automatically. Here are some essential terms associated with IaC:

1. **Configuration Management**: Tools and practices for maintaining and managing the state of infrastructure in a desired, consistent configuration. Examples include Ansible, Chef, Puppet, and SaltStack.

2. **Provisioning**: The process of setting up and configuring the infrastructure resources (servers, networks, storage, etc.) required for applications to run. Tools like Terraform, CloudFormation (AWS), and ARM templates (Azure) are  used for provisioning.

3. **Declarative Configuration**: A method where the desired state of the infrastructure is specified, and the tooling automatically makes the necessary changes to achieve that state, without specifying how to do it.

4. **Imperative Configuration**: A method where specific commands are given to the system to change the infrastructure state, explicitly defining the steps to achieve the desired outcome.

5. **Idempotency**: The property ensuring that an operation can be applied multiple times without changing the result beyond the initial application, crucial for reliable automated provisioning and configuration management.

6. **Continuous Integration/Continuous Deployment (CI/CD)**: Practices and tools used to automate the integration of code changes and reliably deploy applications to production environments. While not exclusive to IaC, CI/CD pipelines often include infrastructure provisioning steps.

7. **Version Control**: The use of systems like Git to keep track of changes to the infrastructure code, allowing for collaboration, history tracking, and rollback capabilities.

8. **Orchestration**: The automated configuration, coordination, and management of computer systems, applications, and services. Orchestration tools help manage complex tasks and workflows in cloud environments.

9. **Terraform**: An open-source tool by HashiCorp used for building, changing, and versioning infrastructure safely and efficiently. Terraform uses a declarative configuration language to manage both cloud and on-premises resources.

10. **CloudFormation**: An AWS service that provides a common language for describing and provisioning all the infrastructure resources in the cloud environment.

11. **Immutable Infrastructure**: A model where infrastructure components are replaced rather than updated in place. Once a component is deployed, it is never modified; if changes are needed, a new component is provisioned and replaced.

12. **Infrastructure as Code (IaC) Tools**: Specific tools designed to facilitate IaC practices, such as Terraform, Ansible, Chef, Puppet, and SaltStack, each with its own syntax and capabilities.

13. **Containers and Container Orchestration**: Technologies like Docker allow applications to be packaged with their dependencies, and orchestration tools like Kubernetes manage these containers at scale, which is often managed through IaC.

14. **YAML and JSON**: Markup languages  used to write configuration files for IaC. They allow for the clear definition of infrastructure as code in a readable format.

These terms represent the foundational concepts and tools that underpin Infrastructure as Code, highlighting its role in automating and managing modern infrastructure efficiently and reliably.
