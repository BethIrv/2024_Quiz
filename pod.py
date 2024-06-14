import random

def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")

def instruction():
    print('''
+-+ Instructions +-+

Welcome to the Basic Facts Quiz!!

To begin, choose which difficulty you want to play. 
You can choose between easy, medium, and hard. 

Next, choose how many questions you would like.
Press <enter> if you want infinite questions. 

You can leave the game at any time by entering <xxx>

Try and get as many questions correct within three attempts. 

Enjoy!!
    ''')

def select_difficulty():
    while True:
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Please enter a valid difficulty level.")

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"
        to_check = input(question)
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

print()
print("😸😸 Basic Facts Quiz 😸😸")
print()
want_instructions = yes_no("Would you like to read the instructions? ")
if want_instructions == "yes":
    instruction()

question_list = {
    "easy": ["1 + 1", "2 * 3", "4 - 2", "5 + 3"],
    "medium": ["12 / 3", "7 * 8", "15 - 6", "9 + 4"],
    "hard": ["sqrt(16)", "8^2", "3!", "sin(π/2)"]
}

mode = "regular"
questions_asked = 0

print\
    ()
difficulty = select_difficulty()

questions = int_check("How many questions would you like to answer? (Press <enter> for infinite mode): ")
if questions == "infinite":
    mode = "infinite"
    print("You've chosen infinite")
    questions = 5

def string_checker(param, question_list):
    pass

while questions_asked < questions:
    if mode == "infinite":
        quiz_heading = f"\nRound  {questions_asked + 1} (Infinite mode) "
    else:
        quiz_heading = f"\n🎗🎗🎗 Question {questions_asked + 1} of {questions} 🎗🎗🎗"
    print(quiz_heading)
    print()

    question = random.choice(question_list[difficulty])
    print("Question:", question)

    user_answer = input("Your answer: ")
    if user_answer == "xxx":
        print("You've quit.")
        break

    # Compare user's answer with correct answer (not implemented)

    questions_asked += 1
    if mode == "infinite":
        questions += 1
