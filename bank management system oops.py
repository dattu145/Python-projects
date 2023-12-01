import pickle
import os
from termcolor import colored

class users:
    def __init__(self,name,acc):
        self.name = name
        self.acc = acc
        self.balance = 0

class Bank:
    def __init__(self):
        self.userlist = []
        
    def add_to_list(self, name, acc):
 	   user = users(name, acc)
 	   self.userlist.append(user)
 	   print(colored("Account created successfully!","green"))
 	   
    def create_acc(self, name, acc):
    	new_user = True

    	if len(self.userlist) != 0:
        	for x in self.userlist:
        	    if name == x.name or acc == x.acc:
                	new_user = False
                	print(colored("\nSuch user already exists",'red'))
                	break 

    	if new_user:
        	self.add_to_list(name, acc)
    	else:
        	print(colored("Account creation failed. User already exists.","red"))

        
    def write_data(self):
        with open("BankUsers",'wb') as file:
        	pickle.dump(self.userlist,file)
        	
    def read_data(self):
        with open('BankUsers','rb') as file:
        	self.userlist = pickle.load(file)

    def Remove_account(self):
        name = input("Enter the User name : ").strip()
        acc = int(input('Enter account number : ').strip())
        user_found = False
        for x in self.userlist:
        	if name == x.name and acc == x.acc:
        		self.userlist.remove(x)
        		print(colored("User removed successfully",'green'))
        		user_found = True
        		break
        if not user_found:
        		print(colored("Such user doesn't exist","red"))
        		
    	
    def view_all_users(self):
        if len(self.userlist) != 0:
            for x in self.userlist:
                print(colored("\nUser details : ","yellow"))
                print(colored(f"\nName : {x.name}\nAccount Number : {x.acc}","cyan"))
        else:
            print(colored("\n->   Records not found..Create accounts","red"))


    def deposit(self,amt):
        accNo = int(input("Enter account Number :").strip())
        user_found = False
        for x in self.userlist:
            if accNo == x.acc:
                x.balance = x.balance + amt
                print(colored(f"${amt} Successfully deposited","green"))
                user_found = True
                break
        if not user_found:
        		print(colored("Such user doesn't exist or incorrect accNO","red"))

    def withdraw(self,amt):
        accNo = int(input("Enter account Number :").strip())
        user_found = False
        for x in self.userlist:
            if accNo == x.acc:
                if amt < x.balance:
                	x.balance = x.balance - amt
                	print(colored(f"${amt} Successfully withdrawn","green"))
                else:
                	print(colored("Insufficient funds check balance",'red'))
                user_found = True
                break
        if not user_found:
        		print(colored("Such user doesn't exist or Incorrect accNO","red"))

    def change_user_details(self):
        user_found = False
        accNo = int(input("\nEnter account Number :").strip())
        for x in self.userlist:
            if accNo == x.acc:
            	name = input("Enter new username : ")
            	acc = int(input("Enter new account number : "))
            	x.name = name
            	x.acc = acc
            	print(colored("User details successfully updated","green"))
            	user_found = True
            	break
        if not user_found:
            print(colored("Such user doesn't exist or Incorrect accNO","red"))
            		

    def show_details(self):
        accNo = int(input("Enter acount number : ").strip())
        user_found = False
        for x in self.userlist:
        	if accNo == x.acc:
        		print(colored(f"\nUser Details :\n\nName : {x.name}\nAcc no : {x.acc}\nCurrent Bal : ${x.balance}","cyan"))
        		user_found = True
        		break
        if not user_found:
        		print(colored("Incorrect credentials or user not found..","red"))
        		
    def view_balance(self):
        accNo = int(input("Enter account Number :").strip())
        user_found = False
        for x in self.userlist:
            if accNo == x.acc:
                print(colored(f"Current bal : ${x.balance}","green"))
                user_found = True
                break
        if not user_found:
        		print(colored("Invalid account number..","red"))
                
    def reset_data(self):
    	self.userlist.clear()
    	print(colored("Data cleared successfully!","green"))

vignesh = Bank()
vignesh.read_data()

def wrapper():
    while True:
        print("\n#####    Bank Management System    #######\n\n1). Create Account\n2). Deposit\n3). Withdraw\n4). Balance Enquiry\n5). List all users\n6). User enquiry\n7). Remove account\n8). Reset Data\n9). Change user details\n0). Exit")
        choice = int(input("\nEnter Choice : ").strip())
        if choice == 1:
            name = input("Enter holder name : ")
            acc = int(input("Enter acc number : ").strip())
            vignesh.create_acc(name, acc)
            vignesh.write_data()
        elif choice == 2:
            amt = int(input("Enter amount to be deposited : ").strip())
            vignesh.deposit(amt)
            vignesh.write_data()
        elif choice == 3:
            amt = int(input("Enter amount to be withdrawn : ").strip())
            vignesh.withdraw(amt)
            vignesh.write_data()
        elif choice == 4:
            vignesh.view_balance()
        elif choice == 5:
            vignesh.view_all_users()
        elif choice == 6:
        	vignesh.show_details()
        elif choice == 7:
            vignesh.Remove_account()
            vignesh.write_data()
        elif choice == 8:
        	vignesh.reset_data()
        	vignesh.write_data()
        elif choice == 9:
        	vignesh.change_user_details()
        	vignesh.write_data()
        elif choice == 0:
            print(colored("\nFelt Great Serving U, Visit Once Again!","light_magenta"))
            break


wrapper()
#text = "	python	"
#print(f"{text:*^30}")

