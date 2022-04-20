#!usr/bin/env python3
import prompt
import random


def main():
    min_num = 1
    max_num = 100
    num = 0
    max_points = 3
    points = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while points < max_points:
        num = random.randint(min_num, max_num)
        print(f'Question: {num}')
        input_user = prompt.string('Your answer: ')
        if num % 2 == 0 and input_user == 'yes':
            print('Correct!')
        elif num % 2 != 0 and input_user == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        points += 1
        if points == max_points:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
