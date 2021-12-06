# https://www.youtube.com/watch?v=dYulda6wEWA&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=23
from flask import Flask
app=Flask(__name__)  #app.py為主程式，建立app物件，用 __name__ 就可以分辨我的程式是被 import 當成模組還是被直接執行的。這樣附帶的好處就是如果我寫的程式平常可以被 import 來使用，但有時它自己也可以直接執行。其它語言的話，可能就要區分 library 跟使用 library 的程式，而 python 的話這兩者的界線就很模糊

@app.route("/") #@為函式的裝飾(decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello Flask" #回給瀏覽器chrome

@app.route("/test") #這支程式：產生根目錄下的"網站路徑"
def test():
    return "This is test"

if __name__=="__main__": #如果以主程式進行
    app.run(port=3000)  #立刻啟動伺服器，可透過port參數指定埠號

# 產生測試連結(根目錄):http://127.0.0.1:5000/ 
# 這支程式，就是網站的伺服器

# Heroku 雲端主機教學 https://www.youtube.com/watch?v=wWRYBUzEG6E&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=24
# Python Flask 部屬到 Heroku 的完整教學：

# 1. 建立專案描述檔
# 1.1 建立 runtime.txt
# 1.2 建立 requirements.txt
# 1.3 建立 Procfile

# 2. 安裝 Git Tool

# 3. 建立 Heroku App 應用程式
# 3.1 註冊帳號，注意信箱驗證
# 3.2 建立 Heroku 應用程式

# 4. 部屬到 Heroku App
# 4.1 安裝 Heroku CLI 命令列工具
# 4.2 執行初始化命令
# 4.3 執行部屬命令





