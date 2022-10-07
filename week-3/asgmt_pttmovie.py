#抓取 PTT 電影版的網路原始碼(HTML)
import urllib.request as req
import bs4

def getData(url): 
    #Ａ.建立一個 Request 物件，附加 Request headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
    })  #  模仿為一般使用者

    with req.urlopen(request) as response:  # A.項建立request物件，在此利用request物件來打開網址，讓抓取資料的行為看起來像使用者在做連線
        data=response.read().decode("utf-8")   #data=response.read()
    #print(data)

    #解析原始碼，取得每篇文章的標題
    root = bs4.BeautifulSoup(data, "html.parser")#data是從網路抓下 來的資料。"html.parser"告訴BeautifulSoup是html的格式，去做解析 
    #print(root.title.string)#root代表整份網頁，title是標籤，string代表要標籤內的文字
    #titles = root.find("div", class_="title") # find()只會尋找一個 class="title"的div標籤。(根據條件找)
    #print(titles.a.string) # 印出titles下a標籤的文字
    titles = root.find_all("div", class_="title") # 在div標籤下，find_all()會找尋找所有 class="title"的div標籤。
    print(titles) # 會印出列表    
    # # 抓取上一頁的連結       
    nextLink=root.find("a",string="‹ 上頁") # 在a標籤下，利用find 找出內文是"‹ 上頁"的a標籤
    #print出nextLink(下一個頁面)的["href"]屬性。
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
            if title.a != None and title.a.string[0:4] =="[好雷]" :#or title.a.string[0:4] == "[普雷]" or title.a.string[0:4] == "[負雷]") :  
                good = title.a.string
                goodlist.append(good)
    #print(goodlist)
            if title.a != None and title.a.string[0:4] =="[普雷]" :
                normal= title.a.string
                normallist.append(normal)
    #print(normallist)
            if title.a != None and title.a.string[0:4] =="[負雷]" :
                bad= title.a.string
                badlist.append(bad)
    alllist = goodlist + normallist + badlist
    file.write("\n".join(alllist)) 
