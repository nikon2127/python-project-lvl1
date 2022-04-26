#!usr/bin/env python3
from brain_games.games import game


def main():
    name = game.hello()
    max_points = 3
    points = 0

    print('What is the result of the expression?')
    while points < max_points:
        report, is_check_win = game.calc(name, 1, 10)
        print(report)
        if not is_check_win:
            break
        points += 1
        game.finish(name, points, max_points)


if __name__ == '__main__':
    main()
