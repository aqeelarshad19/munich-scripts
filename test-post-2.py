import requests
import time
# url = "https://www.muenchen.de/termin/index.php"

querystring = {"cts":"1080805"}
url = "https://www46.muenchen.de/termin/index.php?cts=1080805"
termin_data = {
    'step': 'WEB_APPOINT_SEARCH_BY_CASETYPES',
    'CASETYPES[Niederlassungserlaubnis Blaue Karte EU]': 1,
}
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"step\"\r\n\r\nWEB_APPOINT_SEARCH_BY_CASETYPES\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"CASETYPES[Niederlassungserlaubnis Blaue Karte EU]\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "5b6112e2-9865-4549-a75e-f8ab3f163bd1"
    }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
session = requests.Session()
print(session.cookies)
response = session.post(url, data=termin_data )
# session.get(url)
print(session.cookies)
print(session.cookies.get_dict())

time.sleep(2)
response = session.post(url, data=termin_data , cookies=session.cookies)
# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
print(response.text)
