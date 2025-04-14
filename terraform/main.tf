provider "aws" {
  region = var.region
}

data "aws_security_group" "web_sg" {
  filter {
    name   = "group-name"
    values = ["web_seg_oficinamec"]
  }

  filter {
    name   = "vpc-id"
    values = ["vpc-036ff1a269a819515"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = var.ami
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [data.aws_security_group.web_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install -y docker.io
              sudo systemctl start docker
              sudo usermod -aG docker ubuntu
              docker run -d -p 80:80 ${var.docker_image}
              EOF

  tags = {
    Name = "Oficina-app"
  }
}