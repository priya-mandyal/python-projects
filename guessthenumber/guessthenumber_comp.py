import random

def guess(x):
    random_number = random.randint(1, x+1)  # both included
    guess = 0
    while (guess != random_number) :
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if(guess > random_number) :
            print("Too high, guess again!")
        elif (guess < random_number):
            print("Too low, guess again!")
    print(f"Yay!!! You have guessed the number {random_number} correctly!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low == high): 
            guess = low
        else:
            guess = random.randint(low, high)
        feedback = input(f"Is the number {guess} too HIGH (h) or too LOW (l) or CORRECT (c): ")
        if(feedback == 'l'):
            low = guess + 1
        else:
            high = guess - 1
    print(f"YAY! Computer guessed your number {guess} correctly!!")


# guess(17)
computer_guess(100)