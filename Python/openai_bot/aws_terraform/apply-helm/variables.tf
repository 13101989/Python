# Define AWS access key ID variable
variable "AWS_ACCESS_KEY_ID" {
  description = "AWS access key ID"
}

# Define AWS secret access key variable
variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS secret access key"
}

# Define secrets variables
variable "REST_CLIENT_SECRET" {
  description = "OPENAI authentication secret"
}
variable "POSTGRES_DB" {
  description = "Postgres database name"
}
variable "POSTGRES_USER" {
  description = "Postgres login user"
}
variable "POSTGRES_PASSWORD" {
  description = "Postgress login password"
}
variable "POSTGRES_HOST" {
  description = "ost of postgres database"
}

variable "region" {
  description = "AWS region"
  type        = string
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}