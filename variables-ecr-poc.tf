variable "aws_region" {
  default = "us-east-1"
}

variable "ecr_repo_name" {
  default = "mon-app"
}

variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
}

variable "security_group_ids" {
  description = "List of security group IDs"
  type        = list(string)
}
