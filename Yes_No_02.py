# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        print()
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You have not chosen a valid response.")


# Main routine
while True:
    want_instructions = yes_no("Would you like to read the instructions? ")
    print(f"You've chosen {want_instructions}.")
