"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: "))

    while n > 1:
        if n % 2 == 0: #check if n is an even number
            old_n = n #defining old_n because we're taking the value of n into old_n, so n can be calculated into new number
            n = old_n // 2 #divide by "//" so n will be a whole number (integer)
            print(f"{old_n} is even, so I take half: {n}")
        else: #odd number (can also be n % 2 != 0; n % 2 == 1)
            old_n = n #defining old_n because we're taking the value of n into old_n, so n can be calculated into new number
            n = int(old_n * 3 + 1)
            print(f"{old_n} is odd, so I make 3n + 1: {n}")

if __name__ == "__main__":
    main()