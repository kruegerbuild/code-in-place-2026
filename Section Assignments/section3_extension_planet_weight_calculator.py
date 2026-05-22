# constants for our weight on other planets relative to earth gravity
MERCURY_WEIGHT_MULTIPLIER = 0.376
VENUS_WEIGHT_MULTIPLIER = 0.889
MARS_WEIGHT_MULTIPLIER = 0.378
JUPITER_WEIGHT_MULTIPLIER = 2.36
SATURN_WEIGHT_MULTIPLIER = 1.1
URANUS_WEIGHT_MULTIPLIER = 0.815
NEPTUNE_WEIGHT_MULTIPLIER = 1.14

def main():
    # user will input their weight here
    user_weight = float(input("Enter your weight on earth: "))
    
    # then, user will choose a planet
    planet_choice = input("Enter a planet: ").lower()
    
    # if user input Mercury, then the calculation will be done by this body function
    if planet_choice == "mercury":
        mercury_weight = user_weight * MERCURY_WEIGHT_MULTIPLIER
        mercury_weight_rounded = round(mercury_weight, 2)
        print(f"The equivalent weight on Mercury: {mercury_weight_rounded}")

    # if user input Venus, then the calculation will be done by this body function
    elif planet_choice == "venus":
        venus_weight = user_weight * VENUS_WEIGHT_MULTIPLIER
        venus_weight_rounded = round(venus_weight, 2)
        print(f"The equivalent weight on Venus: {venus_weight_rounded}")

    # if user input Mars, then the calculation will be done by this body function
    elif planet_choice == "mars":
        mars_weight = user_weight * MARS_WEIGHT_MULTIPLIER
        mars_weight_rounded = round(mars_weight, 2)
        print(f"The equivalent weight on Mars: {mars_weight_rounded}")

    # if user input Jupiter, then the calculation will be done by this body function
    elif planet_choice == "jupiter":
        jupiter_weight = user_weight * JUPITER_WEIGHT_MULTIPLIER
        jupiter_weight_rounded = round(jupiter_weight, 2)
        print(f"The equivalent weight on Jupiter: {jupiter_weight_rounded}")

    # if user input Saturn, then the calculation will be done by this body function
    elif planet_choice == "saturn":
        saturn_weight = user_weight * SATURN_WEIGHT_MULTIPLIER
        saturn_weight_rounded = round(saturn_weight, 2)
        print(f"The equivalent weight on Saturn: {saturn_weight_rounded}")

# if user input Uranus, then the calculation will be done by this body function
    elif planet_choice == "uranus":
        uranus_weight = user_weight * URANUS_WEIGHT_MULTIPLIER
        uranus_weight_rounded = round(uranus_weight, 2)
        print(f"The equivalent weight on Uranus: {uranus_weight_rounded}")

# if user input Neptune, then the calculation will be done by this body function
    elif planet_choice == "neptune":
        neptune_weight = user_weight * NEPTUNE_WEIGHT_MULTIPLIER
        neptune_weight_rounded = round(neptune_weight, 2)
        print(f"The equivalent weight on Neptune: {neptune_weight_rounded}")

if __name__ == "__main__":
    main()