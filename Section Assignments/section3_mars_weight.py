"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.

Note: works in every weight unit (kg, lbs)
"""
MARS_WEIGHT_MULTIPLIER = 0.378

def main():
    user_input = float(input("Enter a weight on Earth: "))
    mars_weight = user_input * MARS_WEIGHT_MULTIPLIER
    mars_weight = round(mars_weight, 2)
    print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == "__main__":
    main()