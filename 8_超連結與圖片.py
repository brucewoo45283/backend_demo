# https://www.youtube.com/watch?v=7NWmRmMOgz8&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=9
# 1. 網站前端基礎
#    網站前端發出request請求給後端，後端回應HTML程式碼給前端
# 1.1 撰寫 HTML 網頁網址
# 1.2 使用超連結:比起直接使用網址，提供使用者良好的互動介面，使其能輕易上手
#     <a href="網址">可點擊的內容</a>
# 1.3 使用圖片 <img src="圖片網址"/>

# 2. 網站後端基礎
# 2.1 靜態檔案處理
# 2.2 樣板引擎

# 3. 前後端互動
# 3.1 超連結的運作方式
# 3.2 圖片的運作方式

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

# 對到首頁:建立路徑/對應的處理函式，使用樣板檔案建立超連結
@app.route("/")
def index():
    return render_template("index.html")  # 回應超連結給前端、前端在給另一個圖片超連結的請求，
                                          # 後端再把圖片回應給前端


# 對到第二個網頁:建立路徑/對應的處理函式，使用樣板檔案建立超連結
@app.route("/page")  #  /page對到的是路由
def page():
    return render_template("page.html") # 前端抓的是路徑，非檔名ㄛ~


if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號
