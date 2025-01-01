# Define AWS access key ID variable
variable "AWS_ACCESS_KEY_ID" {
  description = "AWS access key ID"
}

# Define AWS secret access key variable
variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS secret access key"
}

variable "region" {
  description = "AWS region"
  type        = string
}

variable "instance_type" {
  description = "Instance type"
  type        = string
}