def greet(bot_name, birth_year):
    """
    Greets the user with the bot's name and creation year.
    
    Parameters:
    bot_name (str): The name of the bot.
    birth_year (str): The year the bot was created.
    """
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

def remind_name():
    """
    Prompts the user to input their name and acknowledges it with a greeting.
    """
    print('Please, remind me your name.')
    name = input()  # Takes user input for their name
    print('What a great name you have, ' + name + '!')

def guess_age():
    """
    Asks the user for remainders of their age when divided by 3, 5, and 7,
    then calculates and displays the user's age.
    """
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    # Takes inputs for the remainder of age when divided by 3, 5, and 7
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    
    # Calculates age based on the given remainders
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():
    """
    Asks the user for a number and counts from 0 to that number.
    """
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())  # Takes the upper limit of the count as input
    curr = 0
    
    # Loops and prints each number from 0 up to the input number
    while curr <= num:
        print(curr, '!')
        curr += 1  # Increments the counter

def test():
    """
    Conducts a simple programming knowledge quiz with the user. 
    If the answer is incorrect, prompts to try again until the correct answer is given.
    """
    print("Let's test your programming knowledge.")
    
    # Quiz question and options
    print('Which of the following is not related to OOPS concept?')
    print('1. Abstraction')
    print('2. Parallel Programming')
    print('3. Inheritance')
    print('4. Polymorphism')

    # Repeatedly prompts user for an answer until the correct one is provided
    while True:
        choice = int(input())  # User input for quiz answer

        # Checks if the selected option is correct
        if choice == 2:
            end()  # Calls the end function for the congratulatory message
            break
        else:
            print('Please, try again.')  # Prompts user to try again for incorrect answers

def end():
    """
    Prints a congratulatory message to signify successful completion of the quiz.
    """
    print('Congratulations, have a nice day!')

# Program Execution Flow
greet('Aid', '2020')  # Greet with bot's name and creation year
remind_name()         # Prompt and greet the user by name
guess_age()           # Guess user's age based on input remainders
count()               # Prove counting capability up to user-defined number
test()                # Conduct the programming knowledge test
