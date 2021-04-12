import re

def firstAndlast(Z):
    s=re.findall("[a-z0-9A-Z*\s]",Z)
    for i in s:
        p1=s[0]
        p2=i[0] 
    return p1+p2   
 
na=input("enter your name:")
s=firstAndlast(na)

add=input("enter your address:")
t=firstAndlast(add)

fac=input("enter your faculty:")
v=firstAndlast(fac)


site=input("enter the site you want to open:")
w=firstAndlast(site).upper()

code=str(000)

uid=input("enter your username :")
for id in uid:
    rev=re.findall("[a-zA-Z0-9*\s]",uid)
    l=len(rev)
    x=s1=rev[l-2]+rev[l-1] 
        

with open("files.txt", "a+", encoding="utf-8") as f:
    f.write(na+ "                         "+add+"                       "+fac+"                            "+code+"\n")
    f.seek(0)
    pr=f.read()
     
print(code+s+t+v+w+x)
    

    
   