provider "aws" {
  region = "us-east-1"  # Change this to your preferred region
}

resource "aws_ecr_repository" "my_app_repo" {
  name                 = "my-app-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "Dev"
    Project     = "Test"
  }
}
