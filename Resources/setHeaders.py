import os
import boto3
from response import Response
from ssm import getSSM

class SetHeaders:
    def __init__(self):
        self.APIKEY = getSSM.response

    def createHeader(self):
        '''Creates the needed headers to call the API Gateway'''
        if self.APIKEY.success:
            headers = {'content-type' : "application/json", 'Bearer API_KEY ': self.APIKEY.response}
            return headers
        return {'content-type' : "application/json"}

    