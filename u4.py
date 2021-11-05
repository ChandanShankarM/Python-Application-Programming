'''DATABASE PROGRAMMING'''
#SQLite
#Sqlalchemy

#Introduction to SQLite:
#Comparsion not possible w.r.t the client server architecture
#MySQL,Postgres SQL,oracle:scalability -don't compare

#local data storage,
#low price,efficient,reliable,simple,independent

#when to use sqlite?
#when not to use sqlite?easy
#Any client server applications
#during website construction(to many writes need to synchronize leads to complex)(high volume website)
#Huge dataset(140 TB)
#High concurrency

#Library,serverless,zero configuration

#API's
#Connect : :memory: disk,RAM,(create)
#cursor  : use further transcations of database
#execute : use to execute an sql statement (insert,delete)("select * from DB")
#commit  : is to commit the current transcation(DB -- Table-- insert values has to commit)
#rollback: rollback till last commit
#close

import sqlite3

'''
cxn=sqlite3.connect("shan.db") #used for different transcations
#print(cxn)

cur=cxn.cursor()
#print(cur)

#cur.execute('create table tab1(name char(20),age integer)')    makesure commented this
cur.execute('insert into tab1 values("Chandan",19)')#Operational error already tab1 is there
cur.execute('insert into tab1 values("Chandanshankar",29)')
cur.execute('insert into tab1 values("Chandanshankar m",39)')
#Insert using Place holders
info=("CSM",18)
cur.execute('insert into tab1 (name,age) values (?,?)',info) 
x=cxn.execute('select * from tab1')
for i in x:
    print(i)
'''

'''
con=sqlite3.connect(":memory:") #DB onto the RAM
cur=con.cursor()
cur.execute('create table people(firstname char(20),lastname char(20),age integer)')
info=("Chan","Shan",18)
info1=("Chandan","Shankar",28)
cur.execute('insert into people (firstname,lastname,age) values (?,?,?)',info) 
cur.execute('insert into people (firstname,lastname,age) values (?,?,?)',info1)
x=con.execute('select * from people')
for i in x:
    print(i)
'''

#fetchall()
#fetchone()
#fetchmany()
#primary, Foreign key:
'''
con=sqlite3.connect("ex1.db")
cur=con.cursor()
#con.execute('create table supplier_groups(group_id integer PRIMARY KEY,group_name text NOT NULL)')
#con.execute('create table supplier(sup_id integer PRIMARY KEY,supplier_name text NOT NULL,group_id integer NOT NULL, FOREIGN KEY(group_id) references supplier_groups(group_id))')

con.execute("insert into supplier_groups values(8,'chan')")
#con.execute("insert into supplier_groups values(8,'chan')")    IntegrityError:UNIQUE constraint failed
con.execute("insert into supplier_groups values(81,'shan')")
con.execute("insert into supplier_groups values(18,'chandan')")
query='select * from supplier_groups'
x=con.execute(query)

for i in x:
    print(i)

#z=x.fetchone() # return single record if nothing returns None
#print(z)
#a=x.fetchall() # gives all the records
#print(a)
#b=x.fetchmany(3) #fetchmany([arguments][size]) # default single record
#print(b)
'''
'''
#hospital-hospital id(P),name,bed _count.
#doctor tab - doc_id(P),doc_name,hospital id(F),joining_date,salary,experience,speciality. 
con=sqlite3.connect("hos.db")
cur=con.cursor()
#con.execute('create table hospital(hospital_id integer PRIMARY KEY,hospital_name text NOT NULL,bed_count integer)')
#con.execute('create table doctor(doc_id integer PRIMARY KEY,doc_name text NOT NULL,joining_date integer,sal integer,exp integer,speciality text,hospital_id integer NOT NULL, FOREIGN KEY(hospital_id) references hospital(hospital_id))')
#con.execute("insert into hospital values(8,'chan',20)")
#con.execute("insert into hospital values(81,'chand',20)")
#con.execute("insert into hospital values(18,'chandan',20)")
con.execute("insert into doctor values(181,'chandfg',12032020,10000,3,'rad',8)")
con.execute("insert into doctor values(821,'shandar',12132020,100000,13,'pedeatrision',18)")
q2=cur.execute('select * from doctor where sal=(select max(sal) from doctor)')
print(q2.fetchall())
q1=cur.execute('select * from hospital , doctor where doctor.hospital_id == hospital.hospital_id')
print(q1.fetchall())
q3=cur.execute('select * from doctor')
print(q3.fetchall())
'''
#sqlite: connection , cursor
#python : objects non scalar types
#table : student: values: int,float,str -primitive data types
#everything w.r.t python-class: table,row,columns
#sqlalchemy-converting nonscalar to scalar type
#class table:
#sqlalchemy:ORM:Object relational mapper(python): classes gets mapped to the databases
#python     ORM         application
#table, row, column: MetaData()-contains all different data to create TRC
#connection
#create_engine:DBAPI(dialect(DB))-sqlite,mysql

from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

'''
engine=create_engine('sqlite:///university db',echo=True)
meta=MetaData()
students=Table('students',meta,Column('id',Integer,primary_key=True),Column('firstname',String))                          

#meta.create_all(engine)

#ins=students.insert().values(id=12,firstname='chandan')
con=engine.connect()
#con.execute(students.insert(),[{'id':13,'firstname':'shan'},{'id':16,'firstname':'kri'}])
#s1=students.select()
#res=con.execute(s1)
#for i in res:
    #print(i)
s1=students.update().where(students.c.firstname=='chandan').values(firstname='SHAN')        
con.execute(s1)

s2=students.select()
print(con.execute(s2).fetchall())

s3=students.alter().where(students.c.firstname=='shan').values(firstname='SHAN')        
con.execute(s1)

s4=students.select()
print(con.execute(s4).fetchall())

s5=students.delete().where(students.c.firstname=='SHAN')
con.execute(s5)
s6=students.select()
print(con.execute(s6).fetchall())
'''

engine=create_engine('sqlite:///university db',echo=True)
meta=MetaData()
students=Table('students',meta,Column('id',Integer,primary_key=True),Column('firstname',String))                          

exam_sect=Table('exam_sect',meta,
Column('id',Integer,primary_key=True),
Column('st_id',Integer,ForeignKey('students.id')),
Column('marks',Integer))
meta.create_all(engine)
con=engine.connect()
#con.execute(exam_sect.insert(),[{'id':13,'st_id':'40','marks':100},{'id':16,'st_id':'20','marks':99}])
s1=exam_sect.select()
print(con.execute(s1).fetchall())
s1=exam_sect.select().with_only_columns([exam_sect.c.st_id]).where(exam_sect.c.marks < 100)
print(con.execute(s1).fetchall())

lib=Table('lib',meta,
Column('id',Integer,primary_key=True),
Column('lib_id',Integer,ForeignKey('students.id')),
Column('isbn',Integer),
Column('bookname',String))
meta.create_all(engine)
con=engine.connect()
#con.execute(lib.insert(),[{'id':13,'isbn':'4023','bookname':'carl hamacher'},{'id':16,'isbn':'2000','bookname':'ramana'}])

s4=lib.select().with_only_columns([lib.c.id]).where(lib.c.bookname=='ramana')
print(con.execute(s4).fetchall())

