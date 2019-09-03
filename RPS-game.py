import random
def swg():
    user_name = input("Enter your name:")
    list = ['Rock', 'Paper', 'Scissor']
    print(f"\nWelcome to the game Rock Paper Scissor Mr. {user_name}")
    print("You have got 10 chances to win the game")
    chance = 1
    human_point = 0
    computer_point = 0
    draw_count = 0
    while(chance <= 10):
        print("\nSelect Your choices:")
        print("Write:"
              "\n   (R) for Rock, (P) for Paper and (S) for Scissor")
        a = input()
        list_name = a.capitalize()
        choice = random.choice(list)
        if list_name == 'R':
            if choice == 'Scissor':
                human_point += 1
                print(f"\nYou choose Rock and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            elif choice == "Paper":
                computer_point += 1
                print(f"\nYou choose Rock and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            else:
                draw_count += 1
                print(f"\nYou choose Rock and computer choose {choice}")
                print(f"Chances left {10 - chance}")
        elif list_name == "P":
            if choice == "Scissor":
                computer_point += 1
                print(f"\nYou choose Paper and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            elif choice == "Rock":
                human_point += 1
                print(f"\nYou choose Paper and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            else:
                draw_count += 1
                print(f"\nYou choose Paper and computer choose {choice}")
                print(f"Chances left {10 - chance}")
        elif list_name == "S":
            if choice == "Paper":
                human_point += 1
                print(f"\nYou choose Scissor and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            elif choice == "Rock":
                computer_point += 1
                print(f"\nYou choose Scissor and computer choose {choice}")
                print(f"Chances left {10 - chance}")
            else:
                draw_count += 1
                print(f"\nYou choose Scissor and computer choose {choice}")
                print(f"Chances left {10 - chance}")
        elif list_name != "s" or 'g' or "w":
            print("Invalid Input!"
                  "\nPlease Insert Again!")
            print(f"Chances left {10 - chance}")

        chance += 1
    print("\nGame Over")
    if human_point == computer_point:
        print(f"Match Draw")
        print(f"{user_name} Points = {human_point}"
              f"\ncomputer points = {computer_point}"
              f"\nNo. of Drawn = {draw_count}")
    elif human_point > computer_point:
        print(f"{user_name} Wins with points {human_point}")
        print(f"{user_name}'s Points = {human_point}"
              f"\ncomputer points = {computer_point}"
              f"\nNo. of Drawn = {draw_count}")
    else:
        print(f"Computer Wins with points {computer_point}")
        print(f"{user_name}'s Points = {human_point}"
              f"\ncomputer points = {computer_point}"
              f"\nNo. of Drawn = {draw_count}")
swg()