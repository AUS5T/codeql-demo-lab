# Example: Unencrypted EBS volume (intentionally insecure)

resource "aws_ebs_volume" "unencrypted_volume_demo" {
  availability_zone = "us-east-1a"
  size              = 10

  encrypted = false
}
