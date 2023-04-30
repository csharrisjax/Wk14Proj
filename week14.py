import boto3


#create EC2 client for the us-east-1 region
ec2 = boto3.client('ec2', region_name='us-east-1')


# python code to retrieve instances with a specific tag
filters = [{'Name': 'tag:Environment', 'Values': ['Dev']}]
instances = ec2.describe_instances(filters)


#python code to stop each instance
for reservation in instances ['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceID']
        ec2.stop_instances(InstanceIDs=[instance_id])
        print(f'Stopping instance {instance_id}')