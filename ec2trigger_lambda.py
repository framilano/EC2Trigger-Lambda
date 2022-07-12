import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel("INFO")

region = 'eu-south-1'   #or whatever region your instances are in
ec2 = boto3.client('ec2', region_name=region)
#payload/event example
#{   
#    "trigger": "stop",
#    "instances": ["istance-id0", "istance-id1"]
#}
def lambda_handler(event, context):
    payload_body = {}
    if (type(event['body']) is str): payload_body = json.loads(event['body'])
    else: payload_body = event['body']
    
    logger.info(f"INPUT: {payload_body}")
    
    trigger = payload_body['trigger']
    instances = []
    response_body = ""
    if ('instances' in payload_body):
        instances = payload_body['instances']
    
    if (trigger == "stop"):
        ec2.stop_instances(InstanceIds=instances)
        response_body = json.dumps("Stopped EC2 instances")
    else:
        ec2.stop_instances(InstanceIds=instances)
        response_body = json.dumps("Started EC2 instances")
    
    return {
        'statusCode': 200,
        'body': response_body
    }