"""
// Lambda function code

module.exports.handler = async (event) => {
  console.log('Event: ', event);
  let responseMessage = 'Hello, World!';
  if (event.queryStringParameters && event.queryStringParameters['Name']) {
      responseMessage = 'Hello, ' + event.queryStringParameters['Name'] + '!';
      }
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message: responseMessage,
    }),
  }
}

import json
def lambda_handler(event, context):   
    print("Hello from Lambda!!!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
"""
import json
import random
import string
import random
import string
import re
def lambda_handler(event, context):

  return {
          'statusCode': 200,
          'body': json.dumps('Hello from Lambda!')
      }