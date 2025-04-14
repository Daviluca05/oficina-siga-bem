variable "region" {
  default = "us-east-2"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami" {
  default = "ami-0d866da98d63e2b42
"
}

variable "key_name" {
  default = "fastapi_key"
}

variable "docker_image" {
  default = "ronierisonmaciel/login-app:latest"
}