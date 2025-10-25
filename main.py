import random
import time
from pathlib import Path
import csv

file_path = Path("database.csv")
file_exists = file_path.exists()

def offer_hint(num):
    
    hint_toggle = input("Would you like a hint? (yes/no) ").strip().lower()
    
    if hint_toggle == "yes":
        
        hint = num - (num % 10)
        print(f"Hint: range is between {hint} and {hint + 10}")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")

difficulty = None

while True:

    choice = None
    
    while choice not in ("1", "2", "3", "4"):
        
        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print("4. View top scores\n")

        choice = input("Enter your choice:").strip()

        if choice == "1":
            
            difficulty = "Easy"
            total_guesses = 10
            
        elif choice == "2":
            
            difficulty = "Medium"
            total_guesses = 5
            
        elif choice == "3":
            
            difficulty = "Hard"
            total_guesses = 3
            
        elif choice == "4":
            
            if file_path.exists():
                
                with file_path.open("r", newline="") as f:
                    
                    reader = csv.reader(f)
                    
                    print("\n---------------| TOP SCORES |---------------")
                    
                    for row in reader:
                        
                        print(*row)
                    
                    print("--------------------------------------------\n")
                pass
                    
            else: 
                print("No score data yet.")
            
            choice = None
                
        else:
            
            print("Error: choose a valid option")
            choice = None

    print(f"Great! You have selected the {difficulty} difficulty level — You have {total_guesses} guesses\nLet's start the game!")

    num = random.randint(1,100)

    guesses = total_guesses

    start = time.time()

    while guesses != 0:

        try:
            
            user_guess = int(input("Enter your guess: "))
        
        except ValueError:
            
            print("Invalid input! Please enter a number.")
            continue

        if user_guess == num:
            
            print(f"Congratulations! You guessed the correct number in {total_guesses - guesses} attempts.")
            end = time.time()
            print(f"You guessed the correct number in {int(end - start)}s.")
            
            
            with file_path.open("a", newline="") as f:
                
                writer = csv.writer(f)
                
                if not file_exists:
                    
                    if f.tell() == 0:
                        
                        writer.writerow(["highscore", "seconds", "difficulty"])
                    
                writer.writerow([total_guesses - guesses, int(end - start), difficulty])
            
            break
            
        if user_guess > num:
            
            print(f"Incorrect! The number is less than {user_guess}. You have {guesses - 1} guesses left!")
            guesses = guesses - 1
            
            if guesses == total_guesses -1:
                
                offer_hint(num)
        
        if user_guess < num:
            
            print(f"Incorrect! The number is greater than {user_guess}. You have {guesses - 1} guesses left!")
            guesses = guesses - 1
            
            if guesses == total_guesses -1:
                
               offer_hint(num)

    if guesses > 0:
        
        result = "won!!!"
        
    else:
        
        result = "lost..."
        
    print(f"Game over! You {result}")
    
    restart = input("Do you wanna play again? (yes/no)\n")
    
    if restart in ("no", "n"):
        
        print("Thanks for playing!")
        break
    
    elif restart in ("yes", "y"):
        
        print("\nRestarting game...\n")
        continue
    
    else:
        
        print("Invalid input, please enter yes or no.")