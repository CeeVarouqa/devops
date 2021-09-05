resource "aws_instance" "dev" {
  ami           = "ami-005e54dee72cc1d00" # us-west-2
  instance_type = "t2.micro"

  tags = {
    service = "docker"
  }

  security_groups = [aws_security_group.allow-all.name]

  credit_specification {
    cpu_credits = "unlimited"
  }
}

resource "aws_security_group" "allow-all" {
  name        = "allow_all_rules"
  description = "Allow inbound traffic from SSH and web"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow-rules"
  }
}
