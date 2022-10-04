import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Has the lambda layer attached?')
    }
