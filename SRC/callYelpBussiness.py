import os
import json
import urllib3
import csv
import io
import datetime
import boto3
import urllib3
from Resources.setHeaders import SetHeaders
from Resources.reviewProcessor import ReviewProcessor

def getYelpReviews(event, context):
    try: 
        #Build Endpoint so someday can drop in other resturant ids other than Hungry Sumo
        endpointBase = os.environ['YELP_BUSINESS_REWIEW_ENDPOINT_BASE']
        endpointSuffix = os.environ['YELP_BUSINESS_REWIEW_SUFFIX']
        hungrySumoId = os.environ['HUNGRY_SUMO_ID']
        
        endpoint = endpointBase + hungrySumoId + endpointSuffix

        #set Bearer Header for Yelp
        headers = SetHeaders().createHeader()
        if headers.success:
            http = urllib3.PoolManager()
            resp = http.request('GET', url=endpoint, headers=headers.response)
            if (resp.status == 200):
                reviews = json.loads(resp.data.decode('utf-8'))['reviews']
                formatedReviewsResponse = ReviewProcessor(reviews).processReviews()
                if formatedReviewsResponse.success:
                    return ({
                        "statusCode" : 200,
                        "body" : json.dumps(formatedReviewsResponse.response)
                    })
                else:
                    return ({
                        "statusCode" : 412,
                        "body" : json.dumps(formatedReviewsResponse.message)
                    })
        else:
            return ({
                "statusCode" : 401,
                "body" : headers.message
            })
    except Exception as e:
        return({
            "statusCode" : 412,
            "body" : json.dumps("Fatal Error in intial call, Exception [" + e + "]")
        })
   

    
    