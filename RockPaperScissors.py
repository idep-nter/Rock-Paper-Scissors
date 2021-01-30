import random

def main():
    """
    The main function starts by printing an intro as usual, then asks for a player's
    move, generates opponent's move and evaluates a result.
    If it's a tie, it automatically starts over again.
    At the end it asks the player if he wants play again and if not, it prints his
    score.
    """
    intro()
    global score
    score = 0
    while True:
        pMove = playerMove()
        aiMove = superAIMove()
        if result(pMove, aiMove):
            continue
        if repeat():
            continue
        else:
            break
    print(f"Your score for today is: {score}\nBye!")

def intro():
    print("""
=================================
WELCOME TO THE GAME!

You already know the rules, so let's begin!
Have fun!
=================================
    """)

def playerMove():
    """
    Asks the player for a move and returns it after it checks if it's correct.
    """
    moves = ['p', 'r', 's']
    while True:
        try:
            move = input("Enter 'p' for paper, 'r' for rock or 's' for "
                         "scissors\n")
            if move not in moves:
                raise ValueError
            else:
                return move
        except ValueError:
            print("Please follow the instructions!")
            continue

def superAIMove():
    """
    Generates a random move.
    """
    moves = ['p', 'r', 's']
    move = random.choice(moves)
    return move

def result(pMove, aiMove):
    """
    Compares both moves and adds up score if player wins. If it's a tie, it
    returns True.
    """
    moves = {'p' : 'paper', 'r' : 'rock', 's' : 'scissors'}
    print(f"Your move is {moves[pMove]} and opponent's move is {moves[aiMove]}")
    print("And...")
    if (pMove == 'r' and aiMove == 's') or (pMove == 'p' and aiMove == 'r') \
            or (pMove == 's' and aiMove == 'p'):
        print("You have won!")
        global score
        score += 10
    elif pMove == aiMove:
        print("It's a tie!")
        return True
    else:
        print("You have lost!")


def repeat():
    """
    Asks the player if he wants to repeat the game and checks if the answer is correct.
    """
    while True:
        try:
            r = input("Want to play again? y/n\n")
            if r == "y":
                return True
            elif r == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Please enter 'y' for yes or 'n' for no.")
            continue
 
if _name_ == '_name_':
    main()           
