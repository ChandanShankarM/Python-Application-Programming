#process,Thread
#why
#create threads in python
#work with threads
#examples
#pc, ps reg,pcode
'''Thread'''
#Thread is a subset of the process
#share datasegment,code segment files
#own set of register,stack,pc

#create threads

import threading
'''
def f1(num1,num2):
    print(num1+num2)
def f2(num1,num2):
    print(num1*num2)


t1=threading.Thread(target=f1,args=(5,9))
t2=threading.Thread(target=f2,args=(5,10))
t1.start()
t2.start() #main thread --- t1
t2.join()
t1.join()
'''
import os
'''
def f1():
    print(threading.current_thread().name)
    
def f2():
    print(threading.current_thread().name)
    
if __name__=="__main__":
    print("main program ID",os.getpid())
    t1=threading.Thread(target=f1,name='t1')
    t2=threading.Thread(target=f2,name='t2')
    print("main thread name is",threading.main_thread().name)
    t1.start()
    t2.start()
    t2.join()
    t1.join()
'''

import time
'''
def i_am_thread():
    time.sleep(0.000001)
    print("this is some thread")
    
t1=threading.Thread(target=i_am_thread,name="i am t1")
t1.start()
print("state",t1.is_alive())
print("count of threads",threading.active_count())
print("state",t1.is_alive())
t1.join()


x=20
def f1():
    global x
    x+=1
    print(x)
f1()

def f1(num1,num2):
    print(num1+num2)

t1=threading.Thread(target=f1,args=(5,9))
t2=threading.Thread(target=f1,args=(5,10))
t1.start()
t2.start() 
t2.join()
t1.join()

#Race Condition solution:- Synchronization-lock()--semaphores-0 to 1(acquire(blocking and nonblocking) and release) and mutex
x=0
def increment_global():
    global x
    x+=1
    
def task():
    for i in range(270000):
        increment_global()

def main():
    global x 
    x = 0
    t1 = threading.Thread(target=task) 
    t2 = threading.Thread(target=task) 
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main() 
        print(i,x) 

x=0
def increment_global():
    global x
    x+=1
    
def task():
    for i in range(270000):
        lock.acquire() 
        increment_global() 
        lock.release() 

def main():
    global x 
    x = 0
    t1 = threading.Thread(target=task) 
    t2 = threading.Thread(target=task) 
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main() 
        print(i,x)

def cap():
    res = "" 
    for i in range(65, 65 + 2): 
       res = res + chr(i) +chr(i)  
       print(str(res))
       res=""
    
def sma():
    res1 = "" 
    for i in range(97, 97 + 2): 
       res1 = res1 + chr(i) +chr(i)  
       print(str(res1))
       res1=""
cap()
sma()
'''

import sys
import random
'''
Lock=threading.Lock()
def f1():
    s='ABCD'
    for i in range(0,len(s)):
        Lock.acquire()
        print(s[i],end='',flush=True)
        time.sleep(int(random.random()*3))
        print(s[i],end='',flush=True)
        Lock.release()
        time.sleep(int(random.random()*3))
        
def f2():
    s='abcd'
    for i in range(0,len(s)):
        Lock.acquire()
        print(ord(s[i]),end='',flush=True)
        time.sleep(int(random.random()*3))
        print(ord(s[i]),end='',flush=True)
        Lock.release()
        time.sleep(int(random.random()*3))

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
t1.start()
t2.start() 
t2.join()
t1.join()


for i in range(10):
    print(i,end=' ',flush=True)
    #sys.stdout.flush()
    time.sleep(1)
'''
#Semaphores
#Bounded Semaphore
#producer consumer problem
#Lock() - acquire release
#sema - acquire()-decrement release()-increment
#types-binary and counting
'''
se=threading.Semaphore()

def f1():
    print("f1 is starting")
    se.acquire()
    for i in range(20,30):
        print("f1 is working in loop",i)
        time.sleep(1)
    se.release()
    print("f1 completed its work")

def f2():
    print("f2 started working")
    while not se.acquire(blocking=False):
        print("f2 is waiting for semaphore")
        time.sleep(1)
    else:
        print("some values")
        for i in range(20,24):
            print("f2 working in loop too",i)
            time.sleep(1)
    se.release()


t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
t2.start()
t1.start() 
t2.join()
t1.join()
print("DONE")

s1=Semaphore(6) #allow 6 threads
s1.acquire()
print(s1._value)
s1.acquire()
print(s1._value)
s1.acquire()
print(s1._value)
s1.release()
print(s1._value)
s1.release()
print(s1._value)
s1.release()
print(s1._value)
s1.release()
print(s1._value)
print("\n")


s2=BoundedSemaphore(6) #allow 6 threads
s2.acquire()
print(s2._value)
s2.acquire()
print(s2._value)
s2.acquire()
print(s2._value)
s2.release()
print(s2._value)
s2.release()
print(s2._value)
s2.release()
print(s2._value)
s2.release()
print(s2._value)
s2.release()
print(s2._value)
'''

#producer consumer problem
#buffer-list(or queue)
#buggy code
'''
buffer=[]
lock=Lock()
class Producer(Thread):
    def run(self):
        nums=range(5)
        global buffer
        while True:
            num=random.choice(nums)
            lock.acquire()
            buffer.append(num)
            print("producer produced a num",num)
            lock.release()
            time.sleep(random.random())

class consumer(Thread):
    def run(self):
        global buffer
        while True:
            lock.acquire()
            if not buffer:
                print("nothing in buffer")
            num=buffer.pop(0)
            print("consumer consumes the num",num)
            lock.release()
            time.sleep(random.random())

Producer().start()
consumer().start()
'''
#condition class - lock(acquire and release)
#make consumer to wait() until producer produces something or until it notify()
'''
condition=Condition()
buffer=[]
lock=Lock()
class Producer(Thread):
    def run(self):
        nums=range(5)
        global buffer
        while True:
            condition.acquire()
            num=random.choice(nums)
            buffer.append(num)
            print("producer produced a num",num)
            condition.notify()  #consumer wakes up at this point
            condition.release()
            time.sleep(random.random())

class consumer(Thread):
    def run(self):
        global buffer
        while True:
            condition.acquire()
            if not buffer:
                print("nothing in buffer")
                condition.wait()
                print("producer add something")
            num=buffer.pop(0)
            print("consumed",num)
            condition.release()
            time.sleep(random.random())

Producer().start()
consumer().start()
'''

#Multiprocessing - more than one processor
#difference b/w multiprocessing and parallel processing
#mp-single processor with multiple cores(time less)
#pp-single process gets split up and given to processor(each subtask goes to each core)
#create process(spawn)

import multiprocessing
'''
def square(x):
    print("square of a number is",x*x)
def cube(x):
    print("cube of a number is",x*x*x)

if __name__=="__main__":
    p1=multiprocessing.Process(target=square,args=(8,))
    p2=multiprocessing.Process(target=cube,args=(8,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('pid of p1: ', p1.pid)
    print('pid of p2: ', p2.pid)
    print("main program ID",os.getpid())
    print("----------------------------")
'''
#IPC-communicate with eachother in a more synchronized way
#independent
#co-operating:increases the computational speed
#Shared memory
#message passing


#SHARED MEMORY-PRODUCER AND CONSUMER
'''
result=[]

def square_list(mylist): 
    global result  
    for num in mylist: 
        result.append(num * num) 
    print("p1 process is printing the result",result) 
    time.sleep(1)

if __name__ == "__main__": 
    mylist = [1,2,3,4] 
    p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
    p1.start() 
    p1.join() 
    print("main process printing the result",result) 

#main-child(p1)
'''
'''
def square_list(mylist,result,square_sum):  
    for i,num in enumerate(mylist): 
        result[i]=num*num
        
    square_sum.value=sum(result[:])
    print("result in p1",result[:])
    print("sum of squares",square_sum.value)

if __name__ == "__main__": 
    mylist = [1,2,3,4]
    result=multiprocessing.Array('i',4)
    square_sum = multiprocessing.Value('i') 
    p1 = multiprocessing.Process(target=square_list, args=(mylist,result,square_sum)) 
    p1.start() 
    p1.join() 
    print("result in main program",result[:]) 
    print("Sum of squares",square_sum.value) 

[1,22,33,44,55,66]
p1,p2
or
t1,t2

search for an element:
p1 has to test in first half
p2 has to test in second half

result=[1,22,33,44,55]

def search(a):  
    for i in mylist[0:2]: 
        if(i==a):
            print("it's there") 
 
def search(a):  
    for i in mylist[3:5]: 
        if(i==a)
            print("p1 process is printing the result",result)    
'''
'''
def se(x):
    for i in range(int(n/2)):
        if(x==a[i]):
            print("found in 1")
            break;
    else:
        print("not found in 1");
def sea(x):
    for i in range(int(n/2),n):
        if(x==a[i]):
            print("found in 2")
            break;
    else:
        print("not found in 2")
if __name__ == "__main__":
    a=[]
    x= int(input("Enter element : "))
    n = int(input("Enter number of elements : "))
    for i in range(0, n): 
        ele = int(input()) 
        a.append(ele)
    p1 = multiprocessing.Process(target=se, args=(x,)) 
    p2 = multiprocessing.Process(target=sea, args=(x,)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''
import threading
lock=threading.Lock()
def f1():
    for i in range(e1,e2+1):
        lock.acquire() 
        if(i%2==0):
            print("even:",i)
        lock.release() 
def f2():
    for i in range(o1,o2):
        lock.acquire() 
        if(i%2!=0):
            print("odd:",i)
        lock.release()
def f3():
    for i in range(o1,e2+1):
        lock.acquire() 
        print("all:",i)
        lock.release()


if __name__ == "__main__":
    e1= int(input("Enter even from: "))
    e2= int(input("Enter even to: "))
    o1= int(input("Enter even from: "))
    o2= int(input("Enter even to: "))
    p1 = multiprocessing.Process(target=f1) 
    p2 = multiprocessing.Process(target=f2)
    p3 = multiprocessing.Process(target=f3)  
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()


#given a string find the first apperance of the substring not and bad if the bad follows the not replaces the whole not ... bad substring with the good return the result

import re

txt = "This movie is not that bad"
match = re.search('not.*bad', txt)
i = match.start()
j = match.end()
txt = txt[:i]+'good'+txt[j:]
print(txt)


pat=re.compile('^a\d*[13579]ab')
candidates=["a1353ab","a24ab"]
for i in candidates:
    match=pat.search(i)
    print(match)


pat=re.compile('^[aeiou].*',re.I)
string=["PAP","Application","Programming"]
for i in string:
    match=pat.search(i)
    print(match)


pat=re.compile('^[89]\d\d\d\d\d\d\d\d[123456789]$')
string=["8026377330"]
for i in string:
    match=pat.search(i)
    print(match)















