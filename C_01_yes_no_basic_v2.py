
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


#Main routine

#testing loop...
while True:
    want_instructions = yes_no("Do you want to see the instructions? ")
    print(f"you chose {want_instructions}")

print ("we done")
