
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



#main routine starts here
game_goal = int_check()
print(game_goal)