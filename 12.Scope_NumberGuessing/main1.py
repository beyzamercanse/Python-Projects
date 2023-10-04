###### SCOPE ########

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# enemies inside function: 2
# enemies outside function: 1

# LOCAL SCOPE
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) # this will give error


# GLOBAL SCOPE
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2  # local scopes
        print(player_health)

    drink_potion()


print(player_health)
# 2
# 10
