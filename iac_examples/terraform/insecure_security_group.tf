# Intentionally insecure Terraform example for Checkov demonstration

resource "aws_security_group" "demo_sg" {
  name        = "demo-open-sg"
  description = "Security group with open access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
