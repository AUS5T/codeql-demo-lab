# Example: Public S3 bucket (intentionally insecure)

resource "aws_s3_bucket" "public_bucket_demo" {
  bucket = "demo-public-bucket-security-poc"
}

resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.public_bucket_demo.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
