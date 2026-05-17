import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0 #initial score, can't be put inside of for loop

    for i in range (NUM_ROUNDS):
        print(f"Round {i + 1}")

        computer_number = random.randint(1,100) #won't be printed because user have to guess
        user_number = random.randint(1,100)

        print(f"Your number is {user_number}")

        user_guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if user_guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")

        print()
    
    print("Thanks for playing!")

'''
note for myself:
before the code block was:
if
if
else

and thus it prints twice (you were right/aww that's incorrect)
because python evaluate if as TRUE, second if as FALSE, thus second if's else became TRUE

now it has been resolved:
if
elif
else

now about score = 0:
score is always 1 when i put it inside of the for loop.
why? because every time the function loops back, the score is being reset to 0
so yep it won't add, so i put score = 0 outside of the loop

score += 1 means score = score + 1
'''

if __name__ == "__main__":
    main()