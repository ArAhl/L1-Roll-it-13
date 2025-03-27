
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


#Main routine

# ask the user if they want instructions
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)
