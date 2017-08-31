import http.client

conn = http.client.HTTPSConnection("d.jd.com")

headers = {
    'cache-control': "no-cache",
    'postman-token': "7261f103-3fae-530a-c364-88d9b72e3624"
    }

conn.request("GET", "/area/get?fid=72&callback=jQuery2164963&_=1504155423288", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("gbk"))