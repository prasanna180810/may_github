from datetime import datetime
name=input("enter your name")
lists='''
 RICE   RS20/KG
 SUGAR  RS/30KG
 OIL    RS/40KG
 PANNER RS/50KG
 BOOST  RS/80KG
 MAGGI  RS/50KG
 '''
## decleration
price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]

items={'RICE':20,'SUGAR':30,'OIL':40,'PANNER':50,'BOOST':80,'MAGGI':50}
option=int(input("FOR LIST OF ITEAMS PRESS 1:"))
if option==1:
    print(lists)

for i in range(len(items)):
 inp1=int(input("IF YOU WANT TO BUY PRESS 1 OR PRESS 2 TO EXIT:"))
 if inp1==2:
    break 
 if inp1==1:
    item=input("ENTER YOUR ITEMS:")
    quantity=int(input("ENTER YOUR QUANTITY:"))
    if item in items.keys():
     price=quantity*(items[item])
    pricelist.append((item,quantity,items,price))
    totalprice+=price
    ilist.append(item)
    qlist.append(quantity)
    plist.append(price)
    gst=(totalprice*5)//100
    finalamount=gst+totalprice
 else:
   print("sorry your entered iteam is not avaliable:")
else:
  print("you entered wrong number:")
inp=input("can i bill the items yes or no:")
if inp=='yes':
  pass
  if finalamount!=0:
   print(25*"=","kiran supermarket",25*"=")
   print(28*"=","kakinada")
   print("NAME:",name,30*" ","DATE:",datetime.now())
   print(75*"-")
   print("sno,8*"" ",'items',5*" ",'quantity',3*" ",'price')
   for i in range(len(pricelist)):
      print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*"",plist[i])   
      print(75*" ")
      print(50*" ",'Total amount:','RS',totalprice)
      print("gst amount",50*"","RS",gst)
      print(75*" ")
      print(50*" ",'Final amount','RS',finalamount)
      print(75*" ")
      print(50*" ","THANKS FOR VISITING")
      print(75*" ")

