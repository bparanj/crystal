## Downloading a PEM File from AWS Secrets Manager using AWS CLI

To download or retrieve the secret value from AWS Secrets Manager using the AWS CLI and the secret name, you can use the `aws secretsmanager get-secret-value` command. Here is how you would do it for a secret named "ror_key_secret-pqc11in5":

```bash
aws secretsmanager get-secret-value --secret-id ror_key_secret-pqc11in5
```

You must specify a region. You can also configure your region by running "aws configure".

This command returns a JSON object that contains the secret value. If the secret is a string, it can be found in the `SecretString` field of the output. For binary secrets, the `SecretBinary` field will be populated instead.

Replace `"ror_key_secret-pqc11in5"` with your  secret name.

Also, ensure your AWS CLI is configured with the appropriate credentials and region to access the Secrets Manager service. If you need to specify a region different from your default configuration, you can add the `--region` flag to your command, like so:

```bash
aws secretsmanager get-secret-value --secret-id ror_key_secret-pqc11in5 --region us-west-2
```

To extract the `SecretString` from the JSON response and store it in a file named `rails.pem`, you can use the AWS CLI command combined with `jq` and redirection.

```
brew install jq
```

The command:

```sh
aws secretsmanager get-secret-value --secret-id "ror_key_secret-pqc11in5" --region us-west-2 | jq -r '.SecretString' > rails.pem
```

This command performs the following actions:

1. It retrieves the secret value using `aws secretsmanager get-secret-value`.
2. It pipes (`|`) the JSON output to `jq`, which extracts the `SecretString` field.
3. It redirects the output of `jq` (the secret value) to a file named `rails.pem` using `>`.

After running this command, the file `rails.pem` will contain the secret value extracted from the AWS Secrets Manager response.

To include changing the permissions of `rails.pem` to `400` after creating the file, you can simply append a `&&` followed by the `chmod` command. Here's the revised command:

```sh
aws secretsmanager get-secret-value --secret-id "ror_key_secret-pqc11in5" --region us-west-2 | jq -r '.SecretString' > rails.pem && chmod 400 rails.pem
```

This command does the following:

1. Retrieves the secret value and stores it in `rails.pem`.
2. After the file is successfully created, it changes the permissions of `rails.pem` to `400` (read-only for the owner), ensuring that the file is securely stored.

## Downloading a PEM File from AWS Secrets Manager Using JavaScript

To use AWS Secrets that are defined as environment variables in your JavaScript code, especially when working with Node.js, you can use the `process.env` object. This object provides access to the environment variables set in the environment where the Node.js application is running.

If you have AWS Secrets like AWS Access Key ID and AWS Secret Access Key stored in environment variables ( named `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`), you can access these within your JavaScript code to configure the AWS SDK as follows:

First, ensure your environment variables are set. You can set them temporarily in the terminal (for the current session only) or permanently by adding them to your shell profile file (e.g., `~/.bash_profile`, `~/.bashrc`, `~/.zshrc`).

Temporary setting in the terminal:

```sh
export AWS_ACCESS_KEY_ID='your-access-key-id'
export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
export AWS_REGION='us-west-2'  # Optionally set the default region
```

Then, in your JavaScript code, you can access these environment variables and use them to configure the AWS SDK:

```javascript
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

// Access environment variables
const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;
const region = process.env.AWS_REGION || "us-west-2"; // Use 'us-west-2' if AWS_REGION is not set

const secret_name = "ror_key_secret-gtdruaz6";

// Configure the AWS Secrets Manager client
const client = new SecretsManagerClient({
  region: region,
  credentials: {
    accessKeyId: accessKeyId,
    secretAccessKey: secretAccessKey,
  },
});

async function getSecret() {
  let response;

  try {
    response = await client.send(
      new GetSecretValueCommand({
        SecretId: secret_name,
        VersionStage: "AWSCURRENT", // VersionStage defaults to AWSCURRENT if unspecified
      }),
    );
    // Assuming the secret is a string
    console.log("Secret:", response.SecretString);
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
}

// Call the function to get the secret
getSecret();
```

This example demonstrates how to use environment variables to securely configure the AWS SDK without hardcoding sensitive information in your source code. It's a common practice to manage credentials and other sensitive configurations.

The error you're encountering is due to Node.js treating your script as a CommonJS module, not an ES module, which is required to use the `import` syntax. To resolve this issue, you have two main options:

### Option 1: Convert Your Script to Use ES Module Syntax

1. **Set "type": "module" in Your `package.json`**

   Add or modify the `type` field in your `package.json` to `module`. This tells Node.js to treat all `.js` files in your project as ES modules.

   ```json
   {
     "name": "your-project-name",
     "version": "1.0.0",
     "type": "module",
     "scripts": {},
     "dependencies": {}
   }
   ```

2. **Run Your Script Again**

   After making this change, you should be able to run your script with `node keyDownload.js` without the import error.

### Option 2: Use CommonJS Syntax

If you prefer not to use ES modules, you can convert the import statements to CommonJS `require` syntax.

1. **Modify Your Script**

   Convert the `import` statements to `require`:

   ```javascript
   const { SecretsManagerClient, GetSecretValueCommand } = require("@aws-sdk/client-secrets-manager");

   // The rest of your script...
   ```

2. **Ensure Dependencies Are Installed**

   Make sure you've installed the AWS SDK for JavaScript v3 in your project:

   ```bash
   npm install @aws-sdk/client-secrets-manager
   ```

3. **Run Your Script**

   You should now be able to run your script with `node keyDownload.js` using the CommonJS syntax.

### Additional Tips

- Ensure you're using a version of Node.js that supports ES modules and the features you're using in your script. While ES module support has been stable since Node.js 12, later versions provide more features and better stability.
- If you switch to ES modules and use `import`, remember that some Node.js features behave differently compared to CommonJS modules, such as how imports and exports are handled.
- If you encounter further issues related to modules or syntax, consider checking your Node.js version and updating it if necessary.
