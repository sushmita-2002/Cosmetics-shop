import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='kvr',database='cosmetics_shop')
mcur=mydb.cursor()

def insert():
    l=[]
    id=int(input('cosmetics id no.:'))
    l.append(id)
    nm=input('cosmetics name:')
    l.append(nm)
    com=input('cosmetics company:')
    l.append(com)
    cost=int(input('cosmetics cost:'))
    l.append(cost)
    lst=(l)
    sql='insert into mycosmetic(code,name,company,cost) values(%s,%s,%s,%s)'
    mcur.execute(sql,lst)
    mydb.commit()

def view():
   print("Select the search criteria : ")
   print("1. Customer ID  ")
   print("2. Customer Name")
   print("3. All")
   ch=int(input("Enter the choice : "))
   if ch==1:
       s=input("Enter id: ")
       rl=(s,)
       sql="select * from mycosmetic where code=%s"
       mcur.execute(sql,rl)
       res=mcur.fetchall()
       for i in res:
            print(i)
   elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from mycosmetic where name=%s"
        mcur.execute(sql,rl)
        res=mcur.fetchall()
        for i in res:
            print(i)
   else:
        sql="select * from mycosmetic"
        mcur.execute(sql)
        res=mcur.fetchall()
        for i in res:
            print(i)
            
def remove():
    n=input("Enter id to be deleted : ")
    rl=(n,)
    sql='delete from mycosmetic where code=%s'
    mcur.execute(sql,rl)
    mydb.commit()
    
def update():
    print('1. to update name')
    print('2. to update company')
    print('3. to update cost')
    a=int(input('enter id :'))
    li=int(input('enter one of the above :'))
    if li==1:
        b=input('enter name:')
        rl=(a,b)
        sql='update mycosmetic set name=%s where code=%s'
        mcur.execute(sql,rl)
        mcur.commit()
    elif li==2:
       b=input('enter company:')
       rl=(a,b)
       sql='update mycosmetic set com=%s where code=%s'
       mcur.execute(sql,rl)
       mcur.commit() 
    else:
        b=input('enter cost:')
        rl=(a,b)
        sql='update mycosmetic set cost=%s where code=%s'
        mcur.execute(sql,rl)
        mydb.commit()

def menu():
    print('1. to add cosmetic')
    print('2. to view cosmetic')    
    print('3. to delete cosmetic')
    print('4. to update cosmetic')
    pre=int(input('enter your choice :'))
    if pre==1:
        insert()
    elif pre==2:
        view()
    elif pre==3:
        remove()
    elif pre==4:
        update()
    else:
        print('invalid choice..')

menu()
