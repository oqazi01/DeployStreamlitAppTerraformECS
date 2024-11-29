# Indicate where to source the terraform module from.
# The URL used here is a shorthand for
# "tfr://registry.terraform.io/terraform-aws-modules/vpc/aws?version=5.8.1".
# Note the extra `/` after the protocol is required for the shorthand
# notation.
terraform {
  source =  "git::git@github.com:oqazi01/DeployStreamlitAppTerraformECS.git//modules/vpc?ref=v0.0.2"
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
  vpc_name = "streamlit-vpc-dev"

  vpc_cidr= "10.0.0.0/16"

  public_subnet_cidrs= ["10.0.1.0/24", "10.0.2.0/24"]

  private_subnet_cidrs= ["10.0.3.0/24", "10.0.4.0/24"]

}

