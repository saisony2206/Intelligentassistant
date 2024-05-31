import requests

from gemini import gemin
headers = { 
  "apikey": "api"}
k="next IPL match"
params = (
   ("q",k),
);

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);
# print(gemin(response.text))
print(response.text)