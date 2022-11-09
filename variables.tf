# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."

  type    = string
  default = "eu-west-1"
}
# curl "$(terraform output -raw base_url)/hello"
# aws lambda invoke --region=eu-west-1 --function-name=$(terraform output -raw function_name) response.json
