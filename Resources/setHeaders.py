import os
import boto3
from Resources.response import Response
from Resources.ssm import getSSM

class SetHeaders:
    def __init__(self):
        self.APIKEY = getSSM('YELP_API_KEY')

    def createHeader(self):
        '''Creates the needed headers to call the API Gateway'''
        if self.APIKEY.success:
            headers = {'content-type' : "application/json", 'Authorization':'Bearer ' + self.APIKEY.response}
            return Response(True, headers, "Successfully set headers")
        return Response(False, None, self.APIKEY.message)

    