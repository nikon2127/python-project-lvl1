#!usr/bin/env python3
from brain_games.games import game


def main():
    min_num = 1
    max_num = 10
    points = 0
    max_points = 3
    name = game.hello()

    print('What is the result of the expression?')
    while points < max_points:
        quest, correct_answer = game.calc(min_num, max_num)
        input_user = game.question(quest)
        if not game.is_win(name, input_user, correct_answer):
            break
        points += 1
    game.finish(name, points, max_points)


if __name__ == '__main__':
    main()
