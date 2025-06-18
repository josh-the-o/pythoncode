import random

def path():
    print("You're currently in the asteroid field.")

def mercury(difficulty, player_health):
    print("You've landed on Mercury.")
    player_health = alien(difficulty, player_health)
    return player_health

def venus(resource_level, player_health):
    print("You've landed on Venus.")
    player_health = resource_gathering(resource_level, player_health)
    return player_health

def jupiter(player_health):
    print("You've arrived at Jupiter.")
    choice = input("Explore a moon (Y/N)? ")
    if choice.lower() == 'y':
        player_health = moon(player_health)
    else:
        print("You are heading to Saturn.")
    return player_health

def moon(player_health):
    print("You are on one of Jupiter's moons.")
    player_health = resource_gathering("medium", player_health)
    return player_health

def saturn(player_health, difficulty):
    print("You've arrived at Saturn.")
    player_health = alien(difficulty, player_health)
    return player_health

def neptune(player_health):
    print("You've arrived at Neptune.")
    player_health = finalboss(player_health)
    return player_health

def mars(player_health):
    print("You've landed on Mars.")
    player_health = riddle(player_health)
    return player_health

def pluto(player_health):
    print("You've reached Pluto.")
    player_health = riddle(player_health)
    return player_health

def uranus(player_health, difficulty):
    print("You've arrived at Uranus.")
    player_health = alien(difficulty, player_health)
    return player_health

def finalboss(player_health):
    print("You face the ultimate challenge: the Cosmic Destroyer!")
    player_health = boss_fight(player_health)
    return player_health

def resource_gathering(resource_level, player_health):
    if resource_level == "high":
        health_gain = 30
    elif resource_level == "medium":
        health_gain = 20
    else:
        health_gain = 10

    player_health += health_gain
    print(f"You gained {health_gain} health. Your current health is {player_health}.")
    return player_health

def alien(difficulty, player_health):
    if difficulty == "easy":
        alien_health = 20
        alien_damage = 5
    elif difficulty == "medium":
        alien_health = 30
        alien_damage = 10
    else:
        alien_health = 40
        alien_damage = 15

    while alien_health > 0 and player_health > 0:
        player_action = input("Attack (A) or Defend (D)? ")
        if player_action.lower() == 'a':
            damage_dealt = random.randint(10, 20)
            alien_health -= damage_dealt
            print(f"You dealt {damage_dealt} damage. Alien health is now {alien_health}.")
        elif player_action.lower() == 'd':
            shield_gained = random.randint(5, 10)
            print(f"You defended and gained {shield_gained} shield points.")
        else:
            print("Invalid input.")

        if alien_health > 0:
            player_health -= alien_damage
            print(f"The alien attacks you for {alien_damage} damage. Your health is now {player_health}.")

    return player_health

def boss_fight(player_health):
    alien_health = 100
    alien_damage = 30

    while alien_health > 0 and player_health > 0:
        player_action = input("Attack (A) or Defend (D)? ")
        if player_action.lower() == 'a':
            damage_dealt = random.randint(15, 25)
            alien_health -= damage_dealt
            print(f"You dealt {damage_dealt} damage. Boss health is now {alien_health}.")
        elif player_action.lower() == 'd':
            shield_gained = random.randint(5, 15)
            print(f"You defended and gained {shield_gained} shield points.")
        else:
            print("Invalid input.")

        if alien_health > 0:
            player_health -= alien_damage
            print(f"The boss attacks you for {alien_damage} damage. Your health is now {player_health}.")

    return player_health

def riddle(player_health):
    riddles = [
        ("I speak without a mouth and hear without ears. I have no body, but I can still talk. What am I?", "echo"),
        ("I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?", "breath")
    ]
    riddle, answer = random.choice(riddles)
    user_answer = input(riddle + "\nYour answer: ").lower()
    if user_answer == answer:
        print("Correct!")
        player_health += 10 
    else:
        print("Incorrect!")
        player_health -= 5
    print(f"Your current health is {player_health}.")
    return player_health

def main():
    player_health = 100
    resource_level = random.choice(["low", "medium", "high"])
    difficulty = random.choice(["easy", "medium", "hard"])

    while player_health > 0:
        print("\nWhere do you want to go? (Enter a number)")
        print("1. Mercury")
        print("2. Venus")
        print("3. Mars")
        print("4. Jupiter")
        print("5. Saturn")
        print("6. Uranus")
        print("7. Neptune")
        print("8. Pluto")
        print("9. Asteroid Field")
        choice = input("> ")

        if choice == '1':
            player_health = mercury("easy", player_health)
        elif choice == '2':
            player_health = venus(resource_level, player_health)
        elif choice == '3':
            player_health = mars(player_health)
        elif choice == '4':
            player_health = jupiter(player_health)
        elif choice == '5':
            player_health = saturn(player_health, "medium")
        elif choice == '6':
            player_health = uranus(player_health, "hard")
        elif choice == '7':
            player_health = neptune(player_health)
        elif choice == '8':
            player_health = pluto(player_health)
        elif choice == '9':
            path()

        if player_health <= 0:
            print("You died")
            break

    if player_health > 0:
        print("YAY you won!")

main()
