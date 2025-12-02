# "Number Guessing Game"
import random
print("Number Guessing Game \n")
name=input('Enter Your Name Here: ')
print ("Hai,", name, "Welcome to the Number Guessing Game. \n You have 7 chances to guess the number. \n Let's Start the game. \n")
low = int(input("Enter the Lower Range: "))
high = int (input("Enter the Higher Range:"))
print(f"\n You have 7 chances only to guess the number between {low} and {high}. Let's start! \n")
num = random.randint(low, high)
ch = 10       #Total chances allowed
gc = 0       #Guess counter
while gc < ch:
  gc += 1
  guess = int (input("Enter Your Guessed Number:"))
  if guess == num:
    print (f"Correct {name}! The Number is {num}. You guessed it in {gc} attempts.")
    break
  elif gc >= ch and guess != num:
    print (f'Sorry {name}! The Number was {num}. Better Luck next time.')
  elif guess > num:
    print ("Too High! Try a lower number... \n")
  elif guess < num:
    print ("Too Low! Try a higher number...\n")
