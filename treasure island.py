def play_game():
    print("\nWelcome to the treasure island")

    path1 = input("Narrator: You are at a crossroad, choose your path: 'left' or 'right'? ").lower()

    if path1 == 'left':
        path2 = input("You have come to a lake. There is an island in the middle of the lake.\nYou have 2 choices: 'wait' for a boat or 'swim' to safety: ").lower()

        if path2 == 'wait':
            path3 = input("You arrive at the island. There are 3 doors.\nOne 'red', one 'yellow', one 'blue'. Pick a color: ").lower()

            if path3 == 'red':
                print("The room is filled with poisonous snakes. YOU ARE DEAD!!!")
                return "end"

            elif path3 == 'yellow':
                print("You find the treasure. YOU WIN!")
                return "end"

            elif path3 == 'blue':
                print("You are transported back to the beginning...")
                return "restart"

            else:
                print("Invalid choice. YOU ARE DEAD!")
                return "end"
        else:
            print("You got surrounded by man-eating crocodiles. YOU ARE DEAD!!")
            return "end"
    else:
        print("You fell into a hole. YOU ARE DEAD!!!!")
        return "end"

# Main loop
while True:
    result = play_game()

    if result == "restart":
        continue  # Automatically restart game on blue door
    else:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break


