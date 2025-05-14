import boto3
import json
region = '<your instance region>'


def lambda_handler(event, context):
    ec2_connection = boto3.resource(service_name='ec2', region_name=region)
    filter_ec2=[{"Name": "instance-state-name", "Values": ["stopped"]},
               {"Name":"tag:AutoStartUp","Values":["true"]}]
               
    instances_started = False
    for instance in ec2_connection.instances.filter(Filters=filter_ec2):
        print("Start instance:", instance.id)
        instance.start()
        instances_started = True
        
    if instances_started:
        message = "Starting instance!"
    else:
        message = "No instance to Start."
    
    return{
        'statusCode':200,
        'body':json.dumps(message)
    } 