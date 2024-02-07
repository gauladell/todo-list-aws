import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json
from dotenv import load_dotenv
import pytest

load_dotenv()
#BASE_URL = os.environ.get("BASE_URL")
BASE_URL = os.getenv('BASE_URL')
#BASE_URL = "https://m0qwfec693.execute-api.us-east-1.amazonaws.com/Prod"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_listtodos(self):
        print('---------------------------------------')
        print('Starting - integration test List TODO')
        #Add TODO
        url = BASE_URL+"/todos"
        data = {
         "text": "Integration text example"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add Todo: '+ str(json_response))
        jsonbody= json.loads(json_response['body'])
        ID_TODO = jsonbody['id']
        print ('ID todo:'+ID_TODO)
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example", "Error en la petición API a {url}"
        )
        #List
        url = BASE_URL+"/todos"
        response = requests.get(url)
        print('Response List Todo:' + str(response.json()))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a {url}"
        )
        self.assertTrue(response.json())
        
        print('End - integration test List TODO')
   
   
   
    
