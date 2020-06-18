from pymongo import MongoClient

# 파이썬은 클래스 위에 2줄을 띄우는게 국룰임
class MongoDAO: ### DB에 저장할 때 순서는 1. 클래스생성, 2.객체생성, 3.DB에 집어넣고, 4.
    reply_list = [] # MongoDM Document를 담을 List 선언

    def __init__(self):
        # >> MongoDB Connection
        self.client = MongoClient('127.0.0.1', 27017) # 클래스 객체 할당(ip, Port)
        self.db = self.client['local'] # MongoDB의 'local' DB를 할당
        self.collection = self.db.get_collection('movie') # 동적으로 Collection 선택

    # MongoDB에 Insert
    def mongo_write(self, data):
        print('>> MongoDB WRITE DATA:)')
        self.collection.insert(data) # JSON Type = dict Type(Python - > [key:value])
        
    # MongoDB에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0, 'content':1, 'score':1}):
            self.reply_list.append([one['title'], one['content'], one['score']]) # dict에서 Value와 Score만 추출
        return self.reply_list