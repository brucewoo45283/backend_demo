# https://www.youtube.com/watch?v=kIQ5bRuRKqg&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=5
# 1. 關於 HTTP Request
# 1.1 前端發送請求，ex.在瀏覽器打上網址
# 1.2 後端Flask 套件接收請求 ，協助處理網路連線底層：將相關資訊封裝在request物件之中 
# 1.3 Flask 提供請求物件，取得資訊

# 2. 請求request物件的各種屬性
# 2.1 請求方法 Method
# 2.2 通訊協定 Scheme
# 2.3 主機名稱 Host
# 2.4 路徑 Path
# 2.5 完整網址 URL

# 3. 請求物件的標頭 Request Headers (附加資訊)
# 3.1 使用者代理 user-agent 
# 3.2 偏好語言 accept-language
# 3.3 引薦網址 referrer

# 設定一下紀錄的層次
import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request #載入request物件
app=Flask(
    __name__,
    static_folder="public",  #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/" ##自己設定靜態檔案對應的"網址路徑"
)  

# 建立"路徑 / "clear
# 對應的處理函式
@app.route("/")  # @為函式的裝飾(decorator):以函式為基礎，提供附加的功能
def index():
    # print("請求方法", request.method)   # 必需在伺服器端重整，就會打印在終端機
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("完整的網址", request.url)
    # 透過請求標頭，來取得額外資訊，user agent標頭使用者代碼: request(物件).headers(屬性).get(方法)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    # 設計一個機制，能因應前端，給出對應的需求
    lang=request.headers.get("accept-language")
    print("語言偏好", lang)   #印出前後端互動執行細節(注意前端如何回應給後端):語言偏好 zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,es;q=0.5
    if lang.startswith("en"): #如果是前端調成英文，回應給他hello；前端調成中文，回應給他你好
        return "Hello Flask"
    else:
        return "你好"

@app.route("/Bruce") #這支程式：產生根目錄下的"網站路徑"
def test():
    return "Hello Bruce"


@app.route("/user/<username>") 
def handleUser(username):
    if username=="伯俊":
        return "加油"+username
    else:
        return "Hello"+username

if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號
