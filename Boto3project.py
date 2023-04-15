import boto3


ec2 = boto3.resource('ec2')

    
dev = ec2.create_instances(
    ImageId='ami-06e46074ae430fba6',  
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'Development'},
                {'Key': 'ENV','Value': 'Development'}
                
            ]
        }
    ]
)

print(dev)

