import random
import time
limit = 5
mynumber = random.randint(1,50)

print("\n")
print("\t********* WELCOME TO GUESS GAME *********")
time.sleep(3)
def again():
	play_again = input(" Do you want to play again, y = 'yes', n = 'no' : ")
	while play_again.lower() not in ["y","n","yes","no"]:
		play_again = input(" Do you want to play again, y = 'yes', n = 'no' : ")
	else:
		if(play_again.lower() in ['y','yes']):
			print(" Okay here you go function")
			mynumber = random.randint(1,50)
			game(limit,mynumber)
		elif(play_again.lower() in ['n','no']):
			print("\n OKAY THEN BYE PLAY AGAIN SOON HOPE YOU ENJOYED !!")
			print(" Author : @dattu")
			exit()
		
def game(limit,mynumber):
    while True:
        guess = int(input("\n Enter your guess number : "))
        limit -= 1
        print(" The no.of turns remaining = ",limit)
        if(limit == 0):
            print("\n OOPS..! OUT OF TURNS (YOU LOSE) ..!")
            print(" the number is : ",mynumber)
            print(" Better Luck Next Time")
            print("\n")
            again()
        if mynumber < guess:
            print("\n the number is less than",guess)
        elif mynumber > guess:
            print("\n the number is greater than",guess)
        elif mynumber == guess:
            print("\nvWOO HOO YOU WIN")
            print("\n")
            again()

game(limit,mynumber)