'''
1. train Pnr  
2. login
3.source  -destination
4.seats availability
5.price
6.user details  - name etc....
'''
s="""
1. user Name 
2. source and destination
3. train number and seat availability
4. price
5.pnr generate
6.user details
"""
trains ={("kakinada","hyd") : {"godavari":234,"tirupati":345,"vijayawada":344},
         ("vijayawada","hyd"):{"vishaka":123,"amaravathi":567,}}
seats1={"kakinada":200}
seat2={"vijayawada":300}
seat3={"hyd":400}
price1=(400)
price2=(500)
price3=(600)
users = {"prasanna":123,"ravi":345}
user_details = []
user_pin=(2222)
user=input("enter the user name:")
if user in users.keys():
    password=int(input("enter the password:"))
    if password == users[user]:
        print(s)
        option = int(input("enter your option: "))
        if option == 1:
            mobile = int(input("enter your mobile number:"))
            age = int(input("enter your age:"))
            gender=input("enter your gender:")
            l = [user, mobile, age, gender]  
            user_details.append(l) 
        elif option == 2:
            source = input("enter your source:")
            destination=input("enter your destination:")
            print("Available train : \n")
            if (source, destination) in trains:
                print(trains[(source, destination)])
            else:
                print("No trains avalible:")
        elif option==3:
            train=input("enter train name:")
            if train=="kakinada":
                print(seats1)
            elif train=="vijayawada":
                print(seat2)
            else:
                print(seat3)
        elif option ==4:
            name=input("enter train name:")
            if name=="kakinada":
                print(price1)
            elif name=="vijayawada":
                print(price2)
            else:
                print(price3)
        elif option==5:
            pnr=input("Enter your train name:")
            if pnr=="kakinada":
                print(67899)
            elif pnr=="vijayawada":
                print(78787)
            elif pnr=="hyd":
                print(87587)
            else:
                print("enter valid train name:")
        elif option==6:
         pin=input("Enter user pin  details:")
         if pin==user_pin:
             print(users)
         else:
             print("valid user name:")
            
    else:
        print("Invalid password")
else:
    print("Invalid username")
