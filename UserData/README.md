# Examples

Using `cloud-config` and shell scripts with cloud-init:

* Official project: https://cloudinit.readthedocs.io/
* AWS docs: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html

# Deploy

`aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file $MYYAML --stack-name s1 --parameter-overrides MyLaunchTemplate=lt-abcd1234`

