import random

def winner(user, computer) :

    if user == 1 and computer == 1:
        print("draw .")
        return None

    elif user == 1 and computer == 2:
        print("Computer win this round .")
        return 1

    elif user == 1 and computer == 3:
        print("You win this round .")
        return 0

    elif user == 2 and computer == 1:
        print("You win this round .")
        return 0

    elif user == 2 and computer == 2:
        print("draw .")
        return None

    elif user == 2 and computer == 3:
        print("Computer win this round .")
        return 1

    elif user == 3 and computer == 1:
        print("Computer win this round .")
        return 1

    elif user == 3 and computer == 2:
        print("You win this round .")
        return 0

    elif user == 3 and computer == 3:
        print("draw .")
        return None

    else:
        print("invalid .")


def final_result(user_point, computer_point) :
    """ This function print the final result"""
    if user_point > computer_point:
        print(f"You won {user_point} games ")
        print(f"A.I. won {computer_point} games ")
        print("Congratulation , you won this game ! ")

    elif user_point < computer_point:
        print(f"Your won {user_point} games ")
        print(f"A.I. won {computer_point} games ")
        print("A.I. win this game ! good luck for next time ")

    else:
        print(f"Your won {user_point} games ")
        print(f"A.I. won {computer_point} games ")
        print("Draw !!!")


""" Main program start from here """
i = 1
user_point = 0
computer_point = 0
dict = {1: "Stone", 2: "paper", 3: "sessior"}

name = input("Enter your name : ")
n = int(input(f"{name} how many times you want to play a game :  "))
print("\n")

""" Taking input from user and generate computer input """
while i <= n:
    user = int(input("choose 1 for stone ,  2 for paper , 3 for gun : "))
    print(f"{name} : ", dict[user])

    computer = random.randint(1, 3)
    print("A.I. : ", dict[computer])

    """ Function to print and count the point of every round """
    result = winner(user, computer)

    if result == 0:
      user_point += 1

    elif result == 1:
      computer_point += 1

    else:
      user_point += 0
      computer_point += 0

    print("\n")
    i += 1

"""Function to print the final result"""
final_result(user_point, computer_point)
