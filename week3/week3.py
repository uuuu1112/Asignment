import urllib.request as request
import json 

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

with request.urlopen(src) as response:
    data=json.load(response)
    
clist=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for viewpoint in clist:
        file.write(viewpoint["stitle"]+","+viewpoint["longitude"]+","+viewpoint["latitude"]+","+viewpoint["file"].replace("http:","#http:").split("#")[1]+"\n")
