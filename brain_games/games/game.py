import prompt
import random


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even(name, min_num, max_num):
    num = random.randint(min_num, max_num)
    print(f'Question: {num}')
    input_user = prompt.string('Your answer: ')
    if (num % 2 == 0 and input_user == 'yes')\
            or (num % 2 != 0 and input_user == 'no'):
        return ('Correct!', True)
    elif num % 2 == 0:
        return (f"'{input_user}' is wrong answer ;(. Correct answer was 'yes'.\n\
Let's try again, {name}!", False)
    else:
        return (f"'{input_user}' is wrong answer ;(. Correct answer was 'no'.\n\
Let's try again, {name}!", False)


def win_check(name, input_user, correct_answer):
    if input_user == correct_answer \
        or (int(correct_answer) % 2 == 0 and input_user == 'yes') \
            or (int(correct_answer) % 2 != 0 and input_user == 'no'):
        return ('Correct!', True)
    return (f"'{input_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n\
Let's try again, {name}!", False)


def finish(name):
    return f'Congratulations, {name}!'
