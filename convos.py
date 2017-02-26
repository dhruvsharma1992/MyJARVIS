from globals import *
dictionary = {
    'hi jarvis':{
        'status': True,
        'msg': 'Hi ' + user
    },
    'hey jarvis':{
            'status': True,
            'msg': 'Hi ' + user
    },

    'bye':{
        'status': False,
        'msg': 'Bye.. Good Evening' if hour > 12 else 'Have a great day'
    },
    'bye jarvis':{
            'status': False,
            'msg': 'Bye.. Good Evening' if hour > 12 else 'Have a great day'
    },
    'how are you':{
            'status': True,
            'msg': 'I am good, how are you?'
    },
    'default':{
        'status':True,
        'msg':'Sorry I did not understand what you said'
    }
}