# https://www.youtube.com/watch?v=w-XkIYBGCn0&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=6
# 1. 什麼是要求字串 (Query String)
# 1.1 網址的一部份，和路徑間用問號 ? 隔開
# 1.2 特定的撰寫格式
# 參數名稱=資料&參數名稱=資料&...
# 1.3 可以在同一個路徑下，傳遞更多附加資訊

# 2. 要求字串的處理
# 2.1 使用 request 物件
# 2.2 使用 request(物件).args(屬性).get(方法) 方法取得要求字串中的參數資料
# 2.3 使用預設值
# 前後端的互動:影片10:25

import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request #載入request物件
app=Flask(
    __name__,
    static_folder="public",  #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/" ##自己設定靜態檔案對應的"網址路徑"
)  



# 範例
# 建立路徑" /getSum " 對應的處理函式
# 並利用要求字串(Query String)提供彈性
# 能夠min(上限)加到max(下限): getSum?min=上限&max=下限，並給出預設值是1, 100
@app.route("/getSum")
def getSum():
    maxNumber=request.args.get("max", 100)
    maxNumber=int(maxNumber)  #字串轉成整數
    minNumber=request.args.get("min", 1)
    minNumber=int(minNumber)
    print("最大數字", maxNumber) #從前端在?後面的要求字串送出請求，後端接收並把結果打印在我的伺服器上
    res=0
    for i in range(minNumber,maxNumber+1):
        res+=i
    return "結果:"+str(res)




# 建立路徑" / " 對應的處理函式
@app.route("/")  # @為函式的裝飾(decorator):以函式為基礎，提供附加的功能
def index():
    # 設計一個機制，能因應前端，給出對應的需求
    lang=request.headers.get("accept-language")
    print("語言偏好", lang)   #印出前後端互動執行細節(注意前端如何回應給後端):語言偏好 zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,es;q=0.5
    if lang.startswith("en"): #如果是前端調成英文，回應給他hello；前端調成中文，回應給他你好
        return "Hello Flask"
    else:
        return "你好"

# 建立路徑"/Bruce "
@app.route("/Bruce") #這支程式：產生根目錄下的"網站路徑"
def test():
    return "Hello Bruce"

# 建立路徑"/user/<username> "
@app.route("/user/<username>") 
def handleUser(username):
    if username=="伯俊":
        return "加油"+username
    else:
        return "Hello"+username

if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號
