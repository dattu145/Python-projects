import random
tools = ["rock","paper","scissors"]
rounds = 0
comwin = 0
userwin = 0
tiematches = 0
calc=""
cpu = random.choice(tools)
print("\n")
print("\t********* ROCK,PAPER,SCISSORS ********\n")

name = input("ENTER YOUR NAME : ")
while name.lower() == "":
	name = input("ENTER YOUR NAME : ")
	
while rounds < 5:
	print("\n# ------ ROUND",rounds+1,"----- #")
	user = input("\nEnter your choice, r='rock' , p='paper' & s='scissors' : ")
	
	while user.lower() not in ["r","p","s","rock","paper","scissors"]:
		user = input("Enter your choice, r='rock' , p='paper' & s='scissors' : ")
	else:
	 if user.lower() in ["r","rock"]:
	    user = "rock"
	 elif user.lower() in ["p","paper"]:
	    user = "paper"
	 elif user.lower() in ["s","scissors"]:
	    user = "scissors"
	 print("\nComputer choice :",cpu)
	 print("Your choice :",user)
	 
	 if ((cpu=="rock" and user=="paper") or (cpu=="scissors" and user=="rock") or (cpu == "paper" and user=="scissors")):
	 	print("\n===> You won\n")
	 	userwin += 1
	 elif ((cpu == "paper" and user == "rock") or (cpu == "rock" and user == "scissors") or (cpu == "scissors" and user=="paper")):
	 	print("\n===> computer won\n")
	 	comwin += 1
	 else:
	 	print("\n===> Tie")
	 	tiematches+=1
	 cpu = random.choice(tools)
	 rounds+=1
	 
print("\n")
print("\t\t ¥¥¥¥ FINAL RESULTS ¥¥¥¥")

print("\nTotal rounds won by you is : ",userwin)
print("Total rounds won by the computer is : ",comwin)
print("Tie matches :",tiematches)
if(userwin > comwin):
	calc = name
elif(userwin < comwin):
	calc = "the computer"
else:
	calc = "OOPS! ITS A TIE"
print("\nTHE MAJORITY WINS,SO WINNER IS :",calc)


		
		