# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def egress_rule(security_group_id):

    try:
        response = vpc_client.authorize_security_group_egress(
            GroupId=security_group_id,
            IpPermissions=[{
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }, {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{
                    'CidrIp': '0.0.0.0/0'
                }]
            }])

    except ClientError:
        logger.exception('It can not be create egress security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    SECURITY_GROUP_ID = input("Enter the security group ID")
    logger.info(f'Please wait, We are checking a security group egress rule...')
    rule = egress_rule(SECURITY_GROUP_ID)
    logger.info(
        f'Wow!! Your Security group egress rule has been created : \n{json.dumps(rule, indent=4)}')