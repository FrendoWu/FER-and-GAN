import requests
import urllib2
# import urllib
import json
import base64
server_url = 'http://127.0.0.1:10080'
with open('/home/wings/temp/ferwebapp/fer-service/src/fer/1.png', 'rb') as fin:
    image_data = fin.read()
    base64_data = base64.b64encode(image_data)
req = urllib2.Request(server_url, json.dumps({'data': base64.b64encode(image_data)}),{'Content-Type': 'application/json'})
f = urllib2.urlopen(req, timeout = 60)
predictions = json.loads(f.read())
print(predictions)
#print(json.dumps({'data': base64.b64encode(image_data)}),{'Content-Type': 'application/json'})