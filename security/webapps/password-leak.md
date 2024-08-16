Here's a Mermaid diagram that illustrates the automatic leakage of a password reset link:

```mermaid
sequenceDiagram
    participant User
    participant WebApp
    participant Attacker

    User->>WebApp: Request password reset
    WebApp->>User: Send password reset link via email
    WebApp->>Attacker: Automatically leak password reset link
    Attacker->>WebApp: Access password reset link
    Attacker->>WebApp: Set new password for user's account
    Attacker->>WebApp: Gain unauthorized access to user's account
```

In this diagram:

1. The User requests a password reset from the WebApp.
2. The WebApp sends a password reset link to the User via email.
3. However, due to a vulnerability or misconfiguration, the WebApp automatically leaks the password reset link to the Attacker.
4. The Attacker accesses the leaked password reset link.
5. The Attacker uses the password reset link to set a new password for the User's account.
6. The Attacker gains unauthorized access to the User's account using the newly set password.

This diagram highlights the potential security risk of automatically leaking password reset links, which can allow attackers to compromise user accounts without the user's knowledge or consent.
