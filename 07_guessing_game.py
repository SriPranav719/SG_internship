# Build a number guessing game.

import random

# def random_num():
#     return random.randint(1, 100)
# print(random_num())


# random_num = (random.randint(1, 10))

# if guess == random_num:
#     print("Yes the number is correct")

# else:
#     print(f"The number was {random_num}, Try once more")
    
    
random_num = (random.randint(1, 10))


attempts = int(input("Enter the max number of attempts you want to : "))

tries = 1

while tries <= attempts:
    
    try:
        guess = int(input("Guess a number between 1 to 10: "))
    
        if guess > 10:
            print("Enter number betweent 1 to 10 only")
        
        elif guess == random_num:
            print("Yes the number is correct")
            break
        else:
            print("The guessed number is wrong")
        
        
        tries+=1
        
    except ValueError:
        print("Enter a digit only")
        
if guess != random_num:
    print(f"Out of attempts the number was {random_num}")
