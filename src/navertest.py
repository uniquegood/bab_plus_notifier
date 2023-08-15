import requests
import uuid
import time
import json

api_url = 'https://3ujt8lvfy9.apigw.ntruss.com/custom/v1/24386/e890d862c2f310989f6511160e92a159b64dadbd27d5b0094f61baf9884d8003/general'
secret_key = 'aWhoVmVpdEZOTVRDSk5veVFZbHVEYkpPZHhGS3ZSSEc='
image_file = '/home/ubuntu/bab_plus_notifier/image/init08월15일20시12분39초330589.png'

request_json = {
    'images': [
        {
            'format': 'jpeg',
            'name': 'demo',
            'url' : 'https://postfiles.pstatic.net/MjAyMzA4MTFfMTMw/MDAxNjkxNzI4OTczODA1.idU4ZAvQLTE-V53MM8xfhQLaeU6KV7g_-EEY2EMF2tEg.0shpDw-oEIPFCfadmtPCKoYWVfwOXAxVPXKcG8KCzf4g.JPEG.babplus123/2.jpg?type=w773'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'lang' : "ko",
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key,
  'Content-Type' : 'application/json'
}

response = requests.request("POST", api_url, headers=headers, data = json.dumps(request_json).encode('UTF-8'))

result = json.loads(response.text)
result2 = result["images"]
print(response)
print(response.status_code)
print(result2[0]['fields'])