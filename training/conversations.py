#import pymongo
from pymongo import MongoClient
from context import Context
#client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.JARVIS

while True:
    print 'User: ',
    input1 = raw_input().upper()
    print 'build context'

    context = Context()
    print 'Sentiment: ',
    context.sentiment = int(raw_input())

    print 'Sentence Type: ',
    context.sentence_type = int(raw_input())

    print 'Action: ',
    context.action = raw_input()

    print 'message: ',
    context.message = raw_input()

    print 'Tense:',
    context.tense = int(raw_input())


    if not db.conversation.find_one({'input':input1}):
        db.conversation.insert({
            'context': context.toDict(),
            "reply": context.message,
            'input':input1
        })