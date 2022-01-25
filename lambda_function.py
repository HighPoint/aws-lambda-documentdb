import json
import os
import sys
import pymongo


def lambda_handler(event, context): 
     
 
    client = pymongo.MongoClient('mongodb://<USERNAME>:<PASSWORD>@<FULL CLUSTER ENDPOINT NAME>:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&retryWrites=false') 
    
    db = client.sample_database
    
    col = db.sample_collection
    
    col.insert_one({'hello':'PyMongo DocumentDB'})
    
    x = col.find_one({'hello':'PyMongo DocumentDB'})
    
    print(x)

    client.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
