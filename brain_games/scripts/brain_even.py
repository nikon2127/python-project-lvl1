#!usr/bin/env python3
from brain_games.games import game


def main():
    name = game.hello()
    max_points = 3
    points = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while points < max_points:
        input_user, num = game.even(1, 100)
        print(game.win_check(name, input_user, num))
        if game.win_check(name, input_user, num) != 'Correct':
            break
        points += 1
        if points == max_points:
            game.finish(name)
            break


if __name__ == '__main__':
    main()
