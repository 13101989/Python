# Steps to deploy

```bash

terraform fmt
terraform init
terraform validate
terraform plan
terraform apply --auto-approve

terraform output -raw private_key > ec2-private-key.pem && chmod 400 ec2-private-key.pem
```