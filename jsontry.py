import json
import urllib.request

# with urllib.request.urlopen("http://127.0.0.1:5000/jsontry") as url:
#     data = json.loads(url.read().decode())
#     print(data)

user = "kedar"

try:
 with urllib.request.urlopen("http://127.0.0.1:5000/registertry/"+user) as url:
    #print(url)
    data = json.loads(url.read().decode())
    print(data)
except:
    print("Error on loading webpage")