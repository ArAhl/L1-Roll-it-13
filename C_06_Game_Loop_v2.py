import random
from _ast import If
# functions go here

def yes_no (question):
    while True:

        response = input(question).lower()
        if response == "yes" or  response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print(""" 
*** Instuctions ****

Roll the dice and try to win!
""")


def int_check():
    """checks users enter an integer more than / equal to 13"""

    error = 'please enter an integer more than / equal to 13.'

    while True:
        try:
            respons = int(input("What is the game goal? "))

            if respons < 13:
                print(error)
            else:
                return respons

        except ValueError:
            print(error)


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for user and note if they got double
    roll_one = random.randint(1, 6)
    roll_two = random.randint (1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two}\t| Total: {total} ")

    return total, double

def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main starts here...

# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

make_statement("welcome to the Roll It 13 Game",  "🍀")

# ask the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()


# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # Start of round loop
    make_statement(f"Round {rounds_played}", "🎲")

    # For testing purposes, ask the user what the points for the user / computer were
    # Roll the dice for the user and note if they got a double
    initial_user = initial_points("user")
    initial_comp = initial_points("comp")

    # Retrieve user points (first item returned from function
    user_points = initial_user [0]
    comp_points = initial_comp [0]

    double_user = initial_user [1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points!")

    # assume user goes first...
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer\n")

    # if the user and computer roll equal points, the users is player 1
    elif user_points == comp_points:
        print("The initial rolls were the same, the user starts!")

    # if the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round\n")

        # first person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second} {player_2_points}")

    # end of the round

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "computer":
        user_points, comp_points = comp_points, user_points

    # work out who won and set the loser points to zero...
    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset to zero"

    # double user points if eligible
    if winner == "User" and double_user == "yes":
        user_points = user_points * 2

    # Outside rounds loop - Update score with round points, only add points to the score of the score of the winner
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")   # replace with call to statement generator
    print(f"User Score: {user_score} | Computer score {comp_score}")

# end of entire game, output final results
print()
if user_score > comp_score:
    print("The user won")   # replace this with statement generator call
else:
    print("The computer won")


