import prompt
import random


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even(min_num, max_num):
    num = random.randint(min_num, max_num)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (num, correct_answer)


def calc(min_num, max_num):
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
    return (num1, num2, correct_answer, operand)


def gcd(min_num, max_num):
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    max_count = max(num1, num2)
    min_count = min(num1, num2)

    i = 1
    while i <= min_count:
        if min_count % i == 0 and max_count % (min_count // i) == 0:
            return (num1, num2, min_count // i)
        i += 1


def progression(min_num, max_num, min_step, max_step, row):
    colon = random.randint(1, row)
    step = random.randint(min_step, max_step)
    start_num = random.randint(min_num, max_num)
    quest = ''
    i = 1
    while i <= row:
        start_num += step
        quest += ' '
        if i == colon:
            quest += '..'
            correct_answer = start_num
        else:
            quest += str(start_num)
        i += 1
    return (quest.strip(), correct_answer)


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
