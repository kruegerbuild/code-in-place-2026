import random

NUM_SIDES = 10

def main():
    roll = input("How many sides does your dice have? ")
    roll = random.randint(1, NUM_SIDES)
    print("Your roll is ", roll)

if __name__ == '__main__':
    main()