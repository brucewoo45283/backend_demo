# https://www.youtube.com/watch?v=lss8dmoIyIc&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=12

# 使用者狀態管理 Session

# 1.  每次連線均有其獨立性：每次的連線都是獨立運作，彼此不關聯
# 1.1 後面的連線無法記得前面的連線提供的資訊

# 2. 使用者狀態管理
# 2.1 用途：讓後端可以紀錄一些前端的資訊，讓每次的連線之間可以保存狀態
#     流程圖：影片時間軸8:15
# 2.2 透過 Session 的機制完成狀態管理
import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request         #載入request物件
import json  #載入json
from flask import redirect        # 載入函式redirect
from flask import render_template # 載入函式 render_template
from flask import session         # 載入函式session

# 圖片的網址 http://127.0.0.1:3000/紅髮傑克.png
app=Flask(
    __name__,
    static_folder="public",       #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/"           #自己設定靜態檔案對應的"網址路徑"
)  
app.secret_key="any string but secret"  # 設定session的加密機制，密要為任何的祕密字串

# 對到首頁:使用GET方法，建立路徑/對應的處理函式，使用樣板檔案建立超連結
@app.route("/")
def index():
    return render_template("index.html")  # 回應超連結給前端、前端在給另一個圖片超連結的請求，
                                          # 後端再把圖片回應給前端

#  Session範例
# 使用GET方法處理路徑   /hello?name=使用者名字
@app.route("/hello")
def hello():
    name=request.args.get("name", "") #如果使用者忘了輸入，我就用空白替代
    session["username"]=name          # 存放輸入的資料：session["自訂的欄位名稱"]=資料
    return "你好，"+name

# 當使用者連線到/talk，期望網站能夠記住前面一次使用者輸入的名子
@app.route("/talk")
def talk():
    name=session["username"]          # 取得剛剛存放的資料
    return name+"，我記住你的名字囉"


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