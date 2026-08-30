import random
import time

start_time = time.time()

random_characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
    "-", "=", "[", "]", "{", "}", "|", "\\", ":", ";", '"', "'",
    "<", ">", ",", ".", "?", "/"
]

armour = []
weapons = []
stats = []

print("Dark Fantasy\nExplore the world!")

player_name = input("Create a name\n> ")

time.sleep(3)

print(f"Hello {player_name}!\nGenerating world...")

time.sleep(4)


class Player:
    def __init__(self, name):
        self.health = 100
        self.damage = 20
        self.name = name
        self.damage_bonus = 0
        self.absorption = 0


# Create player instance
player = Player(player_name)


class Goblin:
    def __init__(self):
        self.health = 50
        self.damage = 10


goblin = Goblin()


class Skeleton:
    def __init__(self):
        self.health = 75
        self.damage = 15


skeleton = Skeleton()


class Titan:
    def __init__(self):
        self.health = 400
        self.damage = 60


titan = Titan()


class Minion:
    def __init__(self):
        self.health = 30
        self.damage = 10


minion = Minion()


class Dragon:
    def __init__(self):
        self.health = 1000
        self.damage = 100



dragon = Dragon()


def menu():
    while True:
        print("1. Explore")
        print("2. Rest")
        print("3. Quit")

        choice = input("> ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


def all_choice():
    while True:
        print("1. View armour.")
        print("2. View weapons.")
        print("3. View Health.")
        print("4. View Stats")
        print("5. Continue.")

        choice = input("> ")

        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid input. Please choose 1, 2, 3, 4, or 5.")


def goblin_combat():
    goblin.health = 50

    print("\nYou fight the goblin!\n")
    time.sleep(3)

    while player.health > 0 and goblin.health > 0:

        goblin_attack = random.randint(1, 10)

        if goblin_attack % 2 == 0:

            # Check for best armour and apply absorption
            if "Moon Armour" in armour:
                damage_taken = goblin.damage * (1 - player.absorption)

                print(
                    f"The goblin attacks you for {goblin.damage} damage, "
                    f"but your Moon Armour absorbs "
                    f"{goblin.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Diamond Set" in armour:
                damage_taken = goblin.damage * (1 - player.absorption)

                print(
                    f"The goblin attacks you for {goblin.damage} damage, "
                    f"but your Diamond Set absorbs "
                    f"{goblin.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Chainmail" in armour:
                damage_taken = goblin.damage * (1 - player.absorption)

                print(
                    f"The goblin attacks you for {goblin.damage} damage, "
                    f"but your Chainmail absorbs "
                    f"{goblin.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            else:
                print(f"The goblin attacks you for {goblin.damage} damage!")
                player.health -= goblin.damage

            time.sleep(2)

            if player.health <= 0:
                print("You have died!")
                time.sleep(3)
                print("Thanks for playing!")
                exit()

        else:
            print("The goblin misses you!")
            time.sleep(3)

        while True:
            player_attack1 = input("Press 1 to attack!\n> ")

            if player_attack1 == "1":

                print("You attack the goblin!")

                # Check for best weapon and apply damage bonus
                if "Sun Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(f"You deal {total_damage} damage with your Sun Blade!")

                elif "Diamond Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Diamond Blade!"
                    )

                elif "Iron Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Iron Blade!"
                    )

                else:
                    total_damage = player.damage
                    print(f"You deal {total_damage} damage!")

                goblin.health -= total_damage

                time.sleep(3)

                print(f"Goblin health: {goblin.health}\n")

                if goblin.health <= 0:
                    print("You defeated the goblin!")
                    stats.append("Goblin defeated")
                    break

                break

            else:
                print("Invalid input. Please press 1 to attack.")

        print(f"Health: {player.health}\n")
        time.sleep(3)


def minion_combat():
    minion.health = 30

    print("\nYou fight the Minion!\n")
    time.sleep(3)

    while player.health > 0 and minion.health > 0:

        minion_attack = random.randint(1, 10)

        if minion_attack % 2 == 0:

            # Check for best armour and apply absorption
            if "Moon Armour" in armour:
                damage_taken = minion.damage * (1 - player.absorption)

                print(
                    f"The Minion attacks you for {minion.damage} damage, "
                    f"but your Moon Armour absorbs "
                    f"{minion.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Diamond Set" in armour:
                damage_taken = minion.damage * (1 - player.absorption)

                print(
                    f"The Minion attacks you for {minion.damage} damage, "
                    f"but your Diamond Set absorbs "
                    f"{minion.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Chainmail" in armour:
                damage_taken = minion.damage * (1 - player.absorption)

                print(
                    f"The Minion attacks you for {minion.damage} damage, "
                    f"but your Chainmail absorbs "
                    f"{minion.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            else:
                print(f"The Minion attacks you for {minion.damage} damage!")
                player.health -= minion.damage

            time.sleep(2)

            if player.health <= 0:
                print("You have died!")
                time.sleep(3)
                print("Thanks for playing!")
                exit()

        else:
            print("The Minion misses you!")
            time.sleep(3)

        while True:
            player_attack = input("Press 1 to attack!\n> ")

            if player_attack == "1":

                # 20% chance to hit the minion
                hit_chance = random.randint(1, 10)

                if hit_chance <= 2:

                    print("You attack the Minion!")

                    # Check for best weapon and apply damage bonus
                    if "Sun Blade" in weapons:
                        total_damage = player.damage + player.damage_bonus
                        print(
                            f"You deal {total_damage} damage with your Sun Blade!"
                        )

                    elif "Diamond Blade" in weapons:
                        total_damage = player.damage + player.damage_bonus
                        print(
                            f"You deal {total_damage} damage with your Diamond Blade!"
                        )

                    elif "Iron Blade" in weapons:
                        total_damage = player.damage + player.damage_bonus
                        print(
                            f"You deal {total_damage} damage with your Iron Blade!"
                        )

                    else:
                        total_damage = player.damage
                        print(f"You deal {total_damage} damage!")

                    minion.health -= total_damage

                    time.sleep(3)

                    print(f"Minion health: {minion.health}\n")

                    if minion.health <= 0:
                        print("You defeated the Minion!")
                        stats.append("Minion defeated")
                        break

                else:
                    print(
                        "You swing at the Minion but miss!\n"
                        "It's too small to hit consistently!"
                    )
                    time.sleep(3)

                break

            else:
                print("Invalid input. Please press 1 to attack.")

        print(f"Health: {player.health}\n")
        time.sleep(3)


def skeleton_combat():
    skeleton.health = 75

    print("\nYou fight the Skeleton!\n")
    time.sleep(3)

    while player.health > 0 and skeleton.health > 0:

        skeleton_attack = random.randint(1, 10)

        if skeleton_attack % 2 == 0:

            # Check for best armour and apply absorption
            if "Moon Armour" in armour:
                damage_taken = skeleton.damage * (1 - player.absorption)

                print(
                    f"The Skeleton attacks you for {skeleton.damage} damage, "
                    f"but your Moon Armour absorbs "
                    f"{skeleton.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Diamond Set" in armour:
                damage_taken = skeleton.damage * (1 - player.absorption)

                print(
                    f"The Skeleton attacks you for {skeleton.damage} damage, "
                    f"but your Diamond Set absorbs "
                    f"{skeleton.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Chainmail" in armour:
                damage_taken = skeleton.damage * (1 - player.absorption)

                print(
                    f"The Skeleton attacks you for {skeleton.damage} damage, "
                    f"but your Chainmail absorbs "
                    f"{skeleton.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            else:
                print(
                    f"The Skeleton attacks you for {skeleton.damage} damage!"
                )
                player.health -= skeleton.damage

            time.sleep(2)

            if player.health <= 0:
                print("You have died!")
                time.sleep(3)
                print("Thanks for playing!")
                exit()

        else:
            print("The Skeleton misses you!")
            time.sleep(3)

        while True:
            player_attack2 = input("Press 1 to attack!\n> ")

            if player_attack2 == "1":

                print("You attack the Skeleton!")

                # Check for best weapon and apply damage bonus
                if "Sun Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Sun Blade!"
                    )

                elif "Diamond Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Diamond Blade!"
                    )

                elif "Iron Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Iron Blade!"
                    )

                else:
                    total_damage = player.damage
                    print(f"You deal {total_damage} damage!")

                skeleton.health -= total_damage

                time.sleep(3)

                print(f"Skeleton health: {skeleton.health}\n")

                if skeleton.health <= 0:
                    print("You defeated the Skeleton!")
                    stats.append("Skeleton defeated")
                    break

                break

            else:
                print("Invalid input. Please press 1 to attack.")

        print(f"Health: {player.health}\n")
        time.sleep(3)


def titan_combat():
    titan.health = 400

    print("\nYou fight the Titan!\n")
    time.sleep(3)

    while player.health > 0 and titan.health > 0:

        titan_attack = random.randint(1, 10)

        if titan_attack % 2 == 0:

            # Check for best armour and apply absorption
            if "Moon Armour" in armour:
                damage_taken = titan.damage * (1 - player.absorption)

                print(
                    f"The Titan attacks you for {titan.damage} damage, "
                    f"but your Moon Armour absorbs "
                    f"{titan.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Diamond Set" in armour:
                damage_taken = titan.damage * (1 - player.absorption)

                print(
                    f"The Titan attacks you for {titan.damage} damage, "
                    f"but your Diamond Set absorbs "
                    f"{titan.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Chainmail" in armour:
                damage_taken = titan.damage * (1 - player.absorption)

                print(
                    f"The Titan attacks you for {titan.damage} damage, "
                    f"but your Chainmail absorbs "
                    f"{titan.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            else:
                print(f"The Titan attacks you for {titan.damage} damage!")
                player.health -= titan.damage

            time.sleep(2)

            if player.health <= 0:
                print("You have died!")
                time.sleep(3)
                print("Thanks for playing!")
                exit()

        else:
            print("The Titan misses you!")
            time.sleep(3)

        while True:
            player_attack = input("Press 1 to attack!\n> ")

            if player_attack == "1":

                print("You attack the Titan!")

                # Check for best weapon and apply damage bonus
                if "Sun Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Sun Blade!"
                    )

                elif "Diamond Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Diamond Blade!"
                    )

                elif "Iron Blade" in weapons:
                    total_damage = player.damage + player.damage_bonus
                    print(
                        f"You deal {total_damage} damage with your Iron Blade!"
                    )

                else:
                    total_damage = player.damage
                    print(f"You deal {total_damage} damage!")

                titan.health -= total_damage

                time.sleep(3)

                print(f"Titan health: {titan.health}\n")

                if titan.health <= 0:
                    print("You defeated the Titan!")
                    stats.append("Titan defeated")
                    break

                break

            else:
                print("Invalid input. Please press 1 to attack.")

        print(f"Health: {player.health}\n")
        time.sleep(3)


def dragon_combat():

    dragon.health = 1000

    print("\nYou fight the Dragon!\n")
    time.sleep(3)

    while player.health > 0 and dragon.health > 0:

        dragon_attack = random.randint(1, 10)

        # 70% chance for dragon to hit
        if dragon_attack <= 7:

            # Check for best armour and apply absorption
            if "Moon Armour" in armour:

                damage_taken = dragon.damage * (1 - player.absorption)

                print(
                    f"The Dragon attacks you for {dragon.damage} damage, "
                    f"but your Moon Armour absorbs "
                    f"{dragon.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Diamond Set" in armour:

                damage_taken = dragon.damage * (1 - player.absorption)

                print(
                    f"The Dragon attacks you for {dragon.damage} damage, "
                    f"but your Diamond Set absorbs "
                    f"{dragon.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            elif "Chainmail" in armour:

                damage_taken = dragon.damage * (1 - player.absorption)

                print(
                    f"The Dragon attacks you for {dragon.damage} damage, "
                    f"but your Chainmail absorbs "
                    f"{dragon.damage * player.absorption:.1f} damage!"
                )

                print(f"You take {damage_taken:.1f} damage!")
                player.health -= damage_taken

            else:

                print(
                    f"The Dragon attacks you for {dragon.damage} damage!"
                )

                player.health -= dragon.damage

            time.sleep(2)

            if player.health <= 0:

                print("You have died!")
                time.sleep(3)

                print("Thanks for playing!")
                exit()

        else:

            print("The Dragon misses you!")
            time.sleep(3)

        while True:

            player_attack = input("Press 1 to attack!\n> ")

            if player_attack == "1":

                print("You attack the Dragon!")

                # Check for best weapon and apply damage bonus
                if "Sun Blade" in weapons:

                    total_damage = player.damage + player.damage_bonus

                    print(
                        f"You deal {total_damage} damage with your Sun Blade!"
                    )

                elif "Diamond Blade" in weapons:

                    total_damage = player.damage + player.damage_bonus

                    print(
                        f"You deal {total_damage} damage with your Diamond Blade!"
                    )

                elif "Iron Blade" in weapons:

                    total_damage = player.damage + player.damage_bonus

                    print(
                        f"You deal {total_damage} damage with your Iron Blade!"
                    )

                else:

                    total_damage = player.damage

                    print(f"You deal {total_damage} damage!")

                dragon.health -= total_damage

                time.sleep(3)

                print(f"Dragon health: {dragon.health}\n")

                if dragon.health <= 0:

                    print("You defeated the Dragon!")
                    stats.append("Dragon defeated")
                    break

            else:

                print("Invalid input. Please press 1 to attack.")

        print(f"Health: {player.health}\n")
        time.sleep(3)


def scene_1():
    print(
        "You fall into a berry shrub and land in a dark world in which "
        "everything is conscious.\n"
        "You don't know how you got here but everything feels calm. "
        "You look around.\n"
        "Total darkness"
    )

    time.sleep(6)

    choice_1 = menu()

    if choice_1 == "1":

        print(
            "You look up at the moon. It has a face. It's creepy. "
            "You look around and see a towering castle on a hill.\n"
            "Everything moves.\n"
            "You see a small gnome smoking a pipe."
        )

        time.sleep(3.5)

        print(
            "Everything is weird, but you feel calm. "
            "You feel safe. You feel free."
        )

        time.sleep(3.5)

        print(
            "You look down at your feet and see a leather tunic set\n"
            "laying next to you with a stone sword."
        )

        armour.append("Leather Tunic Set")
        weapons.append("Stone Sword")

        time.sleep(3)

        print(
            "You start walking toward the castle and the gnome and hear\n"
            "an eerie but soothing song of a woman singing."
        )

        time.sleep(3)

        print(
            "You make your way up to the hill and hear a giggle from behind you.\n"
        )

        time.sleep(5)

        print(
            "You turn around and see a goblin attacking you! "
            "You have to react!"
        )

        while True:

            choice_2 = input("Press 1 to fight or 2 to run: ")

            if choice_2 == "1":
                goblin_combat()
                break

            elif choice_2 == "2":
                print("You run from the goblin!")
                time.sleep(3)

                print(
                    "You escaped him and keep climbing from a different point."
                )

                time.sleep(3)

                print("He disappears into the abyss.")
                break

            else:
                print("Invalid input. Please choose 1 or 2.")

    elif choice_1 == "2":

        print("You rest and recover.")

        if player.health == 100:
            print(f"Health: {player.health}\n")

        elif player.health < 100:
            player.health += 25

            if player.health > 100:
                player.health = 100

            print(f"Health: {player.health}\n")
            time.sleep(3)

    elif choice_1 == "3":
        exit()


def scene_2():

    while True:

        all_choice_1 = all_choice()

        if all_choice_1 == "1":
            print(f"Armour: {armour}")

        elif all_choice_1 == "2":
            print(f"Weapons: {weapons}")

        elif all_choice_1 == "3":
            print(f"Health: {player.health}\n")

        elif all_choice_1 == "4":
            print(f"Stats: {stats}")

        elif all_choice_1 == "5":
            break

    print(f"Your health is {player.health}")
    time.sleep(3)

    choice_3 = menu()

    if choice_3 == "1":

        print(
            "You reach the top of the hill and enter the gates of the castle.\n"
        )

        time.sleep(3)

        print(
            "You see a dimly lit hallway with an armour stand to the side "
            "displaying chainmail and an iron blade at its feet."
        )

        while True:

            choice_4 = input(
                "Do you take the chainmail? (y/n): "
            ).strip().lower()

            if choice_4 == "y":

                print(
                    "You take the chainmail and the iron blade that comes with it."
                )

                armour.append("Chainmail")
                weapons.append("Iron Blade")

                if "Leather Tunic Set" in armour:
                    armour.remove("Leather Tunic Set")

                if "Stone Sword" in weapons:
                    weapons.remove("Stone Sword")

                # Apply equipment bonuses
                player.damage_bonus = 10
                player.absorption = 0.25

                print(
                    "You feel stronger with the iron blade (+10 damage) "
                    "and more protected with the chainmail "
                    "(25% damage absorption)."
                )

                break

            elif choice_4 == "n":

                print("You leave the chainmail and iron blade.")
                break

            else:
                print("Invalid input. Please choose y or n.")

        print(
            "You venture up the stairs to find a hallway with a door at the end.\n"
        )

        time.sleep(3)

        print(
            "You open the door and enter a dark room with a chest in the centre. "
            "You open it and find nothing."
        )

        time.sleep(4)

        print("Suddenly you hear a rumble beneath you.")
        time.sleep(3)

        print("You hear the clanking of bones to the left of you.")
        print("A skeleton emerges from the shadows!")

        time.sleep(3)

        while True:

            choice_5 = input("Press 1 to fight or 2 to run: ")

            if choice_5 == "1":

                skeleton_combat()
                break

            elif choice_5 == "2":

                print("You try to run, but the door is locked!")
                time.sleep(3)

                print("You have to fight!")

                skeleton_combat()
                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print(
            "You go on with your journey and go up into the castle "
            "using the passage the skeleton came from."
        )

        choice_6 = menu()

        if choice_6 == "1":

            print(
                "You follow the dark corridor into a dead end. "
                "You see a button. You look around and see a key hole "
                "with red lining around it."
            )

            time.sleep(5)

            print("You have no other way. You press the button.")
            time.sleep(3)

            for _ in range(50):
                print(random.choice(random_characters), end="")

            print()
            time.sleep(2)

            print(
                "You fall into what seems a basement.\n"
                "You see better now."
            )

            time.sleep(4)

            print(
                "You keep walking into the dimly lit corridor.\n"
                "Suddenly you hear a screech."
            )

            time.sleep(3)

            print(
                "You see a blue figurine in the distance hovering with "
                "a mysterious item in its small hands.\n"
                "It's a blue minion."
            )

            time.sleep(4)

            print(
                "You don't know it yet but you brush it off as a bat. "
                "You try to feel the walls around you.\n"
                "Until a glimpse of the mysterious item catches your eye."
            )

            time.sleep(5)

            print(
                "You try to reach for it but the minion runs off.\n"
                "You chase it into the abyss, desperate to get your hands on it."
            )

            time.sleep(4)

            print(
                "It's a key. A blue key.\n"
                "You try to get your hands on it but the minion screeches "
                "and hits you with its claws."
            )

            damage_taken = minion.damage * (1 - player.absorption)
            player.health -= damage_taken

            print(f"You took {damage_taken} damage!")
            print(f"Health: {player.health}\n")

            if player.health <= 0:
                print("You died!")
                time.sleep(3)
                exit()

            minion_combat()

            print(
                "You get the blue key and keep wandering down the corridor.\n"
                "Suddenly you step on what seems to be a pressure plate."
            )

            time.sleep(4)

            print(
                "The walls rumble and you feel them pushing against your "
                "outstretched palms.\n"
                "The walls are getting closer!"
            )

            time.sleep(3)

            print(
                "You run as fast as you can and slam into a wall.\n"
                "You see 10 key holes, all black.\n"
                "Only 1 can save you.\n"
            )

            time.sleep(4)

            print(
                "You try 1 lock after another as fast as you can, "
                "frantically searching for the one that works."
            )

            time.sleep(3)

            print("You try the 5th lock and it works!")

            time.sleep(2)

            print(
                "The walls stop moving just as they were going to crush you "
                "and you fall past the key hole wall and land face first "
                "in a dusty room."
            )

            time.sleep(5)

        elif choice_6 == "2":

            print("You rest and recover.")

            if player.health == 100:
                print(f"Health: {player.health}\n")

            elif player.health < 100:

                player.health += 25

                if player.health > 100:
                    player.health = 100

                print(f"Health: {player.health}\n")
                time.sleep(3)

        elif choice_6 == "3":

            print("Thanks for playing! Exiting...")
            time.sleep(4)
            exit()

    elif choice_3 == "2":

        print("You rest and recover.")

        if player.health == 100:
            print(f"Health: {player.health}\n")

        elif player.health < 100:

            player.health += 25

            if player.health > 100:
                player.health = 100

            print(f"Health: {player.health}\n")
            time.sleep(3)

    elif choice_3 == "3":

        print("Thanks for playing! Exiting...")
        time.sleep(4)
        exit()


def scene_3():

    all_choice()
    time.sleep(4)

    print("--------------------")

    choice_7 = menu()

    if choice_7 == "1":

        print(
            "You lift yourself up from the floor and are greeted by "
            "the presence of light and what seems to be a miracle."
        )

        time.sleep(4)

        print(
            "You look around to see a beautiful bed and a table "
            "with a glass of water on it."
        )

        time.sleep(3)

        print(
            "To your right you see an armour stand with a sword being held "
            "up by a clear holder sitting on a shelf under a window."
        )

        time.sleep(3.5)

        print(
            "You look around in awe and set your gaze upon a book "
            "on the other side of the table."
        )

        time.sleep(5)

        print(
            f"WELCOME {player.name}! You may rest here for a couple days. "
            "You'll have everything you need here.\n"
            "If you need anything just ask the gnome behind you."
        )

        time.sleep(4)

        print(
            "You turn around and see the gnome from earlier still smoking "
            "the pipe.\n"
            "You look out the window and see nothing but the seemingly "
            "endless grass plains and the creepy gaze of the moon above."
        )

        time.sleep(5)

        print(
            "You stay for a couple days, although it's never day here. "
            "You feel refreshed and ready to continue your journey."
        )

        time.sleep(3)

        print(
            "You look at the room one last time and sip your last cup of water "
            "after having your lunch of mysterious mushrooms and exotic berries."
        )

        time.sleep(3)

        print(
            "You pick up the diamond armour and sword and begin to head "
            "to the spiral stairs."
        )

        if "Chainmail" in armour:
            armour.remove("Chainmail")

        if "Iron Blade" in weapons:
            weapons.remove("Iron Blade")

        armour.append("Diamond Set")
        weapons.append("Diamond Blade")

        player.damage_bonus = 25
        player.absorption = 0.50

        print(
            "You feel stronger with the Diamond Blade (+25 damage) "
            "and more protected with the Diamond Set (50% damage absorption)."
        )

        time.sleep(4)

        print(
            "You are about to approach the spiral stairs until the gnome "
            "stops you.\n"
            "He asks you to choose a potion in a raspy but calm voice."
        )

        while True:

            choice_8 = input(
                "Choose a potion to drink for its permanent effects:\n"
                "1. Absorption Potion (+10% damage absorption)\n"
                "2. Damage Potion (+30 damage)\n"
                "> "
            )

            if choice_8 == "1":

                player.absorption = 0.60

                print(
                    "You feel more protected with the Absorption Potion "
                    "(+10% damage absorption)."
                )

                time.sleep(3)
                break

            elif choice_8 == "2":

                player.damage_bonus = 55

                print(
                    "You feel stronger with the Damage Potion (+30 damage)."
                )

                time.sleep(3)
                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print(
            "You say thanks to the gnome and head to the spiral stairs, "
            "taking the book with you.\n"
            "Your stay brought you back up to full health."
        )

        player.health = 100

        time.sleep(3)

        print(
            "You climb for what feels like forever.\n"
            "Your legs ache but you are filled with determination."
        )

        time.sleep(3)

        print("You reach the top of the stairs and finally see something.")

        time.sleep(2)

        print(
            "It's an extremely tall room with what seems to be a mountain inside it."
        )

        time.sleep(3)

        print(
            "You don't think much of it and head towards it.\n"
            "However, something catches your eye and you see a skeleton."
        )

        time.sleep(4)

        print(
            "Not one that you have fought before. It looks almost human."
        )

        time.sleep(3)

        print(
            "You see a note where its eye was supposed to be.\n"
            "BEWAR3 0F TH3 T1T@N"
        )

        time.sleep(4)

        print(
            "You look around the room and see a small red exit door\n"
            "around the mountain."
        )

        while True:

            choice_9 = input(
                "1. Do you run to the door to get out of there as quick as you can?\n"
                "2. Do you carefully sneak around and try to find something?\n"
                "> "
            )

            if choice_9 == "1":

                print(
                    "You try to run but you hear the ground beneath you shake "
                    "and a boulder blocks the door. There was not a mountain "
                    "in this room.\n"
                    "It was a Titan."
                )

                time.sleep(6)

                print(
                    "The Titan rises from the ground, blocking your path!"
                )

                time.sleep(3)

                titan_combat()
                break

            elif choice_9 == "2":

                print(
                    "You wander around and see nothing. You quietly head "
                    "towards the red door and manage to get through.\n"
                    "You see a note saying you survived the Titan.\n"
                    "Then you realise..."
                )

                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print("You make it past the Titan and escape the dungeon.")

        time.sleep(3)

        print(
            "You manage to escape the room and move on trying to find a way out.\n"
            "You reach the end of another staircase. Another bedroom waits there for you."
        )

        time.sleep(3)

        print("It's not nearly as nice as the last one.")

        time.sleep(3)

        while True:

            choice_10 = menu()

            if choice_10 == "1":

                print("You explore the room and find nothing of interest.")

                time.sleep(3)

                print(
                    "You remember the red key hole from a few rooms before.\n"
                    "You wonder what it is."
                )

                time.sleep(2)

                print(
                    "You head towards the exit door and open it.\n"
                    "CLANK HEHEHEEEHE SCREEACSH"
                )

                time.sleep(3)

                print("All 3 of your past enemies are here!\nYou have to fight!")

                skeleton_combat()

                time.sleep(3)

                minion_combat()

                time.sleep(3)

                goblin_combat()

                time.sleep(3)

                print("Congrats! Here is a health potion. Drink it!")

                choice_11 = input(
                    "Do you want to drink it? (y/n): "
                ).strip().lower()

                print(f"{player.name} has {player.health} health!")

                if choice_11 == "y":

                    player.health = 100

                    print(f"Health: {player.health}\n")
                    break

                elif choice_11 == "n":

                    print("You decide not to drink it.")
                    break

                else:

                    print("Invalid input. You leave the potion.")

                    break

            elif choice_10 == "2":

                print("You rest and recover.")

                if player.health == 100:
                    print(f"Health: {player.health}\n")

                elif player.health < 100:

                    player.health += 25

                    if player.health > 100:
                        player.health = 100

                    print(f"Health: {player.health}\n")

                time.sleep(3)

            elif choice_10 == "3":

                print("Thanks for playing! Exiting...")
                time.sleep(4)
                exit()

            else:
                print("Invalid input. Please choose 1, 2, or 3.")

    elif choice_7 == "2":

        print("You rest and recover.")

        if player.health == 100:
            print(f"Health: {player.health}\n")

        elif player.health < 100:

            player.health += 25

            if player.health > 100:
                player.health = 100

            print(f"Health: {player.health}\n")

            time.sleep(3)

    elif choice_7 == "3":

        print("Thanks for playing! Exiting...")
        time.sleep(4)
        exit()

    else:

        print("Invalid input. Please choose 1, 2, or 3.")


def scene_4():

    all_choice()

    print("-------------------")

    while True:

        choice_12 = menu()

        if choice_12 == "1":

            print(
                "You make it past everything. You get greeted by yet another "
                "room with an abundance of moonlight.\n"
                "You begin to get tired of rooms."
            )

            time.sleep(3)

            print(
                "You see a beam of light being focused on a mysterious mushroom.\n"
                "You hear the door behind you slam shut.\n"
                "You run back and try to open it.\n"
                "It's no use."
            )

            time.sleep(6)

            print(
                "You sense something pulsing in your pocket. It's the book.\n"
                "You open it. It reads; Y0U H@V3 TO EAT TH3 MUSHRO0M TO CONTINUE."
            )

            time.sleep(6)

            print(
                "You eat the mushroom. You feel a surge of dizziness and fall.\n"
                "You wake up to see that you're falling in some kind of portal.\n"
                "The woman's voice intensifies."
            )

            time.sleep(4)

            print(
                "You see a surge of bright light near the end of your fall.\n"
                "The book flies out your pocket and opens to pages that "
                "don't read in your head."
            )

            for _ in range(100):
                print(random.choice(random_characters), end="")

            print()

            time.sleep(4)

            print("You pass out from the intense light.")

            time.sleep(4)

            print(
                "You wake to the sound of the book flapping pages.\n"
                "You try to pick it up, but it doesn't let you."
            )

            time.sleep(4)

            print(
                "You see the red key.\n"
                "Hanging right above you.\n"
                "You feel the need to grab it."
            )

            time.sleep(3)

            print(
                "You grab it and fall. You fall, fall, fall and fall. "
                "You begin to think about what even are you, why do you "
                "bother doing anything. Why not enjoy the peace of the room "
                "with anything you want?"
            )

            time.sleep(8)

            print(
                "You don't know who you are or where, but you are filled "
                "with determination.\n"
                "To find out what is this place and why it's riddled "
                "with evil but calmness."
            )

            time.sleep(5)

            print(
                "You land.\n"
                "It's the same room with the red key hole you were in. "
                "You force it in."
            )

            time.sleep(3)

            print(
                "You end up in an open field. The sun is out. This is the "
                "first time you've seen it in weeks. In front of you stands "
                "armour that you've never seen before."
            )

            time.sleep(4)

            print(
                "The book rises behind the armour.\n"
                "B3H0LD THE M00N ARMOUR @ND TH3 SUN BL@D3"
            )

            print("You take the armour.")

            if "Diamond Set" in armour:
                armour.remove("Diamond Set")

            if "Diamond Blade" in weapons:
                weapons.remove("Diamond Blade")

            armour.append("Moon Armour")
            weapons.append("Sun Blade")

            player.damage_bonus = 25
            player.absorption = 0.60

            time.sleep(4)

            print(
                "The book flaps to a page. RESTORE OUR LIGHT"
            )

            time.sleep(2.5)

            print("You get teleported to the top of the castle.")

            print(
                "The gnome stands with you. He offers you the pipe. "
                "You smoke it."
            )

            time.sleep(3)

            print(
                "You hear the flap of wings in front of you. "
                "A massive figure flies in front of you."
            )

            print(
                "It gets closer. It's a dragon. It has a glowing orb "
                "in its chest. It looks like a sun."
            )

            time.sleep(3)

            print("The Dragon attacks!")

            dragon_combat()

            print(
                "The sun drops onto the floor waiting for someone or "
                "something to pick it up. You lunge to get it but are "
                "stopped in your tracks."
            )

            print("All of the evil forces are trying to reclaim it.")

            time.sleep(4)

            print(
                "The book throws you a potion you've never seen before.\n"
                "You drink it."
            )

            time.sleep(4.5)

            player.health = 300

            print(f"Health: {player.health}\n")

            time.sleep(3)

            print("GET READY")

            time.sleep(6)

            skeleton_combat()
            goblin_combat()
            minion_combat()
            skeleton_combat()
            minion_combat()
            minion_combat()
            goblin_combat()
            titan_combat()
            titan_combat()
            goblin_combat()

            # Final battle is complete
            break

        elif choice_12 == "2":

            print("You rest and recover.")

            if player.health == 100:
                print(f"Health: {player.health}\n")

            elif player.health < 100:

                player.health += 25

                if player.health > 100:
                    player.health = 100

            print(f"Health: {player.health}\n")
            time.sleep(3)

            continue

        elif choice_12 == "3":

            print("Thanks for playing! Exiting...")
            time.sleep(4)
            exit()

        else:

            print("Invalid input!")
            continue


def end_message():

    print(
        """The final monster fell, and for the first time in centuries, the world was silent.

The darkness that had swallowed kingdoms began to fade. Across the ruined lands, the people looked towards the sky as a single ray of light broke through the endless clouds. The evil that had controlled them was gone. Chains were broken, kingdoms were freed, and the creatures that had haunted the world were no more.

But the hero stood alone among the ruins, watching the light return.

They had fought through darkness so that others would never have to.

And as the sun finally rose over the broken world, a new age began.

The darkness was defeated.

The light had returned.

And the world was free.
"""
    )


def main():

    scene_1()
    scene_2()
    scene_3()
    scene_4()

    end_message()

    completion_time = time.time() - start_time

    print(f"Well Done {player.name}! You win.")
    print(f"Your time was: {completion_time:.2f} seconds!")


main()