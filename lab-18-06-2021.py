import datetime
import requests
import json


r = requests.get("https://index.golang.org/index?since=2021-06-10T19:08:52.997264Z")
print(r.status_code)
# entity = json.loads(r.strip(r.json))
# print(entity)
r.json()
