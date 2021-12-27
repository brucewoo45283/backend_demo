# MongoDB 資料庫簡介、快速開始
# https://www.youtube.com/watch?v=B9X_0v9EEdI&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=14

#                                         【MongoDB 簡介】
# 1.1 非關聯式資料庫
# 1.2 友善 JSON 格式
# 1.3 簡潔的文件模型
# 1.4 較容易水平擴展

# 2. 建置 MongoDB 資料庫
# 2.1 使用官方 MongoDB Atlas 雲端服務
# https://cloud.mongodb.com/v2#/preferences/organizations
# 2.2 註冊雲端服務帳戶
# 2.3 建立組織、專案
# 2.4 管理遠端存取權限設定
# 2.5 建立資料庫叢集(Database)：程式連線到資料庫，所要的帳密root/root123

# 3. 使用 Python 程式與 MongoDB 資料庫互動
# 3.1 安裝 pymongo[srv] 套件
# 3.2 使用帳號密碼連線資料庫
# 3.3 新增資料到資料庫中

# 載入pymongo[srv]套件
import pymongo
# # 連線到雲端資料庫：要從Datebase的connect your application去找，複製整段程式碼、填入自設帳號密碼
client=pymongo.MongoClient("mongodb+srv://root:root123@mycluster.fkc7n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# # 把資料插入資料庫：存放在test資料庫的users集合裡，自己取名
db = client.mywebsite    # 選擇要操作的資料庫：變數 = client.資料庫名稱
collection=db.users # 選擇操作users集合

# # 把資料新增到集合中：json格式在python中就是字典
# collection.insert_one({
#     "name":"leehom",
#     "email":"leehom@cdc.gov.tw",
#     "password":"good",
#     "level":1
# })
# print("資料新增成功")  # 如果前面都沒error，就會在終端機打印這行字串

#                                               【MongoDB 資料庫結構】
# https://www.youtube.com/watch?v=hNGo0kTvigE&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=15
# 1.  三層式結構 Document-Based：Document → Collection → Database
# 1.1 資料庫 (Database)
# 1.2 集合 (Collection)
# 1.3 文件 (Document)
##### 文件儲存使用 JSON 格式
##### Python 程式中的對應操作 

#                                               【MongoDB 新增資料】
#  https://www.youtube.com/watch?v=NS1KiGdx9Nc&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=16
# 1. 一次新增一筆資料
# 1.1 使用 insert_one
#     集合.insert_one(文件資料)
# 1.2 使用 inserted_id 取得資料獨立的編號

# 2. 一次新增多筆資料
# 2.1 使用 insert_many：list裡面放dictionary
#     集合.insert_many([文件資料1, 文件資料2, ...])
# 2.2 使用 inserted_ids 取得多筆資料獨立編號

#範例

# import pymongo
# # 連線到雲端資料庫：
# client=pymongo.MongoClient("mongodb+srv://root:root123@mycluster.fkc7n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# # 把資料插入資料庫：存放在test資料庫的users集合裡，自己取名
# db = client.mywebsite    # 選擇要操作的資料庫：變數 = client.資料庫名稱
# collection=db.users      # 選擇操作users集合

# 把資料新增到集合中：
# result=collection.insert_one({
#     "name":"leehom",
#     "email":"leehom@cdc.gov.tw",
#     "password":"good",
#     "level":1
# })
     
# print(result.inserted_id)  # 取得資料id

# 使用 insert_many 插入多筆資料
# db=client.mywebsite
# result=collection.insert_many([{
#     "name":"Jack",
#      "email":"jack@cdc.gov.tw",
#      "password":"jack",
#      "level":2
#  }, {"name":"Kobe",
#      "email":"kobe@cdc.gov.tw",
#      "password":"kobe",
#      "level":3
#  },{"name":"Jet",
#      "email":"jet@cdc.gov.tw",
#      "password":"jet",
#      "level":1
# }, {"name":"Lebron",
#      "email":"lbj@cdc.gov.tw",
#      "password":"lbj",
#      "level":1
# }])
# print("資料新增成功") 
# print(result.inserted_ids)


#                                         【MongoDB 取得資料】
# 1. 一次取得一筆資料
# 1.1 使用 find_one 取得第一筆資料：集合.find_one()
# 1.2 使用 find_one 根據文件編號取得資料：文件編號是一個ObjectedId物件而非字串，必須從bson.objectid封包載入
# 1.3 注意文件編號 ObjectId 的使用

# 2. 一次取得多筆資料
# 2.1 使用 find 取得集合中所有資料的 Cursor
# 2.2 使用 for 迴圈逐一取得文件資料

# import pymongo
from bson.objectid import ObjectId
# client=pymongo.MongoClient("mongodb+srv://root:root123@mycluster.fkc7n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.mywebsite    # 選擇要操作的資料庫：變數 = client.資料庫名稱
# collection=db.users      # 選擇操作users集合
# 取得集合中的第一筆資料
# data=collection.find_one()
# print(data)
# 根據ObjectId 取得文件資料
# data=collection.find_one(
#     ObjectId("61becf3c3e0cd23443f2bf06")
#     )
# print(data)
# # 取得欄位
# print(data["_id"])
# print(data["email"])

# 把集合的資料全部取出
# 建立游標cursor物件
# cursor=collection.find()
# print(cursor) # <pymongo.cursor.Cursor object at 0x021A2FD0>
# # for迴圈
# for doc in cursor:
#     print(doc["name"])

#                                         【MongoDB 更新資料】
# https://www.youtube.com/watch?v=oNr5F1yWOjs&list=PL-g0fdC5RMboN18JNTMCEfe8Ldk8C5pS-&index=18
# 1. 更新資料基礎
# 1.1 篩選條件和更新方法
# 1.2 運用 update_one 更新一筆文件：集合.update_one(篩選條件, 更新的資訊)；更新資訊會是兩層的字典
# 1.3 運用 update_many 更新多筆文件：集合.update_many(篩選條件, 更新的資訊)；更新資訊會是兩層的字典

# 2. 更新資料方法
# 2.1 覆蓋、新增欄位：$set 
# 2.2 移除欄位：$unset 
# 2.3 統一加減數字型態的欄位：$inc 
# 2.4 統一乘除數字欄位：$mul 

# 3. 取得更新結果
# 3.1 運用 matched_count 取得符合篩選條件的文件數量
# 3.2 運用 modified_count 取得實際完成更新的文件數量

# 範例一： 更新一筆資料
# 撈出資料
# data=collection.find_one(
#      ObjectId("61c29ed32437cc081f79e4a2")
#      )
# print(data)

#更新這筆資料（用email來篩出資料、更新密碼）
# result=collection.update_one({
#     "email":'jack@cdc.gov.tw'
# },{
#     "$set":{
#         "password":"jack-revised"
#     }
# })
# print("符合條件的文件數：", result.matched_count)
# print("實際更新的文件數：", result.modified_count) # 出現0，是因為已經更改過了

#新增敘述並更新這筆資料
# result=collection.update_one({
#     "email":'jack@cdc.gov.tw'
# },{
#     "$set":{
#         "description":"編修第一次"
#     }
# })
# print("符合條件的文件數：", result.matched_count)
# print("實際更新的文件數：", result.modified_count)

# 刪除欄位
#新增敘述並更新這筆資料
# result=collection.update_one({
#     "email":'jack@cdc.gov.tw'
# },{
#     "$unset":{
#         "description":""
#     }
# })
# print("符合條件的文件數：", result.matched_count)
# print("實際更新的文件數：", result.modified_count)

# 更新數字型態的欄位:把level+100
# result=collection.update_one({
#     "email":'jack@cdc.gov.tw'
# },{
#     "$inc":{
#         "level":100
#     }
# })
# print("符合條件的文件數：", result.matched_count)
# print("實際更新的文件數：", result.modified_count)

# 更新數字型態的欄位:把level除以2
# result=collection.update_one({
#     "email":'jack@cdc.gov.tw'
# },{
#     "$mul":{
#         "level":0.5
#     }
# })

# print("符合條件的文件數：", result.matched_count)
# print("實際更新的文件數：", result.modified_count)


# 範例二：更新多筆
# 篩選所有level為1，直接更新為1000
# result=collection.update_many({
#      "level":1
#  },{
#      "$set":{
#          "level":1000
#      }
#  })
 
# print("符合條件的文件數：", result.matched_count) # 意義：檢核機制
# print("實際更新的文件數：", result.modified_count)

#                                                     【MongoDB 刪除資料】
# 1. 刪除資料方法
# 1.1 使用 delete_one 刪除一筆文件資料
# 1.2 使用 delete_many 刪除多筆文件資料
# 1.3 取得刪除的結果

# 使用 insert_many 插入多筆資料
# db=client.mywebsite
# result=collection.insert_many([{
#      "name":"John",
#       "email":"john@cdc.gov.tw",
#       "password":"john",
#       "level":4
#   }, {"name":"測試名稱一",
#       "email":"test1@cdc.gov.tw",
#       "password":"test1",
#       "level":5
#   },{"name":"測試名稱二",
#       "email":"test2@cdc.gov.tw",
#       "password":"test2",
#       "level":5
#  }, {"name":"測試名稱三",
#       "email":"test3@cdc.gov.tw",
#       "password":"test3",
#       "level":5
#  }])
# print("資料新增成功") 

#  刪除一筆文件資料:delete_one
# result=collection.delete_one({
#     "email":"test3@cdc.gov.tw"
# })
# print("實際上刪除的資料有幾筆", result.deleted_count)

# # 使用 delete_many 刪除所有level為5的文件資料
# result=collection.delete_many({
#     "level":5
# })
# print("實際上刪除的資料有幾筆", result.deleted_count)


#                                         【MongoDB 篩選、排序資料】
# 1. 篩選文件資料
# 1.1 使用 find_one 篩選一筆文件資料
# 1.2 使用 find 篩選多筆文件資料：集合.find(篩選條件)
# 1.3 使用 for 迴圈逐一取得篩選結果

# 2. 多重篩選條件
# 2.1 交集：使用 $and 結合篩選條件
# 2.2 聯集：使用 $or 結合篩選條件

# 3. 排序篩選結果：集合.find(篩選資料, sort=排序方式)
# 3.1 使用 sort 參數設定排序方式
# 3.2 使用 pymongo.ASCENDING 由小到大排序
#     游標cursor=集合.find({}, sort=[("欄位", pymongo.ASCENDING)])
#     再用for迴圈印出游標
# 3.3 使用 pymongo.DESCENDING 由大到小排序

# 範例一:交集，同時篩選帳密
# doc=collection.find_one({
#     "$and":[
#         {條件一},
#         {條件二}
#     ]
# })

doc=collection.find_one({
    "$and":[
        {"email":"kobe@cdc.gov.tw"},
        {"password":"kobe"}
    ]
})
print("取得資料:", doc)

# 範例二:聯集篩選 & 排序
cur=collection.find({
    "$or":[
        {"email":"jack@cdc.gov.tw"},
        {"level":1000}
    ]
}, sort=[
    ("level", pymongo.DESCENDING)
])

for doc in cur:
    print("按LEVEL由大到小之排序後結果:", doc)








