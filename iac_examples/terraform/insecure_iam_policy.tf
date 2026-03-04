# Example: Overly permissive IAM policy (intentionally insecure)

resource "aws_iam_policy" "overly_permissive_demo" {
  name = "demo-admin-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}
