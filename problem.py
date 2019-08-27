class Square:
    def __init__(self, up, right, down, left):
        self.dents = {'up': up, 'right': right, 'down': down, 'left': left}
        self.used = False

    def __repr__(self):
        return '({:02d}, {:02d}, {:02d}, {:02d})'.format(self.dents['up'], self.dents['right'], self.dents['down'],
                                                         self.dents['left'])


def problem():
    while True:
        try:
            n = int(input('Enter n: '))
            break
        except ValueError:
            print('Wrong Number.')

    squares = list()
    for i in range(n * n):
        while True:
            try:
                edges = input('Enter Dents in Clockwise Order For Square[{}][{}]:\n'.format(i // n, i % n))
                squares.append(Square(*(int(dent) for dent in edges.split(' '))))
                break
            except TypeError:
                print('Wrong Dents.')

    return n, squares
