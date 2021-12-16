# https://www.youtube.com/watch?v=cjQVIDVBGyE&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=10
# https://www.youtube.com/watch?v=JxDx2rPYNjA&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=11
# 網站前後端互動的一種 - 表單 Form，可傳送額外資料，設定更多連線細節

# 1. 表單 HTML 基礎
# 1.1 使用 form 標籤
# 1.2 使用 action 屬性指定連線網址
# 1.3 使用按鈕送出表單

# 2. 表單前後端互動
# 2.1 透過 input 標籤接受使用者輸入
# 2.2 透過網址的要求字串 (Query String) 傳送資訊到後端
# 2.3 後端接收要求字串，並做出回應

# 前端html程式碼：發出請求（預設是用GET方法）到"網址路徑?data=使用者之輸入"
# POST方法，"data=使用者輸入"不顯示在網址後面，另外存放

# <form action="網址路徑"method="GET"> #method="POST"
#     <input type="text"name="data" />
#     <button>點擊送出表單</button>
# </form>

# 後端python程式

# @app.route("網址路徑",methods=["GET"])  # methods=["POST"]
# def handle():
#     input=request.args.get("data","")   # input=request.form("data")
#     return "給前端之回應"

# 網站前後端互動 - 連線方法 GET、POST

# 1. 連線方法的基礎觀念
# 1.1 同樣的網址，連線方法可以不同
# 1.2 常見的有 GET、POST
      # GET方法：直接輸入網址、超連結
      # 表單可以自己設定要POST方法或GET方法，POST用在讓使用者輸入機密資料，比較安全
# 1.3 其他的有 PUT、DELETE、PATCH

# 2. 使用表單設定連線方法
# 2.1 透過表單的 METHOD 屬性設定方法
# 2.2 後端接收 GET 方法的要求字串 (Query String)
# 2.3 後端接收 POST 方法的要求字串 (Query String)


import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request         #載入request物件
import json  #載入json
from flask import redirect        # 載入函式redirect
from flask import render_template # 載入函式 render_template

# 圖片的網址 http://127.0.0.1:3000/紅髮傑克.png
app=Flask(
    __name__,
    static_folder="public",       #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/"           #自己設定靜態檔案對應的"網址路徑"
)  

# 對到首頁:使用GET方法，建立路徑/對應的處理函式，使用樣板檔案建立超連結
@app.route("/")
def index():
    return render_template("index.html")  # 回應超連結給前端、前端在給另一個圖片超連結的請求，
                                          # 後端再把圖片回應給前端

# 表單1：處理路徑/show的對應函式 （對應到templates資料夾裡的index.html檔前端程式碼）
@app.route("/show")
def show():
    name=request.args.get("n", "")
    return "歡迎光臨，"+name

# 表單2：使用POST方法（要求字串與GET不同!），處理路徑/calculate的對應函式 
# 對應到templates資料夾裡的index.html檔前端程式碼，再另創建樣板檔案result.html來美化前端的顯示，把動態的資料結果，代入樣板引擎，最後讓使用者可以點擊回首頁  
# 以技術人員來觀察，使用者"計算結果"之資料沒有顯示在"網址列"（對使用者來說，確保他們輸入的資料是安全的），就是使用POST，要求字串被存放在Request Body，可以打開前端Network檢查                                 
@app.route("/calculate", methods=["POST"])
def calculate():
    # 接收GET方法的Query String
    # maxN=request.args.get("max", "")
    # 接收POST的要求字串寫法為
    maxN=request.form["max"]
    maxN=int(maxN)
    # 1加到maxN
    res=0
    for i in range(1, maxN+1):
        res+=i
    return render_template("result.html", data=res)


# 對到第二個網頁:建立路徑/對應的處理函式，使用樣板檔案建立超連結
@app.route("/page")  #  /page對到的是路由
def page():
    return render_template("page.html") # 前端抓的是路徑，非檔名ㄛ~


if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號