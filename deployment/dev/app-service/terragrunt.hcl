# Indicate where to source the terraform module from.
# The URL used here is a shorthand for
# "tfr://registry.terraform.io/terraform-aws-modules/vpc/aws?version=5.8.1".
# Note the extra `/` after the protocol is required for the shorthand
# notation.
terraform {
  source =  "git::git@github.com:oqazi01/DeployStreamlitAppTerraformECS.git//modules/app-service?ref=v0.0.1"
}

# Indicate what region to deploy the resources into
generate "provider" {
  path = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
provider "aws" {
  region = "us-east-2"
}
EOF
}

# Indicate the input values to use for the variables of the module.
inputs = {

name= "lama-app-dev"
Environment="dev" # prod or dev
desired_count=1
cpu=256
memory=212
container_port=8501
alb_port=80
secret_keys={

  OPENAI_API_KEY=getenv("OPENAI_API_KEY")
  
  SERPAPI_KEY=getenv("SERPAPI_KEY")
  
  }

}