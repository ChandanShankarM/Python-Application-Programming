#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ex1:
    pass
print(type(ex1))


# In[5]:


class ex2:
    def f1():
        print("f1 in ex2")
ex2.f1()        


# In[6]:


class ex3:
    a='pap'
print(ex3.a)    


# In[8]:


a=ex1() #varialble, instance, object 
#the above line actually is:  ex1.__init__(a)
print(a,type(a))


# In[10]:


class ex4:
    def __init__():
        print("nothing")
        
a=ex4()        


# In[13]:


#so, we should use "self" or any name as an argument for init
class ex4:
    def __init__(self):
        print("this is actually a constructor")
        print(self)
        
a=ex4()
print(a)
#a and self are same


# In[17]:


class student:
    def __init__(self, name, srn):
        self.name=name
        self.srn=srn
        print("name:",name,"srn:",srn)

s=student("pap","pes120")        


# In[29]:


class student:
    count=0 #class variable, static variable
    #class variable is defined before the init. 
    def __init__(self, name, srn):
        self.name=name
        self.srn=srn
        student.count=student.count+1

s=student("pap","pes120")
print(s.count)
print(student.count)

s2=student("pap","pes120")
print(s2.count)


# In[32]:


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
emp1=employee("abc",70000)
print(emp1.salary)
#update object property
emp1.salary= 100000
print(emp1.salary)


# In[3]:


#dynamic creation of attributes
class employee:
    pass
e1=employee()
setattr(e1,'sal',120000)
print(e1.sal)


# In[5]:


e2=employee()
setattr(e2,'age',12)
print(e2.age)
print(e2.sal)


# In[7]:


#getattr
class employee:
    age=23
    name='abc'
e1=employee()
print("age:",getattr(e1,'age'))


# In[8]:


#getattr can have a default value in case the mentioned attribute is not found, here male is default
print("gender:",getattr(e1,'gender','male'))


# In[11]:


#
class myclass:
    __num=10  # this is a private variable(double underscore), has some protection
    def add(self,a):
        sum=a + self.__num
        print(sum)
        
obj= myclass()
obj.add(20)
print(obj.__num) #cant be accesed becoz it is private   


# In[12]:


#dir gives the name of all functions associted with the class
print(dir(myclass))


# In[14]:


#function overloading
def sum(a,b):
    print(a+b)
def sum(a,b,c):
    print(a,b,c)
sum(1,2)        


# In[17]:


# single level inheritance
class operation:
    a=10
    b=20
    def add_func(self):
        sum=self.a + self.b
        print("sum",sum)
        
class req_class(operation):
    def sub_func(self):
        sub=self.a - self.b
        print(sub)
        
obj=req_class()
obj.add_func()
obj.sub_func()


# In[ ]:


#multi level inheritence
A()
B(A)
C(B)

#multiple inheritance
A()
B()
C(A,B)


# In[23]:


#function over riding
class A:
    def hello_pap(self):
        print("in b2 pap class")
class B(A):
    def hello_pap(self):
        print("still in b2 pap class only")
obj= B()
obj.hello_pap()


# In[4]:


#is a 
#has a (composition)

class MyDate:
    def __init__(self,dd,mm,yy):
        self.dd=dd
        self.mm=mm
        self.yy=yy
    def __str__(self):
        return str(self.dd)+"-"+str(self.mm)+"-"+ str(self.yy) #this is used to return the date in a particular order
    def convert_days(self):
        return self.yy*365 + self.mm*30 + self.dd
    
d=MyDate(15,8,1947)    

print(d)
#here __str__ is executed by default
print(d.convert_days())


# In[5]:


class MyEvent:
    def __init__(self,dd,mm,yy,event_details):
        self.date= MyDate(dd,mm,yy)
        self.event_details = event_details
    def __str__(self):
        return str(self.date) + "----->"+ self.event_details
    
e=MyEvent(15,8,1947,"I day")
print(e)


# In[1]:


l= [1,2,3,4] # this ia an iterable list
for i in l:
    print(i)
    
dir(l)   
#iteration thru l is possible becoz it is instatioated with a function called __iter__


# In[2]:


next(l)


# In[3]:


l=iter(l)
next(l)


# In[4]:


next(l)
# list is iterable but 'for' is the iterator


# In[5]:


next(l)


# In[6]:


next(l)


# In[7]:


next(l)# stop iteration is raised


# In[13]:


dir(l)
#this has the 'next' function


# In[14]:


range(10)


# In[15]:


#python is a lazy evaluator, so...
list(range(10))


# In[16]:


#creating our own iterator
#creating our own 'range' function,  any iterator should include iter and next
class act_range:
    def __init__(self,n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration
            
print(list(act_range(10)))            


# In[ ]:





# In[17]:


#generators
#these are easier and smaller than vreating itertors
# function containing 'yield' is called a generator
#yield pauses and remembers its previous state but return terminates the program
def my_gen():
    n=1
    print("its one")
    yield n
    
    n=n+1
    print('its two')
    yield n
    
    n=n+1
    print('its three')
    yield n
    
a= my_gen()
print(next(a))


# In[13]:


print(next(a))


# In[14]:


print(next(a))


# In[15]:


print(next(a))


# In[19]:


#instead of using next(), we can use 'for' since a is an iterable

a= my_gen()
for i in a:
    print(i)


# In[28]:


def primeno(n):
    for i in range(2,n+1):
        c=0
        for j in range(2,i):
            if (i % j) == 0:
                c=1
                break
        if (c==0):
            yield i

p=primeno(11)
for i in p:
    print(i)
            
        


# In[27]:





# In[ ]:


#design pattern
#3 types: creational, Structural, Behavioral


# In[34]:


#Facade -> structural -> abstraction
class cpu:
    def process(self):
        print("processing")
        
class memory:
    def io_ops(self):
        print("memory")
        
class harddrive:
    def read(self):
        print("do read ops")
        
#facade
class computer_facade:
    def __init__(self):
        self.cpu= cpu()
        self.mem= memory()
        self.hdd= harddrive()
    def bootup(self):
        self.cpu.process()
        self.mem.io_ops()
        self.hdd.read()

comp= computer_facade()
comp.bootup()


# In[35]:


class forward:
    def acceleration(self):
        print("accelerating")
        
class stop:
    def breaking(self):
        print("stopping")
        
class gear:
    def shift_gear(self):
        print("changing gear")
        
#facade
class car_facade:
    def __init__(self):
        self.forward= forward()
        self.stop= stop()
        self.gear= gear()
    def start(self):
        self.forward.acceleration()
        self.stop.breaking()
        self.gear.shift_gear()

car1= car_facade()
car1.start()


# In[ ]:





# In[9]:


#singleton class
#1 object(single)

class single:
    instance=None
    def getinstance():
        if single.instance==None:
            single()
        return single.instance
    def __init__(self):
        if single.instance!=None:
            raise Exception("hey this is singleton")
        else:
            single.instance=self
            
s1= single()
print(s1)


# In[5]:


#now, if a second instance is created, we raise the given exeption
s2=single()
print(s2)


# In[11]:


#observer

#subset of PUBlisher/ SUBscriber
#subject ----- dependents(list) ------ observers

#publisher: register, un-register, notify

#subscriber:

#event: not, avail


# In[22]:


class publisher:           #god class
    def __init__(self):
        pass
    def register(self):
        pass
    def unregister(self):
        pass
    def notifyall(self):
        pass
    
class Techforum(publisher):
    def __init__(self):
        self.listofusers=[]
        self.postname=None
    def register(self,userobj):
        if userobj not in self.listofusers:
            self.listofusers.append(userobj)
    def unregister(self,userobj):
        self.userobj.remove(userobj)
    def notifyall(self):
        for objects in self.listofusers:
            objects.notify(self.postname)
    def writepost(self,postname):
        self.postname=postname
        self.notifyall()
        
class subscriber:
    def __init__(self):
        pass
    def notify(self):
        pass
    
class user1(subscriber):
    def notify(self,postname):
        print("user is notifies with new post: ",postname)
        

if __name__=="__main__":
    techforum=Techforum()
    usr1= user1()
    techforum.register(usr1)
    techforum.writepost("hello, you are notified")


# In[23]:


class user2(subscriber):
    def notify(self,postname):
        print("user is notifies with new post: ",postname)
usr2= user2()
techforum.register(usr2)
techforum.writepost("hello, you are notified")

