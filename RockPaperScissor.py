import random

def play_rock_paper_scissors():
        choices = ["Rock", "Paper", "Scissors"]

        while True:
                print("Choose your choice: \n1. Rock \n2. Paper \n3.Scissors")
                user_choice = int(input("Enter your choice: "))

                for i in range(user_choice):
                        if i >= 3:
                                print("Invalid choice. Please try again.")
                                play_rock_paper_scissors()
                                break
                        
                if user_choice == 1:
                        user_in = 'Rock'

                elif user_choice == 2:
                        user_in = 'Paper'

                elif user_choice == 3:
                        user_in = 'Scissors'
                        
                print('User choice is: ', user_in)
                print("\nNow it's computer's turn")
                        
                computer_choice =  random.choice(choices)
                print(f"Computer choose: {computer_choice}")

                if user_in == computer_choice:
                        print("\nIt's a Tie!")

                elif (user_choice == 1 and computer_choice == "Scissors") or \
                     (user_choice == 2 and computer_choice == "Rock") or \
                     (user_choice == 3 and computer_choice == "Paper"):
                        print("\nYou Win!")

                else:
                        print("\nYou Lose!")
                
                play_again = input("\nPlay again? (yes = y or no = n): ").lower()
                if play_again == "n":
                        break
                
play_rock_paper_scissors()
