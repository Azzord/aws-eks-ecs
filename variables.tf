variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "availability_zone" {
  description = "AZ to deploy resources"
  default     = "us-east-1a"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
  description = "CIDR block for the subnet"
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "SSH key name for EC2 access"
  type        = string
}
