# EC2Trigger-Lambda
Start and stop EC2 instances through your Lambda function

Can be useful when interacting with EC2 instance from an external endpoint, like Discord or Telegram Bots

To interact with EC2 instance, your Lambda IAM role must have this Statement:
```
{
  "Effect": "Allow",
  "Action": [
      "ec2:Start*",
      "ec2:Stop*"
  ],
  "Resource": "*"
}
