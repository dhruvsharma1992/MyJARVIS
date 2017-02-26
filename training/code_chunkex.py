# Natural Language Toolkit: code_chunkex
#import nltk
from nltk import pos_tag, RegexpParser
sentence = pos_tag("Who is the prime minister of india".split(" "))
grammar = r"""
   NP: {<DT>?<JJ>*<NN>}
   {<DT|PP\$>?<JJ>*<NN>}
        {<NNP>+}
        {<NN>+}
      """
cp = RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()