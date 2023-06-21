#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_vpc_ec2.cdk_vpc_ec2_stack import CdkVpcEc2Stack
from cdk_vpc_ec2.cdk_rds_stack import CdkRdsStack
from cdk_vpc_ec2.cdk_ec2_stack import CdkEc2Stack

app = cdk.App()

vpc_stack = CdkVpcEc2Stack(app, "cdk-vpc")


ec2_stack = CdkEc2Stack(app, "cdk-ec2",vpc=vpc_stack.vpc)
rds_stack = CdkRdsStack(app, "cdk-rds",vpc=vpc_stack.vpc,
                        asg_security_groups=ec2_stack.asg.connections.security_groups)
app.synth()
