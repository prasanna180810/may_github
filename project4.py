print("=" * 20)
print("       state BANK SYSTEM       ")
print("=" * 20)

customerNames = ['Ravi Kumar', 'Sneha Reddy', 'Arjun Mehta', 'Priya Sharma', 'Kiran Das']
customerPins = ['1111', '2222', '3333', '4444', '5555']
customerBalances = [15000, 25000, 18000, 30000, 12000]
counter_1 = 1
counter_2 = 5
i = 0

while True:
    print("\n=====================================")
    print(" ---- Welcome to Times Bank ----      ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")

    choiceNumber = input("Select your choice number : ")

    # ------------------- Open New Account -------------------
    if choiceNumber == "1":
        print("\nChoice number 1 is selected")
        NOC = int(input("Number of Customers to add : "))
        i = i + NOC

        if i > 5:
            print("\nCustomer registration limit exceeded!")
            i = i - NOC
        else:
            while counter_1 <= i:
                name = input("Enter Full Name : ")
                customerNames.append(name)
                pin = input("Set a 4-digit PIN : ")
                customerPins.append(pin)

                balance = int(input("Deposit initial amount : "))
                customerBalances.append(balance)

                print("\n---- Account Created Successfully ----")
                print("Name   :", customerNames[counter_2])
                print("Pin    :", customerPins[counter_2])
                print("Balance:", customerBalances[counter_2], "-/Rs")

                counter_1 += 1
                counter_2 += 1
                print("\nPlease remember your Name and PIN for login.")

        input("\nPress Enter to return to main menu...")

    # ------------------- Withdraw Money -------------------
    elif choiceNumber == "2":
        print("\nChoice number 2 is selected")

        name = input("Enter Name : ")
        pin = input("Enter PIN : ")

        if name in customerNames and pin in customerPins:
            k = customerNames.index(name)
            if pin == customerPins[k]:
                print("Your Current Balance:", customerBalances[k], "-/Rs")
                withdrawal = int(input("Enter amount to withdraw : "))

                if withdrawal > customerBalances[k]:
                    print("Insufficient Balance!")
                else:
                    customerBalances[k] -= withdrawal
                    print("\n---- Withdraw Successful ----")
                    print("Updated Balance:", customerBalances[k], "-/Rs")
        else:
            print("Invalid Name or PIN!")

        input("\nPress Enter to return to main menu...")

    # ------------------- Deposit Money -------------------
    elif choiceNumber == "3":
        print("\nChoice number 3 is selected")

        name = input("Enter Name : ")
        pin = input("Enter PIN : ")

        if name in customerNames and pin in customerPins:
            k = customerNames.index(name)
            if pin == customerPins[k]:
                print("Your Current Balance:", customerBalances[k], "-/Rs")
                deposition = int(input("Enter amount to deposit : "))
                customerBalances[k] += deposition
                print("\n---- Deposit Successful ----")
                print("Updated Balance:", customerBalances[k], "-/Rs")
        else:
            print("Invalid Name or PIN!")

        input("\nPress Enter to return to main menu...")

    # ------------------- Check Customers & Balances -------------------
    elif choiceNumber == "4":
        print("\nChoice number 4 is selected")
        print("\nCustomer List and Balances:")
        for x in range(len(customerNames)):
            print("Customer:", customerNames[x], "| Balance:", customerBalances[x], "-/Rs")

        input("\nPress Enter to return to main menu...")

    # ------------------- Exit Program -------------------
    elif choiceNumber == "5":
        print("\nThank you for using Times Bank!")
        print("Visit Again. Bye Bye 👋")
        break

    else:
        print("\nInvalid option! Try Again.")
        input("\nPress Enter to return to main menu...")
