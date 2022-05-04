#!usr/bin/env python3
from brain_games.games import game


def main():
    points = 0
    max_points = 3
    max_num = 50
    max_step = 10
    row = 10
    name = game.hello()

    print('What number is missing in the progression?')
    while points < max_points:
        quest, correct_answer = game.progression(max_num,
                                                 max_step, row)
        input_user = game.question(quest)
        if not game.is_win(name, input_user, correct_answer):
            break
        points += 1
    game.finish(name, points, max_points)


if __name__ == '__main__':
    main()
