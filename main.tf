terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"  # You can check for the latest version in the Terraform Registry
    }
  }
}

provider "aws" {
  region = "your-aws-region" # Replace with your preferred AWS region
}