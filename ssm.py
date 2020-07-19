import boto3
import os
import urllib3
from Resources.response import Response

def getSSM(ssmName):
    name = os.environ[ssmName]
    client = boto3.client('ssm')
    ssmResponse = client.get_parameter(
        Name=name,
        WithDecryption=True
    )
    if ssmResponse['Parameter']['Value']:
        return Response(True, ssmResponse['Parameter']['Value'], ssmName + "SSM returned")
    
    return Response(False, None, "Failed to retirve SSM" + ssmName)