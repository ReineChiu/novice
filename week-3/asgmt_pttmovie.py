import urllib.request as req
import bs4

def getData(url): 
    
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
    })  #  模仿為一般使用者

    with req.urlopen(request) as response:  # A.項建立request物件，在此利用request物件來打開網址，讓抓取資料的行為看起來像使用者在做連線
        data=response.read().decode("utf-8")   

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
       
    nextLink=root.find("a",string="‹ 上頁") 
    return nextLink["href"]#return把屬性傳遞出來


with open("movie.txt","a",encoding="utf-8") as file:
    goodlist = [ ]
    normallist = [ ]
    badlist = [ ]

    for i in range(9506,9496,-1):
        link = "https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
        getData(link)
        titles = getData(link)

        for title in getData(link):
            if title.a != None and title.a.string[0:4] =="[好雷]" :
                goodlist.append(good)
            if title.a != None and title.a.string[0:4] =="[普雷]" :
                normal= title.a.string
                normallist.append(normal)
            if title.a != None and title.a.string[0:4] =="[負雷]" :
                bad= title.a.string
                badlist.append(bad)
    alllist = goodlist + normallist + badlist
    file.write("\n".join(alllist)) 
