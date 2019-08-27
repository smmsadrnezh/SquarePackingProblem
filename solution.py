def solution(n, squares):
    big_square = [[-1] * n for _ in range(n)]

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
                return 'No Possible Answer For The Given Input.'

    return big_square
