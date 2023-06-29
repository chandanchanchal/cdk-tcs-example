#!/usr/bin/env python3
import os

import aws_cdk as cdk

from monitoring.monitoring_stack import MonitoringStack
from monitoring.custom_cloudwatch_live_dashboard import CustomCloudwatchLiveDashboardStack
from monitoring.custom_cloudwatch_metrics import CustomMetricsStack
from monitoring.custom_ec2_with_alarms import CustomEc2WithAlarmsStack



app = cdk.App()
CustomEc2WithAlarmsStack(app, "CustomEc2WithAlarmsStack")
CustomMetricsStack(app, "CustomMetricsStack")
CustomCloudwatchLiveDashboardStack(app, "CustomCloudwatchLiveDashboardStack")


app.synth()
