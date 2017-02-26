from context import Context
from globals import *
from sentiment_analysis import *
def preprocess(input):
    if "n't" in input:
        input = " not ".join(input.split("n't"))
    input =  input.upper()

    return input

def get_context(input):
    context = Context()
    context.sentiment = get_sentiment(input)


def get_output(input):
    '''if input in dictionary:
        return dictionary[input]
    else:
        return dictionary['default']'''
    return ''

def answer(input):
    input = preprocess(input)
    context = get_context(input)
    output = get_output(input)
    return output['status'], output['msg']
globals = Globals()
for context in globals.contexts:
    print context