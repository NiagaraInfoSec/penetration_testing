import os
import os.path

import requests
from requests.auth import HTTPBasicAuth

def test_convert():
    with open("zamzar_api_key.key", "rb") as _file:
        api_key = _file.read()
    
    endpoint = "https://sandbox.zamzar.com/v1/jobs"
    target_format = "csv"
    
    source_files = os.path.join("..", "data", "schools")
    for filename in os.listdir(source_files):
        source_file = os.path.join(source_files, filename)
        if os.path.isfile(source_file):
            with open(source_file, "rb") as _file:
                file_content = {"source_file" : _file}        
                data_content = {'target_format': target_format}
                res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
                print res.json()
                break