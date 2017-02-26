from globals import *
from answer import *
status = True
globals = Globals()
for context in globals.contexts:
    print context
print 'ready'
while status:
    input = raw_input()
    status,output = answer(input)
    print output