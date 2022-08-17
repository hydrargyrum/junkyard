from contextlib import contextmanager


@contextmanager
def pos_at(x, y):
    print('\x1B[s')
    print(f"\x1B[{y};{x}H")
    try:
        yield
    finally:
        print('\x1B[u')


@contextmanager
def graphical(s):
    print(f"\x1B[{s}m")
    try:
        yield
    finally:
        print('\x1B[m')


old_print = print


def print(*args, **kwargs):
    kwargs.setdefault('end', '')
    old_print(*args, **kwargs)


class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def fill(self):
        for row in range(self.y, self.y + self.h):
            with pos_at(self.x, row):
                print(' ' * self.w)

    def stroke(self):
        with pos_at(self.x, self.y):
            print('+')
            print('-' * (self.w - 2))
            print('+')

        for row in range(self.y + 1, self.y + self.h - 1):
            with pos_at(self.x, row):
                print('|')
            with pos_at(self.x + self.w - 1, row):
                print('|')

        with pos_at(self.x, self.y + self.h - 1):
            print('+')
            print('-' * (self.w - 2))
            print('+')
