import prompt
import random


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even(name, min_num, max_num, max_points):
    points = 0
    while points < max_points:
        num = random.randint(min_num, max_num)
        input_user = question(f'{num}')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if not is_win(name, input_user, correct_answer):
            return points
        points += 1
    return points


def calc(name, min_num, max_num, max_points):
    points = 0
    while points < max_points:
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        operand_rand = random.randint(1, 3)
        if operand_rand == 1:
            correct_answer = num1 + num2
            operand = '+'
        elif operand_rand == 2:
            correct_answer = num1 * num2
            operand = '*'
        else:
            correct_answer = num1 - num2
            operand = '-'
        input_user = question(f'{num1}{operand}{num2}')
        if not is_win(name, input_user, correct_answer):
            return points
        points += 1
    return points


def question(quest):
    print(f'Question: {quest}')
    return prompt.string('Your answer: ')


def is_win(name, input_user, correct_answer):
    if input_user != str(correct_answer):
        print(f"'{input_user}' is wrong answer ;(. Correct answer was \
'{correct_answer}'.\nLet's try again, {name}!")
        return False
    print('Correct!')
    return True


def finish(name, point, max_point):
    if point == max_point:
        print(f'Congratulations, {name}!')
