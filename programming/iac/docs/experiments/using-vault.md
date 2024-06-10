## AWS Credentials and Vault

1. Create a new IAM user
2. Provide full EC2 access and use that policy
3. Generate credentials for CLI access
4. Save the credentials in Vault Secrets
5. Install vault and check the credentials on laptop

On Mac:

```
brew tap hashicorp/tap
brew install vlt

vlt login
vlt config init

vlt secrets get -plaintext {desired secret}
vlt run -c "python3 my_app.py"
```
