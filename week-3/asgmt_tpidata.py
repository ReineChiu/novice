#下載特定網址資料
import urllib.request as request
import json # 網路資料是json 所以載入json套件 
import time # 使用time模組進行日期比較  time 模組提供了 strptime 方法來操作日期。輸入字串格式的日期
import re

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:  # with request.urlopen(網址) as response
    data=json.load(response)   #利用jaon模組處理json資料格式        #data=response.read()
# print(data)
# # 解讀json使用內建json模組
# # 取得想要的資料
clist=data["result"]["results"]
#print(clist)
with open("data.csv","w",encoding="utf-8") as file:
    start_date = "2015/01/01"  #設定要比較的時間值
    for material in clist:
        area = material["address"] # print(area[5:8]) 只取字串中第5,6,7位的字元
        print(area)
        if material["xpostDate"] < start_date :
            continue

        web = material["file"]
        img = (re.split("jpg|JPG", web)) # 用｜分開多個分隔符,之間不要有其他不是要作為分隔符字串、符號，甚至空格
#        img = web.split("jpg")
        first_img = img[0]+"jpg"

        file.write(material["stitle"]+","+area[5:8]+","+material["longitude"]+","+material["latitude"]+","+first_img+"\n")
#    print(sitetitle["xpostDate"])
## file:的鍵值有多個檔案連結在一起,彼此之間沒有用","隔開 但又必須取第一個檔案連結
## 想法1.將鍵值直接改成我要的,再把最新的資料複製回檔案中,做讀取
## 想法2.字串分割使用split() ： 檔案有固定格式,結尾都是.jpg,所以用jpg做隔開,回頭再加上+"jpg"
