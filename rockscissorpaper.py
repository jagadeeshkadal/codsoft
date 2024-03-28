import random

choice = ("rock", "paper", "scissor")
play=True


def game():

    while play:
        player = None
        computer = random.choice(choice)
        while player not in choice:
            player = input("Enter a choice (rock, paper, scissor): ")

        print("Player:" ,player)
        print("Computer:" ,computer)

        if computer == player:
            
            print("It's a tie!")
            
        elif player == "rock" and computer == "scissor":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissor" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")
        if not input("press (y or n)").lower()=="y" :
            break
game()
print("Thanks for playing!")




