import sqlite3
from colorama import Fore
#database construction
db=sqlite3.connect("d:\programming\lala.db")
cr=db.cursor()
#saving and closiing database
def sc():
       db.commit()
       db.close()
#variables
note=str
note="choose: either to add (a), delete(d), modifiy(m), quite(q) or show(s)  your option:"
user=input(note).strip().lower()
#define methods
def a():
    print(Fore.BLUE, "Adding in process")
    name=input("enter user name:").strip().capitalize()
    age=int(input("enter user age:"))
    cr.execute(f"insert into users (name, age) values('{name}', {age}) ")
    #end
    print(f"user name is {name} user age is {age} ")
    print(f"thanks for adding user {name}")
    sc()
def d():
    print("deleting in process")
    delete_user=input("enter name :").strip().capitalize()
    age=int(input("user age:"))
    cr.execute(f"delete from users where name='{delete_user}' and age={age}")
    sc()
def m():
    print("modifying in process")
    add_user=input("enter name :").strip().capitalize()
    age=int(input("user age:"))
    cr.execute(f"update users set name='{add_user}' where age={age}")
    sc()
def s():
    print("showing items in process")
    cr.execute("select*from users")
    users=cr.fetchall()
    print(f"you have {len(users)} users")
    for row in users:
           print(f"user name is :{row[1]} , age:{row[0]}")

    sc()
def q():
    print("quit app")
    sc()

#options
options=["s","a","d","q","m"]
if user in options:
    print(f"hello your option is{user} ")
    if user=="a":
               a()
    elif user=="s":
               s()
    elif user=="m":
                m()
    elif user=="d":
               d()
    else :
               q()
else:
    print(f"{user} doesn't belong to available options")