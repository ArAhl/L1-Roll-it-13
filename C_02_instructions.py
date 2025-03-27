
#functions go here
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


#Main routine


want_instructions = yes_no("Do you want to see the instructions? ")


if want_instructions == "yes":
    instructions()

print()
print("program continues")
