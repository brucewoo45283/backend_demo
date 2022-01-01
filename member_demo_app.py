# 初始化資料庫連線：讓後端程式隨時可以跟資料庫互動
import pymongo
client=pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.fkc7n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db=client.member_system      # 資料庫名稱自訂為member_system，存進變數db
print("資料庫連線成功!")

# 初始化 Flask 伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"
# app.run(port=3000)

# 一、建立前端頁面規劃：以使用者角度換位思考
# https://www.youtube.com/watch?v=QVcHHiOc0P0&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=22
# 首頁（路由:/）：在首頁註冊成功後，登入後進入會員頁面（路由:/member），並有登出的功能
# 首頁註冊失敗後，登入失敗導向錯誤頁面（路由:/error，要求字串利用樣板引擎自動帶入客製化資訊?msg=錯誤訊息）

# (一)處理首頁路由
# 建立templates專案資料夾：
##底下建置member_demo_index.html【! 加 TAB ，VSCODE會快速幫使用者建立一個HTML頁面】來處理前端首頁的呈現
@app.route("/")
def index():  
    return render_template("member_demo_index.html")

# (二)處理會員頁面路由
# templates專案資料夾底下，建置member_demo.html來處理前端會員頁面之呈現
@app.route("/member")
def member():  # 使用者權限管理："會員頁面"只給曾經登入成功的人看，用後端邏輯檢查使用者的登錄狀態，不能讓使用者僅僅key in網址就能進到我們的會員頁面
    if "nickname" in session:  # 假設session裡有存放會員的暱稱資料，代表他曾經走過登入這個程序
        return render_template("member_demo.html") # 給這種人看會員頁面
    else:     # 還沒登入過的人，導回首頁
        return redirect("/")

# (三)處理錯誤頁面路由
# templates專案資料夾底下，建置member_demo_error.html來處理登入錯誤頁面之呈現
# (四)要求字串處理錯誤頁面，客製化錯誤訊息，回應給使用者必須是彈性、不能寫死，可以自動帶入彈性訊息
@app.route("/error")
def error():
    # 處理要求字串：?msg=錯誤訊息【欄位名稱為msg，並塞入變數message，預設值為"發生錯誤，請重新檢視您輸入的資料"】
    message=request.args.get("msg", "發生錯誤，請重新檢視您輸入的資料")
    # 記得把要求字串(錯誤訊息之文字)整合進樣板引擎中
    # 動態帶入資料:變數message，帶進第二個參數"message"【參數名稱=我要帶入的資料】
    # member_demo_error.html對應之處理: {{message}}
    return render_template("member_demo_error.html", message=message)




# 二、建立會員註冊功能
# https://www.youtube.com/watch?v=QkxqaHrS314&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=23
# 規劃概念：當使用者在首頁按下註冊的按鈕，導向路由/signup，為一功能性路由，不負責網頁呈現；真正的功能是負責與資料庫互動，會到資料庫檢查、新增會員資料
# (一) 會員註冊功能規劃
# (二) 首頁建立註冊表單：在member_demo_index.html寫表單、按鈕，特別注意變數name
# (三) 建立註冊功能路由：特別注意，前端使用<form action="/signup" method="POST">導向後端路由程式
# (四) 檢查資料庫中的註冊信箱是否重複，並完成註冊
@app.route("/signup", methods=["POST"])
def signup():
    # 接收前端的資料
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    # print(nickname, email, password) # 在終端機印出，可檢核程式運行是否正確
    # 根據前端接受到的資料，和資料庫互動
    # 把所有會員資料都放到集合user
    # .find_one 來檢查會員集合中之文件資料中的email有無重複
    collection=db.user
    res=collection.find_one({
        "email":email
    })
    #                                建立商業邏輯：取資料邏輯判斷式
    # 如果變數res不等於空值 → 表資料已存在 → 表使用者輸入的email已被使用過 → 把使用者導向錯誤頁面
    if res != None: 
        return redirect("/error?msg=您的信箱已被註冊過")
    # 把前端的資料，透過後端程式，放進資料庫
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/")  # 登入成功，導回首頁


# 三、建立會員登入、登出功能
# https://www.youtube.com/watch?v=AhRhRizgU08&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=24
# 1. 會員登入功能規劃
# 1.1 首頁建立登入表單
# 1.2 建立登入功能路由
# 1.3 檢查資料庫中是否有對應的信箱和密碼，儲存會員資訊在 Session 中，登入成功

# 2. 會員登出功能規劃
# 2.1 會員頁建立登出連結：/signin登入成功，Session紀錄會員資訊，導向會員頁（/member）
# 2.2 建立登出功能路由（/signout）
# 2.3 登出成功：移除 Session 中的會員資訊

@app.route("/signin", methods=["POST"])
def signin():
    # 從前端抓取使用者輸入的資料
    email=request.form["email"]
    password=request.form["password"]
    # 與資料庫互動：資料庫member_system、集合user（存進變數db）
    collection=db.user 
    # 檢查使用者輸入的帳密是否正確：在集合中尋找有無重複的資料
    res=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    # 商業邏輯：如果res有在集合抓到一樣的資料，表示使用者輸入的帳密正確；反之，則導向錯誤頁面
    if res==None:
        return redirect("/error?msg=帳號或密碼輸入錯誤，請重新檢查")
    # 登入成功，導向會員頁面，在Session中記錄會員資訊
    session["nickname"]=res["nickname"]
    return redirect("/member")


# 在會員頁面，建立登出功能
@app.route("/signout")
def signout():
    del session["nickname"] # 刪除Sesson中的會員資訊
    return redirect("/")    # 導回首頁









app.run(port=3000)