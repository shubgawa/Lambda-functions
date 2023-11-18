import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    bucket_name = []
    keys = []

    for i in response['Buckets']:
        bucket_name.append(i['Name']) #getting bucket names

    source = bucket_name[0] #note- add condition where you can take source which you want
    print(source)
    target = bucket_name[1] #note- same goes for target
    print(target)

    response1 = s3.list_objects_v2(Bucket=source) #to get object details in it

    for i in response1.get('Contents', []): # 'Contents' gives us the key name, creation date and all 
        keys.append(i['Key'])

    print(keys)

    for i in keys:
        copysource = {'Bucket': source, 'Key': i} #loop is added to ,copy all keys in a bucket to target
        print(copysource)
        output = s3.copy_object(CopySource=copysource, Bucket=target, Key=i) 

    return {
        "statuscode": 200,
        'body':'All objects copied successfully!'
    }