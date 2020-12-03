from package.module import recursive_sum, recursive_even_sum, recursive_odd_sum


def my_function(*args, **kwargs):
    s = 0
    for value in args:
        try:
            converted_value = float(value)
            s += converted_value
        except ValueError:
            continue
        except TypeError:
            continue
    return s


def is_integer():
    try:
        number = input("Enter a number: ")
        int_number = int(number)
        return int_number
    except ValueError:
        return 0


if __name__ == '__main__':
    print(my_function(1, 5.2, -3, "abc", [12, 56, "cad"]))
    print(my_function())
    print(my_function(2, 4, "abc", param_1=2))
    print(is_integer())
    print(recursive_sum(10))
    print(recursive_even_sum(10))
    print(recursive_odd_sum(10))
