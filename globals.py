import datetime
from pymongo import MongoClient
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

class DB:
    __metaclass__ = Singleton
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.JARVIS

class Globals:
    __metaclass__ = Singleton
    def __init__(self):
        self.user = "Dhruv"
        self.hour = int(str(datetime.datetime.now().time())[:2])
        self.name = "JARVIS"
        print 'init'
        self.contexts = list(DB().db.conversation.find({}))




