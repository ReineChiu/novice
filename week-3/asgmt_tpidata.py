import urllib.request as request
import json 
import time 
import re

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response: 
    data=json.load(response)   

clist=data["result"]["results"]

with open("data.csv","w",encoding="utf-8") as file:
    start_date = "2015/01/01"  
    for material in clist:
        area = material["address"] 
        print(area)
        if material["xpostDate"] < start_date :
            continue
        web = material["file"]
        img = (re.split("jpg|JPG", web)) 
        first_img = img[0]+"jpg"

        file.write(material["stitle"]+","+area[5:8]+","+material["longitude"]+","+material["latitude"]+","+first_img+"\n")

