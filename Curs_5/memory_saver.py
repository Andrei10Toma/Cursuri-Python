import copy

print("Memory savers!!")
# my_lambda = lambda x, y: x + y

# my_sum = my_lambda(2, 3)

# print(my_sum)

# print(id(my_lambda))
# print(id(lambda: 1))
# print(id(my_lambda))
# print(id(lambda: 3))

players = [
    {
        "first name": "John",
        "last name": "Doe",
        "rank": 3
    },
    {
        "first name": "Kevin",
        "last name": "McDonald",
        "rank": 1
    },
    {
        "first name": "Brad",
        "last name": "Kelvin",
        "rank": 2
    }
]
print(players)
sorted_players = sorted(players, key=lambda player: player["rank"], reverse=True)
print(sorted_players)


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player["is_top_3"] = True if player["rank"] < 4 else False
    return updated_player


top_players = map(check_top_3_player, players)
print(list(top_players))


def filter_all_mcdonalds(player):
    if player["last name"] == "McDonald":
        return True
    else:
        return False


# all_mcdonalds = list(filter(filter_all_mcdonalds, players))
all_mcdonalds = list(filter(lambda player: player["last name"] == "McDonald", players))
print(all_mcdonalds)

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers):
    print(f"{letter} -> {number}")
my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers]
squared_numbers_even = [item ** 2 for item in my_numbers if item % 2 == 0]
print(squared_numbers)
print(squared_numbers_even)
