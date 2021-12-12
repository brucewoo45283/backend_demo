# https://www.youtube.com/watch?v=ICrA5aRUIKw&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=8&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B
# 樣板引擎 Template Engine

# 1. 後端回應前端的方式
# 1.1 第一種:回應字串
# 1.2 第二種:回應 JSON 格式字串
# 1.3 第三種:重新導向
# 1.4 第四種:使用樣板引擎，優點為方便撰寫複雜的前端程式&方便在回應中，動態的代入資料

# 2. 樣板引擎 Template Engine
# 2.1 建立樣板檔案:必須建立在專案的templates子資料夾底下
# 2.2 使用樣板檔案:透過render_template()根據樣板檔案的內容產生字串
# 2.3 加入資料欄位在樣板檔案中:利用{{資料欄位名稱}}定義欄位
import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask import request         #載入request物件
import json  #載入json
from flask import redirect        # 載入函式redirect
from flask import render_template # 載入函式 render_template
app=Flask(
    __name__,
    static_folder="public",       #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/"           #自己設定靜態檔案對應的"網址路徑"
)  

# 建立路徑/對應的處理函式
@app.route("/")
def index():
    # 優點:可以直接在index檔案去修改，很方便，不用寫在python程式碼:用在"我想寫複雜一點的內容顯示在前端"，可以在index搭配html語法，事半功倍，可詮釋更好的畫面
    return render_template("index", name="伯俊")  #templates資料夾下的檔案index，取出樣板檔案中的內容變成字串，回應給前端，並把資料"伯俊"動態地代入欄位名稱name


if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號
