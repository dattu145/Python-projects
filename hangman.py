import random
import time

randlist = ["skyblue","border","image","film","promise","kids","lungs","dupe","rhyme","damn","plants","explode","world"]

randwrd = random.choice(randlist)

print("\n")
print("\t********** WELCOME TO HANGMAN GAME ***********\n")
time.sleep(2)
print("""   RULES :
	
	1). You should enter only one letters at a time
	2). Do not leave blank input
	3). Guess the number in 5 turns!
	""")
time.sleep(2)
def hangman(randwrd):
	count = 0
	randwrd = random.choice(randlist)
	limit = 5
	display = "_" * len(randwrd)
	guessed = []
	letters = list(randwrd)
	
	print(f"\nYOUR GUESS WORD CONSISTS OF : {len(randwrd)} letters\n")
	while (count < limit):
		userguess = input(f"The hangman word is {display}, enter your guess : ").strip()
			
		while len(userguess) == 0 or len(userguess) > 1:
			print(str("\nInvalid input (check rules)...!\n").upper())
			userguess = input(f"The hangman word is {display}, enter your guess : ").strip()
			
			
		if userguess in guessed:
			print("Oops! you already tried that try a new letter")
			continue
			
		if userguess in letters:
			index = randwrd.find(userguess)
			display = display[:index] + userguess + display[index + 1:]
			letters.remove(userguess)	
			
		else:
			guessed.append(userguess)
			count += 1
			if count == 1:
				time.sleep(1)
				print("\n+---+")
				print("O   |")
				print("    |")
				print("    |")
				print("   ===\n")
				print(f"Number of turns remaining : {limit-count}\n")
			elif count == 2:
				time.sleep(1)
				print("\n+---+")
				print("O   |")
				print("|   |")
				print("    |")
				print("   ===\n")
				print(f"Number of turns remaining : {limit-count}\n")
			elif count == 3:
				time.sleep(1)
				print("\n+---+")
				print(" O  |")
				print("/|  |")
				print("    |")
				print("   ===\n")
				print(f"Number of turns remaining : {limit-count}\n")
			elif count ==4:
				time.sleep(1)
				print("\n+---+")
				print(" O  |")
				print("/|\ |")
				print("    |")
				print("   ===\n")
				print(f"Number of turns remaining : {limit-count}\n")
			elif count == 5:
				time.sleep(1)
				print("\n+---+")
				print(" O   |")
				print("/|\  |")
				print("/ \  |")
				print("    ===\n")
				print("\nOoops! out of turns...")
				print("YOU LOSE ...")
				print(f"The guess number is : {randwrd}")
				
		if "_" not in display:
			print(f"\nWooHoo! You won the guess word is : {randwrd}")
			print(f"You indentified the guess word in {count}/{limit} chances")
			print("\nauthor : @dattu")
			break
			
	again()

def again():
	ask = input("\nDo you want to play again(y/n) : ").lower()
	while ask not in ["y","yes","no","n"]:
		ask = input("\nDo you want to play again(y/n) : ").lower()
	if ask in ["no","n"]:
		print("\nOkay thanks for playing the game !!")
		print("Hope you liked it!")
	elif ask in ["y","yes"]:
		hangman(randwrd)
		
hangman(randwrd)
