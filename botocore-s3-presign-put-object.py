#!/usr/bin/env python3
import os
import argparse
import botocore
import botocore.session

awsregion=os.environ.get("AWS_DEFAULT_REGION", "us-east-1") # must match bucket region because of sigV4

parser = argparse.ArgumentParser(description=f'Generate a PUT method S3 signed URL for {awsregion} only (because of sigV4)')
parser.add_argument('-b', '--bucket', required=True, help=f'name of your bucket in {awsregion}')
parser.add_argument('-k', '--key', required=True, help='S3 path for upload, for example prefix/key')
parser.add_argument('-s', '--seconds', type=int, help='seconds until URL expires, default and max is 604800 (7 days)', default=604800)
args = parser.parse_args()
 
session = botocore.session.get_session()
s3 = session.create_client('s3')
url = s3.generate_presigned_url('put_object', Params={'Bucket': args.bucket, 'Key': args.key, 'Expires': args.seconds})
print(f'curl "{url}" --upload-file yourfile.txt')

