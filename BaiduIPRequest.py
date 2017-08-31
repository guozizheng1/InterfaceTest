import http.client

conn = http.client.HTTPSConnection("sp0.baidu.com")

headers = {
    'cache-control': "no-cache",
    'postman-token': "055eb847-5976-d16a-81b3-71068d4a5474"
    }

conn.request("GET", "/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=2.2.2.2&co=&resource_id=6006", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode('gbk'))
