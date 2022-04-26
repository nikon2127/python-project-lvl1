#!usr/bin/env python3
from brain_games.games import game
import random


def main():
    min_num = 1
    max_num = 100
    max_points = 3
    points = 0
    name = game.hello()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    # points = game.even(name, 1, 100, max_points)
    while points < max_points:
        num = random.randint(min_num, max_num)
        input_user = game.question(f'{num}')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if not game.is_win(name, input_user, correct_answer):
            break
        points += 1
    game.finish(name, points, max_points)


if __name__ == '__main__':
    main()
