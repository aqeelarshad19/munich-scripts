import http.client

conn = http.client.HTTPConnection("www46,muenchen,de")

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"step\"\r\n\r\nWEB_APPOINT_SEARCH_BY_CASETYPES\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"CASETYPES[Niederlassungserlaubnis Blaue Karte EU]\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "b892d1f4-9beb-43ba-b9d3-4cc9f22cd30a"
    }

conn.request("POST", "termin,index.php", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
