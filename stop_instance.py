import boto3
import json
region = '<your instance region>'


def lambda_handler(event, context):
    ec2_connection = boto3.resource(service_name='ec2', region_name=region)
    filter_ec2=[{"Name": "instance-state-name", "Values": ["running"]},
               {"Name":"tag:AutoShutDown","Values":["true"]}]
               
    instances_stopped = False
    for instance in ec2_connection.instances.filter(Filters=filter_ec2):
        print("Stopping instance:", instance.id)
        instance.stop()
        instances_stopped = True
        
    if instances_stopped:
        message = "Stopping instance!"
    else:
        message = "No instance to stop."
    
    return{
        'statusCode':200,
        'body':json.dumps(message)
    } 