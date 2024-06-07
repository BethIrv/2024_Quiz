# checks users enter yes (y) or no (n)
import random


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")


# Displays instructions to user
def instruction():
    print('''
+-+ Instructions +-+

Welcome to the Basic Facts Quiz!!

To begin, choose which difficulty you want to play. 
You can choose between, easy, medium, and hard. 

Next, choose how many questions you would like.
Press <enter> if you want infinite questions. 

You can leave the game at any time by entering <xxx>

Try and get as many questions correct within three attempts. 

Enjoy!!
    ''')


# Check's if the user has entered a valid integer
def int_check(question, low=None, high=None, exit_code="xxx"):
    # Sets up the error message

    if low is None and high is None:
        error = "Please Enter an Integer"

    # Checks if the number entered is an integer
    elif low is not None and high is None:
        error = f"Please Enter an integer That is More Than or Equal to {low}"

    # Checks if the number entered is between a high and low number (inclusive)
    else:
        error = f"Please Enter an Integer That is Between {low} and {high} (Inclusive)"

    while True:
        response = input(question)

        if response.strip() == "":
            return None

        elif response == exit_code:
            return response

        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

    # Generates the questions based on it's difficulty


# Main routine
print()
print("😸😸 Basic Facts Quiz 😸😸")

# loop for testing purposes

print()
want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
print()
questions = int_check("How many questions would you like to answer? (Push <enter> for infinite mode): ")

if questions == "infinite":
    mode = "infinite"
    print("You've chosen infinite")
    questions = 5

    # asks user if they want to customise the number range
    print()
    difficulty_level = "What level difficulty would you like (Easy, Medium, Hard):"


def question_generator(difficulty_level):
    # Initializes the ranges of difficulty
    if difficulty_level == "Hard":
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, 50)
    elif difficulty_level == "Medium":
        num_1 = random.randint(1, 25)
        num_2 = random.randint(1, 25)
    elif difficulty_level == "Easy":
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)

    # Lists the possible math operations
    math_operations = ["addition", "subtraction", "multiplication", "division"]
    operation = random.choice(math_operations)

    # Generates the questions & answers for the math operations involved
    if operation == "subtraction":
        num_1 = num_1 + num_2
        question = f"What's {num_1} - {num_2}?: "
        answer = num_1 - num_2
    elif operation == "addition":
        question = f"What's {num_1} + {num_2}?: "
        answer = num_1 + num_2
    elif operation == "multiplication":
        question = f"What's {num_1} x {num_2}?: "
        answer = num_1 * num_2
    else:
        num_1 = num_1 * num_2
        question = f"What's {num_1} ÷ {num_2}?: "
        answer = num_1 // num_2

    return question, answer


# Generates the question numbers and attempts
def num_question(num, num_questions, difficulty, question_number):
    # Displays the question numbers
    if num_questions is None:
        print(f"\n Question {question_number}")
    else:
        print(f"\n Question {num} of {num_questions} ")

    question, answer = question_generator(difficulty)
    attempts = 0

    # Sets previous wrong attempts
    wrong_answers = set()

    # Prints the amount of attempts the user has
    while attempts < 3:
        if attempts > 0:
            print(f"\nAttempt {attempts + 1}:")

        # Collects the users answer
        users_answer = int_check(question, low=1)

        # Quits the quiz if exit code is entered
        if users_answer == "xxx":
            return "exit", answer

        if users_answer == answer:
            print(f" You are correct, the answer is {answer}!")
            return "correct", answer
        elif users_answer in wrong_answers:
            print(" You already given this answer")
        else:
            attempts += 1
            wrong_answers.add(users_answer)
            if attempts < 3:
                print(" You are incorrect, Please try again")
            else:
                print(f" You've run out of attempts. The correct answer is {answer}.")
                return "wrong", answer


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Initialise game variables
mode = "regular"
questions_asked = 0

print()
