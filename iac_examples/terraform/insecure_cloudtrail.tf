# Intentionally insecure example for security scanning demonstration
# Demonstrates missing logging / monitoring controls

resource "aws_cloudtrail" "insecure_demo_trail" {
  name                          = "demo-cloudtrail"
  s3_bucket_name                = "demo-cloudtrail-bucket"
  include_global_service_events = false
  is_multi_region_trail         = false
  enable_logging                = false
}
