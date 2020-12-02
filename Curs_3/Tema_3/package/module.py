def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


def recursive_even_sum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + recursive_even_sum(n - 2)
    else:
        return recursive_even_sum(n - 1)


def recursive_odd_sum(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return n + recursive_odd_sum(n - 2)
    else:
        return recursive_odd_sum(n - 1)