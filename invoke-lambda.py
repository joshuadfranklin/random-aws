#!/usr/bin/env python3
import os
import sys
import json
import boto3
import base64
import botocore
import logging

level=os.environ.get("LOGLEVEL", "DEBUG")
logging.basicConfig(level=level)
awsregion=os.environ.get("AWS_DEFAULT_REGION", "us-east-1")

if len(sys.argv) < 2:
    print('Usage: %s FunctionName' % sys.argv[0])
    sys.exit(0)

payload=json.loads('{}')
if len(sys.argv) == 3:
    try:
        payload= json.loads(sys.argv[2])
    except ValueError:
        logging.error('Caught a ValueError loading JSON args! You provided\n  %s\nIs it formatted like this?\n  \'{"a": ["x","y"]}\' ', sys.argv[2])
        sys.exit(1)

awslambda = boto3.client('lambda', region_name=awsregion, config=botocore.config.Config(retries={'max_attempts': 1}))
response = awslambda.invoke(
    FunctionName=sys.argv[1],
    LogType='Tail',
    Payload=json.dumps(payload)
)

print('\n\nLambda Log Tail and Response:\n')
out = base64.b64decode(response['LogResult'])
print(out.decode("unicode_escape"))
print(response['Payload'].read().decode("utf-8"))

# AWS CLI equivalent:
#aws lambda invoke --function-name $F --payload {} --log-type Tail --query LogResult --output text lambdaout.87103 | base64 -d

