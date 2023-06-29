#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ec2_cloudwatch.ec2_cloudwatch_stack import Ec2CloudwatchStack


app = cdk.App()
Ec2CloudwatchStack(app, "Ec2CloudwatchStack")

app.synth()
