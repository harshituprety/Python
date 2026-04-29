import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Enter your number:"))
    if(guess > random_number):
      print(f"Guess is wrong.Number is too high")
    elif(guess < random_number):
      print(f"Guess is wrong. Number is too low")

  print(f"Guess is correct. Hurrah!👋")

guess(29)