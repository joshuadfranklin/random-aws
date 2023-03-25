# Examples

Using `cloud-config` and shell scripts with cloud-init in Amazon Linux 2023:

* Official project: https://cloudinit.readthedocs.io/
* AWS docs: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
* AL2023: https://aws.amazon.com/blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/

# Deploy

```
# Create Launch Template stack
aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file cfn-al2023-launchtemplate-InstanceProfile-IMDSv2.yaml --stack-name lt-al2023

# Find Launch Template ID
aws ec2 describe-launch-templates --output text --query 'LaunchTemplates[].[CreateTime,LaunchTemplateId,LaunchTemplateName,DefaultVersionNumber,LatestVersionNumber]' | sort

# Create Instance stack
aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file $MYYAML --stack-name is1 --parameter-overrides MyLaunchTemplate=lt-abcd1234

```
