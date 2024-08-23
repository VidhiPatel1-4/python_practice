
stone = 1
paper = 2
scissor = 3

user_input = int(input("Enter a number from User  (1 = Stone, 2 = Paper, 3 = Scissor): "))
computer_input = int(input("Enter a number from computer  (1 = Stone, 2 = Paper, 3 = Scissor): "))

if user_input not in [stone, paper, scissor] or computer_input not in [stone, paper, scissor]:
    print("Invalid number")
else:
    if user_input == computer_input:
        print("Tie")

    elif user_input == stone:
        if computer_input == paper:
            print("Computer Wins")

        elif user_input == stone:
            if computer_input == scissor:
                print("User Wins")

    elif user_input == paper:
        if computer_input == stone:
            print("User Wins")

        elif user_input == paper:
            if computer_input == scissor:
                print("Computer Wins")

    elif user_input == scissor:
        if computer_input == stone:
            print("Computer Wins")

        elif user_input == scissor:
            if computer_input == paper:
                print("User Wins")







