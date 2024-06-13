import random
print("WELCOM TO THIS GAME!")
while True:
        choices = ['rock', 'paper', 'scissors']
        computer= random.choice(choices)
        player=None

        while player not in choices:
            player=(input("\n""Rock,Paper,Scissors ? :").lower())
            if player not in choices:
                print("\t""Enter the given options !""\n")

        if player == computer:
            print("\t""Computer :", computer)
            print("\t""Player : ", player)
            print("\t\t""Both Tied")
        elif player=='rock':
            if computer=='paper':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you loss :(")
            if computer=='scissors':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you win :)")

        elif player=='paper':
            if computer=='rock':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you win :)")
            if computer=='scissors':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you lose :(")

        elif player=='scissors':
            if computer=='paper':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you win :)")
            if computer=='rock':
                print("\t""Computer :", computer)
                print("\t""Player : ", player)
                print("\t\t""you loss :(")
        play_again = input("\n""Do you want to play again [ yes :) / no :( ] : ").lower()
        if play_again !="yes":
            break

print("\n\t""Thank you for Playing")