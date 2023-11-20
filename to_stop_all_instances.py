import boto3
import json


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # to get all regions
    response = ec2.describe_regions()

    for region in response['Regions']:
        print(region['RegionName'])

        # give access key id and access secret id in below client
        ec1 = boto3.client('ec2', region_name=region['RegionName'])

        # to get instance id's within one region
        response1 = ec1.describe_instances()

        for instances in response1['Reservations']:
            for i in instances['Instances']:
                print(i['InstanceId'])

                if i['State']['Name'] != 'stopped':
                    ec1.stop_instances(InstanceIds=[i['InstanceId']])
                    print(f"{i['State']['Name']} and instance id:{i['InstanceId']}")

                print(f"{i['State']['Name']} and instance id:{i['InstanceId']}")
    
    return {
        "statuscode": 200,
        'body':'All Instances stopped'
    }
   
# note - you can add time condition using cloud watch action based on cron job