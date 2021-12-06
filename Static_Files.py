# Python Flask 網站後端開發：https://www.youtube.com/watch?v=_nkb0Olc3FQ&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=4
# 靜態檔案處理 Static Files

# 1. 什麼是靜態檔案？
#    不執行程式，直接將檔案送到前端，ex.圖片檔、影片檔、HTML, CSS, JAVASCRIPT
# 2. 靜態檔案路徑的設定
# 2.1 預設靜態檔案路徑 (static)
# 2.2 自訂靜態檔案路徑 (static_folder, static_url_path) : 後端工程師要自己設定

from flask import Flask
app=Flask(
    __name__,
    static_folder="public",  #自己設定靜態檔案的"資料夾名稱"
    static_url_path="/" ##自己設定靜態檔案對應的"網址路徑"
)  
# app.py為主程式，建立app物件，用 __name__ 就可以分辨我的程式是被 import 當成模組還是被直接執行的。這樣附帶的好處就是如果我寫的程式平常可以被 import 來使用，但有時它自己也可以直接執行。其它語言的話，可能就要區分 library 跟使用 library 的程式，而 python 的話這兩者的界線就很模糊
# 設靜態檔案：所有在public資料夾下的檔案，都對應到網址路徑/檔案名稱

# 建立"路徑 / " 對應的處理函式
@app.route("/") #@為函式的裝飾(decorator):以函式為基礎，提供附加的功能
def index():   # 用來回應"路徑 / " 的處理函式
     return "Hello Flask" #回傳給瀏覽器chrome的內容

@app.route("/Bruce") #這支程式：產生根目錄下的"網站路徑"
def test():
    return "Hello Bruce"

# 建立動態路由
@app.route("/user/<username>") 
def handleUser(username):
    if username=="伯俊":
        return "加油"+username
    else:
        return "Hello"+username

if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號

# sol(1):預設法
# 創建static資料夾，把圖片丟進去
# 伺服器會直接把static檔案夾的圖片，送至前端
# http://127.0.0.1:3000/static/紅髮傑克.png

# sol(2):自訂法
# 建立Application物件時，可自訂靜態檔案的路徑
