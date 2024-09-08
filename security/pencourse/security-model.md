Security model is a theoretical framework. Sometimes, a set of rules that can be implemented in different contexts.

Bell-LaPadula Model

- Deals with confidentiality
- Enforce access controls in systems with multiple security levels
    - Unclassified
    - Confidential
    - Secret
    - Top secret
- Who can access what objects at various security levels
- Simple Security Property
    - Individuals cannot read data with a security level higher than their own
- Star Security Property
    - Individuals cannot write data with a security level lower than their own
- Discretionary Security Property
    - Not allowed to read or write at a level other than their own

Brewer and Nash Model

- Enforce access controls to maintain confidentiality (with aim of minimizing conflict of interest)

Biba Model

- Enforce access controls
- Designed to protect the integrity of information (individuals and information are assigned different integrity levels)
- Simple Integrity Property
- Star Integrity Property
- Invocation Property
    - Cannot request access to information with a higher integrity level than their own

Clark-Wilson Model

- Used to protect data integrity
- Implemented through access control triples
    - Subject, program and object
- Subjects don't have direct access to objects
- Access and modify through a series of programs
- Program operate on data objects and enforce integrity policies

Role-Based Access Control

- Used in Identity and Access Management (IAM)
- Grants permissions to roles
- Roles are applied to individual users

Attribute-Based Access Control (ABAC)

Series of attributes are applied to users and objects. Rules use the attributes to determine which users can perform which types of access on which objects.

- Provides more granular access control
- More dynamic

Shift-Left Security

Security is built into the service architecture. Consider security engineering from the beginning when designing a system, rather than bolting it in after the system is built.

- Improve efficiency
- Slower production time

Administrative Segmentation

Internal threats. Segment controls that no single authority can bypass all controls. Shamir's Secret Sharing (SSS). No one person has the root credentials.

Threat Modeling

Taking data from real-world adversaries and evaluating those attack patterns and techniques against our people, processes, systems and software. 

Threat Intelligence

Refined data in the context of the organization. Allows taking informed action to improve processes, procedures, tactics and controls.








