import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='eu-north-1')

queue_url = 'https://sqs.eu-north-1.amazonaws.com/530342348278/aaltaras-vmware-sqs'

def queue_write(): 

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )
    
    print(response['MessageId'])
