import json
import re
import boto3 
import sys
import logging
import pymysql


logger = logging.getLogger()
logger.setLevel(logging.INFO)
    
try:
    rds_host  = "***********"
    name = "***********"
    password = "***********"
    db_name = "***********"
    
    print("try to coonect DB")
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit(1)

#==================================================


def lambda_handler(event, context):
    # TODO implement
    if isinstance(event['body'], str):
        body = json.loads(event['body'])
    else:
        body = event['body']
    
    print(body)
    print(type(body))
    
    
    ########### M1 -- comprehend
    
    print("Begin comprehend")
    
    comprehand  = boto3.client("comprehend")
    response = comprehand.detect_sentiment(Text = body['text'], LanguageCode="en")
    
    print("End comprehend")
    
    
    #####################
    # Save to Database  --- Begin
    with conn.cursor() as cur:
        
        sql = "INSERT INTO `FP706`.`emotion` \
                     (`uid`, `text`, `emotion`, `post_date`)  VALUES \
                     ('BOB123', \
                      '{}', \
                      '{}', \
                      '2020-10-31')".format(body['text'].replace("\\", "\\\\'")
                                                        .replace(u"'", u"\\'")
                                                        .replace(u'"', u'\\"'), 
                                            response['Sentiment'])
                      
        print(sql)
                          
        cur.execute(sql)
        conn.commit()
    conn.commit()
    
    #  Save to Database  --- End
    ################
    
    print(response)
    print(type(response))
    
    
    response_body =  {
        'Sentiment': response['Sentiment']
        #'SentimentScore': response['SentimentScore']
    }
    
    
    response = {
                "isBase64Encoded": False,
                "statusCode": 200,
                "headers": { 
                              "Access-Control-Allow-Headers" : "Content-Type",
                              "Access-Control-Allow-Origin": "*",
                              "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                    
                },
                "body": json.dumps(response_body)
            }



    return  response