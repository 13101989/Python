# Steps to deploy

```bash
cd deploy-eks
terraform init
terraform validate
terraform plan
terraform apply

assign EKSAdminPolicy to IAM principal account in AWS

cd apply-helm
terraform init
terraform validate
terraform plan
terraform apply
```