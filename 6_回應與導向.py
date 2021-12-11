# https://www.youtube.com/watch?v=p5RoBuO3tSc&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=7
# Python Flask 網站後端開發：
# 回應與導向 Response
# 前端request後端、後端response前端
# 1. 後端回應前端的方式
# 1.1 回應字串
# 1.2 回應 JSON 格式字串
# 1.3 重新導向

# 2. JSON 格式字串
# 2.1 載入 json 模組
# 2.2 使用 json.dumps() 將字典列表的組合轉換成 JSON 格式的字串

# 3. 重新導向
# 3.1 載入 redirect() 函式
# 3.2 導向到同網站的其它路徑
# 3.3 導向到其他網站


import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request #載入request物件
import json  #載入json
from flask import redirect # 載入函式redirect
app=Flask(
    __name__,
    static_folder="public",  #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/" ##自己設定靜態檔案對應的"網址路徑"
)  

# 第一種首頁的處理函式:
# 建立路徑" / " 對應的處理函式
# 重新導向到別的網址redirect
#@app.route("/")  # @為函式的裝飾(decorator):以函式為基礎，提供附加的功能
#def index():
    #  把首頁重新導向到別的網址
    #  return redirect("https://training.pada-x.com/online_premium.htm")
    # # 設計一個機制，接收前端使用者的語言偏好，給出對應的需求
    # lang=request.headers.get("accept-language")
    # if lang.startswith("en"): #回傳值為json格式的資料，json.dumps可以把字典轉成json的字串，送到前端
    #     return json.dumps({
    #         "status":"ok",
    #         "text":"Welcome Flask"
    #     })
    # else:
    #     return json.dumps({
    #         "status":"ok",
    #         "text":"這是首頁"
    #         }, ensure_ascii=False) # 不要用ascii此種編碼來處理中文


# 另一種首頁的呈現方式:產生英文、中文兩種首頁
# 使用者如果語言偏好為英文，把網址導向到英文根目錄
# 建立路由:/en/對應的處理函式
@app.route("/en/")
def index_english():
    return json.dumps({
             "status":"ok",
             "text":"Welcome Flask"
              }) 

# 建立路由:/zh/對應的處理函式
@app.route("/zh/")
def index_chinese():
    return json.dumps({
             "status":"ok",
             "text":"這是首頁"
            }, ensure_ascii=False)

# 依照中文、英文路由、建立導向:如果使用者今天連到首頁，就依語言偏好來判斷，導向中文or英文
@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")  
    else:
        return redirect("/zh/")
        


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
