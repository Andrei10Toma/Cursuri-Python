import random


def conditional():
    my_var = 9

    if my_var < 6:
        print("Numarul este mai mic decat 6")
    elif my_var < 10:
        print("Numarul este mai mare decat 6 si mai mic decat 10")

    apple = 3
    has_apple = "Apple" if apple else "Not apple"
    print(has_apple)


def looping():
    choices = [x for x in range(11)]
    while True:
        random_choice = random.choice(choices)
        if random_choice % 3 == 0:
            break
        print(f"Random choice is {random_choice}")
    print(f"Exit random choice is {random_choice}")


def continue_looping():
    for i in range(10):
        if i % 2 != 0:
            continue
        print(f"{i} Numarul este par")


def my_function(list_param):
    new_list_param = list(list_param)
    new_list_param.append(4)
    print("list_param inside function: ", new_list_param)


def my_function_2(name, age, job="Student", has_car=True):
    has_car_str = "a car" if has_car else "no car"
    print(f"My name is {name} and my age is {age}. I'm a {job} and I have {has_car_str}.")
    print("-" * 80)


def my_function_3(*args, **kwargs):
    print(args)
    print(kwargs)
    # for arg in args:
    #     print(f"arg is {arg}")
    # for key in kwargs.keys():
    #     print(f"key {key} has value {kwargs[key]}")
    # print("-" * 80)


def my_function_5():
    while True:
        my_var = input("Introduceti numarul: ")
        try:
            my_int = int(my_var)
            # print(mi_int)
        except ValueError as e:
            print("Introduceti un numar intreg", e)
        except NameError as e:
            # print("Ai folosit o variabila nedefinita")
            pass
        else:
            print("Nicio exceptie nu a fost aruncata")
        finally:
            print("Se executa tot timpul!")


def my_function_4():
    msg = "Hello, World!"
    print(msg)


def my_function_6():
    def my_subfunction_6():
        print(f"my subfunction {msg}")
    msg = "Hello world"
    my_subfunction_6()


if __name__ == '__main__':
    # conditional()
    # looping()
    # continue_looping()
    # list_param = [1, 2, 3]
    # my_function(list_param)
    # print("list_param outside function: ", list_param)
    # my_function_2("John", 21)
    # my_function_2("Andrei", 20, "Developer", False)
    # my_function_3("Ana")
    # my_function_3("Ana", "are", "mere")
    # my_function_3(1, 2, 3, name="Ana", verb="are", complement="mere")
    my_function_6()