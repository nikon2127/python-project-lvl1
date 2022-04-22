import prompt
import random


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even(min_num, max_num):
    num = random.randint(min_num, max_num)
    print(f'Question: {num}')
    input_user = prompt.string('Your answer: ')
    return (input_user, num)


def win_check(name, input_user, correct_answer):
    if input_user == correct_answer:
        return 'Correct!'
    return f"'{input_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n\
    Let's try again, {name}!"


def finish(name):
    return f'Congratulations, {name}!'
