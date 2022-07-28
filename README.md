## Create a AWS security Group Egress rule using boto3.

#### A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. An outbound rule permits instances to send traffic to the specified destination IPv4 or IPv6 CIDR address ranges, or to the specified destination security groups for the same VPC.You can follow this [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html) to know more.

-------------

**Files:** 
```
    security_grp_egress_rule.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create a egress rule.

        python3 security_grp_egress_rule.py
