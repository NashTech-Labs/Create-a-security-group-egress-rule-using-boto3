# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION")
logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client = boto3.client("ec2", region_name=REGION)


def egress_rule(security_grp_id):

    try:
        res = client.authorize_security_group_egress(
            GroupId=security_grp_id,
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
        logger_for.exception('It can not be create egress security group rule.')
        raise
    else:
        return res


if __name__ == '__main__':
    SECURITY_GRP_ID = input("Enter the security group ID")
    logger_for.info(f'Please wait, We are checking a security group egress rule...')
    rule = egress_rule(SECURITY_GRP_ID)
    logger_for.info(
        f'Wow!! Your Security group egress rule has been created : \n{json.dumps(rule, indent=4)}')