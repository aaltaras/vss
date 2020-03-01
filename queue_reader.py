import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.eu-north-1.amazonaws.com/530342348278/aaltaras-vmware-sqs'

def queue_read():

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    
    print ("response: " +  str(response)) 
    try:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received and deleted message: %s' % message)

    except KeyError:
        print('No messages on the queue!')
        message = ""
    
    return message
