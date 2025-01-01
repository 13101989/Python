# Define AWS access key ID variable
variable "AWS_ACCESS_KEY_ID" {
  description = "AWS access key ID"
}

# Define AWS secret access key variable
variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS secret access key"
}

# Configure Terraform settings
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  cloud {
    organization = "my-skillab"

    workspaces {
      name = "development"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}


resource "tls_private_key" "access_key" {
  algorithm   = "ED25519"
  ecdsa_curve = "P521"
}

output "private_key" {
  value     = tls_private_key.access_key.private_key_openssh
  sensitive = true
}

resource "aws_key_pair" "public_key" {
  key_name   = "ec2-public-key"
  public_key = tls_private_key.access_key.public_key_openssh
}

resource "aws_security_group" "django_app_security_group" {
  name        = "django-app"
  description = "Allow SSH and HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "django_app_ec2_instance" {
  ami             = "ami-04f9a173520f395dd"
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.public_key.key_name
  security_groups = [aws_security_group.django_app_security_group.name]

  user_data = file("${path.module}/deploy/deploy_django_app.sh")

  tags = {
    Name = "DjangoAppInstance"
  }
}