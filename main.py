import random

from pandas import DataFrame


def problem():
    global n, squares, big_square

    class Square:
        def __init__(self, up, right, down, left):
            self.dents = {'up': up, 'right': right, 'down': down, 'left': left}
            self.used = False

        def dent_in_count(self):
            return sum(filter(lambda x: x == -1, self.dents.values()))

        def dent_out_count(self):
            return sum(filter(lambda x: x == 1, self.dents.values()))

        def __repr__(self):
            return str(self.dents)

    while True:
        try:
            n = int(input('Enter n: '))
            break
        except ValueError:
            print('Wrong Number.')

    squares = list()
    for i in range(n * n):
        edges = (random.randrange(-1, 2) for _ in range(4))
        squares.append(Square(*edges))
    big_square = [[-1] * n for _ in range(n)]


def solution():
    for row in range(n):
        for column in range(n):
            edges = dict()

            if row == 0:
                edges['up'] = 0
            elif row == n - 1:
                edges['up'] = - big_square[row - 1][column].dents['down']
                edges['down'] = 0
            else:
                edges['up'] = - big_square[row - 1][column].dents['down']

            if column == 0:
                edges['left'] = 0
            elif column == n - 1:
                edges['left'] = - big_square[row][column - 1].dents['right']
                edges['right'] = 0
            else:
                edges['left'] = - big_square[row][column - 1].dents['right']

            for square in squares:
                if square.used:
                    continue

                if square.dents['up'] == edges['up'] and square.dents['left'] == edges['left']:
                    right = square.dents['right'] == edges['right'] if 'right' in edges.keys() else True
                    down = square.dents['down'] == edges['down'] if 'down' in edges.keys() else True
                    if right and down:
                        square.used = True
                        big_square[row][column] = square
                        break
            else:
                return 'No Possible Answer For The Given Input'

    return DataFrame(big_square)


if __name__ == "__main__":
    problem()
    print(solution())
