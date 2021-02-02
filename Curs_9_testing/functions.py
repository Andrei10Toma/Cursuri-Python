def iter_sum(data):
    current_sum = 0

    my_iter = iter(data)
    for n in my_iter:
        current_sum += n

    return current_sum


def iterator_sum(*args):
    sums = []
    for iter_item in args:
        try:
            sums.append(iter_sum(iter_item))
        except TypeError:
            sums.append(0)

    return sums


class MyIterator:
    def __init__(self, max=3):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration
