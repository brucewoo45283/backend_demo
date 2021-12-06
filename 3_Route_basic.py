# https://www.youtube.com/watch?v=ytP9CSTm1p8&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=3
from flask import Flask
app=Flask(__name__)  #app.py為主程式，建立app物件，用 __name__ 就可以分辨我的程式是被 import 當成模組還是被直接執行的。這樣附帶的好處就是如果我寫的程式平常可以被 import 來使用，但有時它自己也可以直接執行。其它語言的話，可能就要區分 library 跟使用 library 的程式，而 python 的話這兩者的界線就很模糊

# 範例一
# 路由可以決定網站要支援那些路徑
# 建立"路徑 / " 對應的處理函式
@app.route("/") #@為函式的裝飾(decorator):以函式為基礎，提供附加的功能
def index():   # 用來回應"路徑 / " 的處理函式
     return "Hello Flask" #回傳給瀏覽器chrome的內容

@app.route("/Bruce") #這支程式：產生根目錄下的"網站路徑"
def test():
    return "Hello Bruce"

# if __name__=="__main__": #如果以主程式進行
#     app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號

# 範例二 : 建立動態路由
# @app.route("/user/<username>") 
# def handleUser(username):
#     return "Hello"+username

# if __name__=="__main__": #如果以主程式進行
#     app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號


# 範例三 : 建立動態路由
@app.route("/user/<username>") 
def handleUser(username):
    if username=="伯俊":
        return "加油"+username
    else:
        return "Hello"+username

if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號


