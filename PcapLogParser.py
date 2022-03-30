import json
import boto3
import logging
from botocore.exceptions import ClientError


def PcapParse(PcapInput):
    
    _json_out_file_name = 'output.txt'
    file = open(_json_out_file_name, 'r')
    data = []
    
    
