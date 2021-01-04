
from translate import Translator

with open('text.txt') as txt:
    read  = txt.read()
    y = Translator(to_lang='ro').translate(read)
    with open('trans.txt','w') as trans:
        trans.write(y)