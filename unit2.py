#!/usr/bin/env python
# coding: utf-8

# In[1]:


#regular exp

'''
^ - beginnig of string
$ - ending of string
\d - 0-9
\D - negates \d
\w - word character (a-z, A-Z, 0-9,, _)
\W - negates \w
\s - white space(tab newline)
\S - negates \s
\b - word boundry
\B - not a word boundry

character sets

[] - matches the characters in the bracket 
[^ ] - matches the characters not in the bracket
[1 - 5] - gives range. range can also have alphabets like a-z, A-Z, etc

quantifiers

. - matches everything except a new line(\n)
* - matches the characters in the brackets, 0 or more
+ - 1 or more
? - 0 or 1
{3} - exact numbers
{3,3} - range of numbers

'''


# In[2]:


import re  #regular expression
text='''
200-1234
300.1234

varun
karun 
tarun
parun
'''

pattern= re.compile(r'[23]00[.-]\d\d\d\d')
matches= pattern.finditer(text)
for match in matches:
    print(match)


# In[3]:


pattern= re.compile(r'[a-z]arun')
matches= pattern.finditer(text)
for match in matches:
    print(match)


# In[4]:


pattern= re.compile(r'[^p]arun')
matches= pattern.finditer(text)
for match in matches:
    print(match)


# In[ ]:





# In[7]:


#search()- find the given patterrn in the text. search(pattern, text)
#returns none if there is no match
import re
pat="this is"
text="this is pap sp topic"
match= re.search(pat,text)

s=match.start()# records starting point of the span
e=match.end()

print(match.re.pattern, match.string,s,e)
#span below says where the match starts and ends in the string


# In[ ]:


#search() takes 3rd parameters that are flags
#can add many flags with + sign
"""
re.I or re.IGNORECASE - ignore case
"""
match= re.search(pat,text,re.I)


# In[21]:


program_list= ["Python", "PHP", "C++"]
pat= "^p.*p$"
for program in program_list:
    if re.search(pat, program,re.I):
        print("found")
    else:
        print("not found")


# In[22]:


#compiling and storing the reg exp that is used many times will save extra processing. we can use the compiled, saved in cache data
import re
regex= [re.compile(p) for p in ["this", "that"]]
text= "does this text match the pattern"
for reg in regex:
    if reg.search(text):
        print("match")
    else:
        print("no match")


# In[29]:


#search returns only the first occurence of the pattern, findall gives all (returns the word)
text=" this is pap. this is st"
pat = "this"
for match in re.findall(pat, text):
    print(match)


# In[32]:


text="ababbbbbbabab"
pat="ab"
for match in re.finditer(pat,text):
    s=match.start()
    e=match.end()
    print(text[s:e],s,e)


# In[ ]:





# In[2]:


#match should have pat at the beginning only
import re
pat="is"
txt="is this is pap."
x=re.match(pat,txt)
print(x)


# In[3]:


txt="this is pap."
x=re.match(pat,txt)
print(x)


# In[6]:


#search will return only the first occurence
y=re.search(pat,txt)
print(y)


# In[8]:


#for fullmatch, both pat and txt should be same
z=re.fullmatch(pat,txt)
print(z)


# In[23]:


txt="""this
is special
topic
@2.30 hr"""
r1= re.findall("^\w",txt) #findall will process only till newline char
print(r1)


# In[24]:


#flag: multiline
r1= re.findall("^[\w]",txt,flags=re.MULTILINE)
print(r1)


# In[25]:


r1= re.findall("^\w*",txt,flags=re.MULTILINE)
print(r1)


# In[21]:


# . matches everything except a new line(\n)

txt= """once upon a time,
there lived a king"""
r1=re.findall(".+",txt)
print(r1)


# In[22]:


r1=re.findall(".+",txt,flags=re.DOTALL)
print(r1)


# In[ ]:





# In[26]:


address= re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')
candidates=['nag-hem@gmail.com', '123@pes.edu','spec-top@spec.foo']
for i in candidates:
    match=address.search(i)
    print(match)


# In[27]:


#adding commenting to compile
address=re.compile(
"""[\w\d.+-]+ #username
@
([\w\w.]+\.)+ #prefix
(com|org|edu) #tD""", re.VERBOSE)
for i in candidates:
    match=address.search(i)
    print(match)


# In[32]:


txt='this is some text with dots...'
pat='(?i)\\bT\w+'
reg=re.compile(pat)
x=reg.findall(txt)
print(txt)
print(pat)
print(x)


# In[ ]:




