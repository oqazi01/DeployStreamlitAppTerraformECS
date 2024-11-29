# Infrastructure Deployment Using Terragrunt

This project provides Infrastructure as Code (IaC) automation using Terraform and Terragrunt. Terragrunt simplifies managing Terraform configurations, remote states, and module dependencies.

# ECS Fargate Service Module

This is an example of how to use Terraform to deploy an [ECS Fargate Service](https://aws.amazon.com/ecs/) with an 
[Application Load Balancer (ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) in front of 
it. 


## Prerequisites
1. **Install Terraform**:
   - Download and install Terraform from the [official Terraform website](https://www.terraform.io/downloads.html).
   
2. **Install Terragrunt**:
   - Download and install Terragrunt from the [Terragrunt GitHub repository](https://github.com/gruntwork-io/terragrunt).
   - Verify installation:
     ```bash
     terragrunt --version
     ```
   
3. **AWS CLI** (if applicable):
   - Ensure the AWS CLI is installed and configured with credentials:
     ```bash
     aws configure
     ```

4. **Access Permissions**:
   - Ensure your AWS credentials or IAM role has the necessary permissions for the infrastructure being deployed.

---

## Project Structure
The repository follows a modular structure:

```plaintext
├── modules/
│   ├── vpc/
│   ├── app-service/ 
│ 
├── deployment/
│   ├── dev
│   │   └── vpc
|   |         └──terragrunt.hcl
|   |
│   │   └── app-service
|   |         └──terragrunt.hcl 
│   ├── prod
│   │   └── vpc
|   |         └──terragrunt.hcl
│   │   └── app-service
|   |         └──terragrunt.hcl
|   |
└── terragrunt.hcl
```

- modules: Contains reusable Terraform modules.
- environments: Defines configurations specific to environments (dev prod).
- terragrunt.hcl: Central configuration for remote state and shared settings

## Setup
- clone repository
```bash
git clone [https://github.com/oqazi01/DeployStreamlitAppTerraformECS.git](https://github.com/oqazi01/DeployStreamlitAppTerraformECS.git)
cd ~/DeployStreamlitAppTerraformECS
```
## Configure Environment Variables
```bash
export AWS_ACCESS_KEY_ID=<your-aws-access-key>
export AWS_SECRET_ACCESS_KEY=<your-aws-secret-key>
export AWS_DEFAULT_REGION=<region>
```

## Remote State Configuration
- Ensure that the remote_state block in terragrunt.hcl is configured for your backend (e.g., S3):
```bash
remote_state {
  backend = "s3"
  config = {
    bucket         = "my-terraform-state"
    key            = "env/terraform.tfstate"
    region         = "us-east-2"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## Usage
1. **Navigate to the Environment Directory**
```bash
cd deployments/prod/vpc
```
2. **Initialize Terragrunt**
```bash
terragrunt init
```
3. **Plan the Deployment**
```bash
terragrunt plan
```
4. **Apply the Changes**
```bash
terragrunt apply
```
5. **Navigate to the App Service Directory and Repeate Steps 1- 4**
```bash
cd deployments/prod/app-service
``` 
7. **Destroy the Infrastructure **
```bash
terragrunt destroy
```
## Customizing Inputs
You can pass variables to your Terraform modules via the inputs block in ```bash terragrunt.hcl ``` For example:
```bash
inputs = {

name= "lama-app"
Environment="prod" # prod or dev
desired_count=2
cpu=256
memory=512
container_port=8501
alb_port=80
secret_keys={

  OPENAI_API_KEY="<secret key>"
  
  SERPAPI_KEY="<secret key>"
  
  }

}

```



