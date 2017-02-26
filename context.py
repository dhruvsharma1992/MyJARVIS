class Context:
    def __init__(self):
        self.sentiment = None
        self.sentence_type = None #interrogative = 0, imperative = 1, declarative = 2
        self.action = None
        self.message = None
        self.tense = None  #present:0, past:1, future:2
        self.keywords = []
        self.specific_context = None

    def toDict(self):

        d = dict()
        d['sentiment'] = self.sentiment if self.sentiment else 0
        d['sentence_type'] = self.sentence_type
        d['action'] = self.action if self.action else 'text'
        d['message'] = self.message if self.message else 'Sorry. I did not understand that'
        d['tense'] = self.tense if self.tense else 0
        d['keywords'] = self.keywords
        d['specific_context'] = self.specific_context
        return d