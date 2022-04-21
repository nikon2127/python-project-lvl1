import prompt
import random


def even(min_num, max_num):
    num = random.randint(min_num, max_num)
    print(f'Question: {num}')
    input_user = prompt.string('Your answer: ')
    return (input_user, num)


def eveno(name):
    min_num = 1
    max_num = 100
    num = 0
    max_points = 3
    points = 0

    while points < max_points:
        num = random.randint(min_num, max_num)
        print(f'Question: {num}')
        input_user = prompt.string('Your answer: ')
        if num % 2 == 0:
            if input_user == 'yes':
                print('Correct!')
            else:
                print(f"'{input_user}' is wrong answer ;(. \
                    Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        if num % 2 != 0:
            if input_user == 'no':
                print('Correct!')
            else:
                print(f"'{input_user}' is wrong answer ;(. \
                    Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
        points += 1
        if points == max_points:
            print(f'Congratulations, {name}!')
            break


def win_check(name, input_user, correct_answer):
    if input_user == correct_answer:
        return 'Correct!'
    return f"'{input_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n\
    Let's try again, {name}!"


def finish(name):
    return f'Congratulations, {name}!'
