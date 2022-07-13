import json
import boto3
import logging
from base64 import b64decode


logger = logging.getLogger()
logger.setLevel("INFO")

region = 'eu-south-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    logger.info(f"INPUT: {event['body']}")
    if (event['body'] is str): payload_body = json.loads(event['body'])
    else: payload_body = event['body']

    trigger = payload_body['trigger']
    instances = []
    response_body = ""
    if ('instances' in payload_body):
        instances = payload_body['instances']
    
    if (trigger == "stop"):
        ec2.stop_instances(InstanceIds=instances)
        response_body = "Stopped EC2 instances"
    elif (trigger == "start"):
        ec2.start_instances(InstanceIds=instances)
        response_body = "Started EC2 instances"
    else: response_body = "No valid action selected for EC2 - Check payload fields"
    return {
        'statusCode': 200,
        'body': response_body
    }
