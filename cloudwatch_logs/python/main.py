#!/usr/bin/env python

import boto3
client = boto3.client('logs')

def main():
    try:
        response = client.create_log_group(
            logGroupName='python_demo',
            tags={
                'string': 'string'
            }
        )
    except:
        print("Error creando logGroupName")

    try:
        response = client.create_log_stream(
            logGroupName='python_demo',
            logStreamName='string'
        )
    except:
        print("Error creando logStreamName")

    response = client.describe_log_streams(
        logGroupName='python_demo',
        logStreamNamePrefix='string'
    )
    print(response)

    response = client.put_log_events(
        logGroupName='python_demo',
        logStreamName='string',
        logEvents=[
            {
                'timestamp': 123,
                'message': 'string'
            },
        ],
        sequenceToken="0"
    )
    print(response)



if __name__=="__main__":
    main()
