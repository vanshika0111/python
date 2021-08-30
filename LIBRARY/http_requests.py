import requests
from requests import status_codes

# GET REQUEST
r = requests.get("https://www.wikipedia.org/")
print(r.text)
print(r.status_codes)
# status = 200 implies everything is perfect. You are good to go

# POST REQUEST
url = "www.hello.com"
data = { "p1":10, "p2":20}
r2 = requests.post(url=url, data=data)