#!usr/bin/env python3
from brain_games.games import game
import random


def main():
    min_num = 1
    max_num = 10
    points = 0
    max_points = 3
    name = game.hello()

    print('What is the result of the expression?')
    # points = game.calc(name, 1, 10, max_points)
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
        input_user = game.question(f'{num1}{operand}{num2}')
        if not game.is_win(name, input_user, correct_answer):
            break
        points += 1
    game.finish(name, points, max_points)


if __name__ == '__main__':
    main()
