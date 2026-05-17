'''
In Nimm, the initial number of stones is 20, and there are 2 players. So we defines them
'''

def main():
    stones_count = 20 #initial number of stones
    current_player = 1 #to indicate 1st player's turn

    while stones_count > 0: 
        print(f"There are {stones_count} stones left.")
        user_input = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))
        if current_player == 1:
            current_player = 2 #to switch turn to 2nd player after 1st player inputed
        else:
            current_player = 1 #to switch turn to 1st player after 2nd player inputed
        
        input_is_invalid = user_input > 2 #we want the player to only input the number 1 or 2
        while (input_is_invalid):
            user_input = int(input("Please enter 1 or 2: "))
            input_is_invalid = user_input > 2 #required again inside the while loop to recheck (to prevent infinite loop)

        stones_count = stones_count - user_input
        print()

        if stones_count <= 0:
            print(f"Player {current_player} wins!")


if __name__ == '__main__':
    main()