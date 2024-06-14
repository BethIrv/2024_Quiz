import random


# Checks if the user has entered yes (Y) or no (N)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"

        elif response in ["no", "n"]:
            return "no"

        else:
            print("Please enter Yes or No!")
            print()


# Display's the instructions
def instructions():
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
def question_generator(difficulty):

    # Initializes the ranges of difficulty
    if difficulty == 3:
        num_1 = random.randint(1, 30)
        num_2 = random.randint(1, 30)
    elif difficulty == 2:
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)
    else:
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
        print(f"\n⭐ Question {question_number} (Infinite Mode) ⭐")
    else:
        print(f"\n⭐ Question {num} of {num_questions} ⭐")

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
            print(f"🎉 You got the answer right, it was {answer}")
            return "correct", answer
        elif users_answer in wrong_answers:
            print("💔 You already provided this incorrect answer")
        else:
            attempts += 1
            wrong_answers.add(users_answer)
            if attempts < 3:
                print("💔 You got the answer wrong. Please try again!")
            else:
                print(f"😿 Sorry, You ran out of attempts. The correct answer was {answer}.")
                return "wrong", answer


# Generates the answer and prints quiz history
def answer_checker(num_questions):

    # Initialize variables
    total_won = 0
    total_lost = 0
    quiz_history = []
    question_number = 0

    # Asks the user for the desired difficulty
    difficulty = int_check("Choose the difficulty (Easy (1) / Medium (2) / Hard (3): ", low=1, high=3)

    if num_questions is not None:
        num_range = range(1, num_questions + 1)
    else:
        num_range = iter(int, 1)

    for num in num_range:
        if num_questions is None:
            question_number += 1

        result, answer = num_question(num, num_questions, difficulty, question_number)

        if result == "exit":
            print("You've Ended the Quiz!")
            break

        if result == "correct":
            total_won += 1
            quiz_history.append(
                f"Question {num if num_questions else question_number}: 🎉 You got the answer right!, "
                f"(The Answer:  {answer:<3})  ✅")

        elif result == "wrong":
            total_lost += 1
            quiz_history.append(
                f"Question {num if num_questions else question_number}: 💔 You ran out of attempts,    "
                f"(The Answer: {answer:<3})  ❌")

    # Calculates the quiz results
    total_questions = total_won + total_lost
    quiz_statistics(total_won, total_lost, total_questions)

    # Prints the quiz history
    print()
    history_feedback = yes_no("Would you like to view the Quiz History?: ")
    if history_feedback == "yes":
        print("\n💫💫 Quiz History 💫💫")
        for item in quiz_history:
            print(item)


# Generates the quiz results
def quiz_statistics(total_won, total_lost, total_questions):

    correct_percentage = (total_won / total_questions) * 100 if total_questions > 0 else 0
    wrong_percentage = (total_lost / total_questions) * 100 if total_questions > 0 else 0

    # Generates personalized messaged (based on the average score)
    if correct_percentage == 100:
        score_message = "🥳 You've gotten a score of 100%! - That's amazing!"
    elif correct_percentage >= 80:
        score_message = f"😻 You've gotten a score of {correct_percentage:.2f}%! - Great job!"
    elif correct_percentage >= 50:
        score_message = f"🙂 You've gotten a score of {correct_percentage:.2f}%! - Great Effort!"
    else:
        score_message = f"😔 You've gotten a score of {correct_percentage:.2f}%! - Continue Practicing!"

    # Prints the quiz results
    print("\n📊📊 Quiz Results 📊📊")
    print(f"Questions Correct: {total_won}/{total_questions} ({correct_percentage:.2f}%)")
    print(f"Questions Wrong  : {total_lost}/{total_questions} ({wrong_percentage:.2f}%)")
    print(f"{score_message}")


# Main routine

# Displays the title
print("✨ Welcome to Einesh's Basic Facts Quiz! ✨")

# Loop for testing purposes
print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# Displays the instructions
if want_instructions == "yes":
    instructions()

# Asks the user for the desired questions
print()
number_questions = int_check("How many questions would you like? (<enter> for Endless Questions): ",
                             low=1, exit_code="xxx")
if number_questions == "xxx":
    print("You Quit!")
else:
    answer_checker(number_questions)

print()
print("😻 Thank You for Playing My Quiz! 😻")
