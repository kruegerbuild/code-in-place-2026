import random

def main():
    print("Khansole Academy")
    
    first_number = random.randint(10, 99)
    second_number = random.randint(10, 99)
    correct_answer  = first_number + second_number

    print(f"What is {first_number} + {second_number}?")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

if __name__ == '__main__':
    main()