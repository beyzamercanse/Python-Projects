# game_level = 3
# enemies = ["skeleton", "zombie", "alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)  # skeleton


game_level = 3


def create_enemy():

    enemies = ["skeleton", "zombie", "alien"]
    if game_level < 5:
        new_enemy = enemies[0]


# name 'new_enemy' is not defined because its a local scpe defined within the functin
print(new_enemy)
