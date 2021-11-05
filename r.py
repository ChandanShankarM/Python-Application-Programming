'''
import re 
txt=sstduid dsdfdied dgsgksmdf
    dfgjkldhdod@hdhjodj
    duidodhgduidi@gdd
    478689576667@
    sd
    sgdpodiodi

p = re.compile('\C') 
print(p.findall(txt))

import re


pat="is"
txt="is this is PAP.its a Special Topic"
print(re.search(pat,txt))
print(re.findall(pat,txt))
print(re.finditer(pat,txt))
print(re.match(pat,txt))    #only matches to beginning
print(re.fullmatch(pat,txt))

import re
txt=this 
is special 
topic 
@ 2.30 hr this
r1=re.findall("^\w|@",txt,flags=re.MULTILINE)
print(r1)

import re
txt=once upon a time,
there lived a king
print(re.findall(".+",txt))
print(re.findall(".+",txt,re.DOTALL))

import re
address=re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')
candidates=['chan2000@gmail.com','123@pes.edu','special_topic@special.foo']
for i in candidates:
    match=address.search(i)
    print(match)

import re
address=re.compile(
[\w\d.+-]+ #username
@
([\w\d.]+\.)+ #prefix
(com|prg|edu) #top domain
,
re.VERBOSE)
candidates=['chan2000@gmail.com','123@pes.edu','special_topic@special.foo']
for i in candidates:
    match=address.search(i)
    print(match)
'''
import re
txt='this is some text along with dots... and punctuations.'
pat='(?i)\\bT\w+'   #re,mul+re.i ()-group |re.group
#print(re.search(pat,txt))
reg= re.compile(pat)
x=reg.findall(txt)
print(txt)
print(pat)
print(x)






