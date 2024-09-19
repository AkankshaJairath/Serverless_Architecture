import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Get all instances with the 'Auto-Stop' tag
    auto_stop_instances = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop1']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Get all instances with the 'Auto-Start' tag
    auto_start_instances = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start1']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    # Stop the instances tagged 'Auto-Stop'
    stop_instance_ids = [instance['InstanceId'] 
                         for reservation in auto_stop_instances['Reservations']
                         for instance in reservation['Instances']]
    
    if stop_instance_ids:
        ec2_client.stop_instances(InstanceIds=stop_instance_ids)
        print(f'Stopped instances: {stop_instance_ids}')
    else:
        print('No instances to stop.')

    # Start the instances tagged 'Auto-Start'
    start_instance_ids = [instance['InstanceId'] 
                          for reservation in auto_start_instances['Reservations']
                          for instance in reservation['Instances']]

    if start_instance_ids:
        ec2_client.start_instances(InstanceIds=start_instance_ids)
        print(f'Started instances: {start_instance_ids}')
    else:
        print('No instances to start.')

    return {
        'statusCode': 200,
        'body': 'EC2 Instance management complete'
    }