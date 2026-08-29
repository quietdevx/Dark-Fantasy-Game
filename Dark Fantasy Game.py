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


# =========================
# GAME INTRO
# =========================

print("Dark Fantasy\nExplore the world!")

player_name = input("Create a name\n> ")

time.sleep(2)

print(f"\nHello {player_name}!\nGenerating world...\n")

time.sleep(3)


# =========================
# CLASSES
# =========================

class Player:
    def __init__(self, name):
        self.health = 100
        self.damage = 20
        self.name = name
        self.damage_bonus = 0
        self.absorption = 0


class Goblin:
    def __init__(self):
        self.health = 50
        self.damage = 10


class Skeleton:
    def __init__(self):
        self.health = 75
        self.damage = 15


class Titan:
    def __init__(self):
        self.health = 400
        self.damage = 60


class Minion:
    def __init__(self):
        self.health = 30
        self.damage = 10


class Dragon:
    def __init__(self):
        self.health = 1000
        self.damage = 100
        self.damage_bonus_special_attack = 25


player = Player(player_name)

goblin = Goblin()
skeleton = Skeleton()
titan = Titan()
minion = Minion()
dragon = Dragon()


# =========================
# MENUS
# =========================

def menu():
    while True:
        print("\n1. Explore")
        print("2. Rest")
        print("3. Quit")

        choice = input("> ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


def all_choice():
    while True:
        print("\n1. View armour.")
        print("2. View weapons.")
        print("3. View Health.")
        print("4. View Stats")
        print("5. Continue.")

        choice = input("> ")

        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid input. Please choose 1, 2, 3, 4, or 5.")


# =========================
# HELPER FUNCTIONS
# =========================

def rest():
    print("\nYou rest and recover.")

    if player.health < 100:
        player.health += 25

        if player.health > 100:
            player.health = 100

    print(f"Health: {player.health}")

    time.sleep(2.5)


def check_death():
    if player.health <= 0:
        print("\nYou have died!")
        time.sleep(2.5)
        print("Thanks for playing!")
        exit()


def get_player_damage():
    if "Sun Blade" in weapons:
        return player.damage + player.damage_bonus, "Sun Blade"

    elif "Diamond Blade" in weapons:
        return player.damage + player.damage_bonus, "Diamond Blade"

    elif "Iron Blade" in weapons:
        return player.damage + player.damage_bonus, "Iron Blade"

    else:
        return player.damage, None


def take_damage(enemy):
    damage_taken = enemy.damage * (1 - player.absorption)

    if "Moon Armour" in armour:
        print(
            f"\nThe enemy attacks you for {enemy.damage} damage,\n"
            f"but your Moon Armour absorbs "
            f"{enemy.damage * player.absorption:.1f} damage!"
        )

        print(f"You take {damage_taken:.1f} damage!")

    elif "Diamond Set" in armour:
        print(
            f"\nThe enemy attacks you for {enemy.damage} damage,\n"
            f"but your Diamond Set absorbs "
            f"{enemy.damage * player.absorption:.1f} damage!"
        )

        print(f"You take {damage_taken:.1f} damage!")

    elif "Chainmail" in armour:
        print(
            f"\nThe enemy attacks you for {enemy.damage} damage,\n"
            f"but your Chainmail absorbs "
            f"{enemy.damage * player.absorption:.1f} damage!"
        )

        print(f"You take {damage_taken:.1f} damage!")

    else:
        print(f"\nThe enemy attacks you for {enemy.damage} damage!")

    player.health -= damage_taken


def player_attack(enemy, enemy_name):
    while True:
        choice = input("\nPress 1 to attack!\n> ")

        if choice == "1":
            damage, weapon = get_player_damage()

            print(f"\nYou attack the {enemy_name}!")

            if weapon:
                print(f"You deal {damage} damage with your {weapon}!")
            else:
                print(f"You deal {damage} damage!")

            enemy.health -= damage

            time.sleep(2.5)

            print(f"{enemy_name} health: {max(0, enemy.health)}")

            return

        else:
            print("Invalid input. Please press 1 to attack.")


# =========================
# COMBAT
# =========================

def combat(enemy, enemy_name, hit_chance=10):
    enemy.health = {
        "Goblin": 50,
        "Skeleton": 75,
        "Titan": 400,
        "Minion": 30,
        "Dragon": 1000
    }[enemy_name]

    print(f"\nYou fight the {enemy_name}!")
    time.sleep(2.5)

    while player.health > 0 and enemy.health > 0:

        # ENEMY TURN
        enemy_attack = random.randint(1, 10)

        if enemy_attack <= hit_chance:
            take_damage(enemy)
            time.sleep(2.5)

            check_death()

        else:
            print(f"\nThe {enemy_name} misses you!")
            time.sleep(2.5)

        # Check if enemy somehow died
        if enemy.health <= 0:
            break

        # PLAYER TURN
        player_attack(enemy, enemy_name)

        # Special Minion hit chance
        if enemy_name == "Minion":
            # Undo the normal attack and handle the minion's 20% chance
            pass

        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy_name}!")
            stats.append(f"{enemy_name} defeated")
            time.sleep(2.5)
            break

        print(f"\nHealth: {player.health}")
        time.sleep(2.5)


def goblin_combat():
    combat(goblin, "Goblin", 5)


def skeleton_combat():
    combat(skeleton, "Skeleton", 5)


def titan_combat():
    combat(titan, "Titan", 5)


def minion_combat():
    print("\nYou fight the Minion!")

    minion.health = 30

    time.sleep(2.5)

    while player.health > 0 and minion.health > 0:

        # MINION TURN
        minion_attack = random.randint(1, 10)

        if minion_attack <= 5:
            take_damage(minion)
            time.sleep(2.5)

            check_death()

        else:
            print("\nThe Minion misses you!")
            time.sleep(2.5)

        if minion.health <= 0:
            break

        # PLAYER TURN
        while True:
            player_attack_input = input(
                "\nPress 1 to attack!\n> "
            )

            if player_attack_input == "1":

                # 20% chance to hit
                hit_chance = random.randint(1, 10)

                if hit_chance <= 2:
                    damage, weapon = get_player_damage()

                    print("\nYou attack the Minion!")

                    if weapon:
                        print(
                            f"You deal {damage} damage "
                            f"with your {weapon}!"
                        )
                    else:
                        print(f"You deal {damage} damage!")

                    minion.health -= damage

                    time.sleep(2.5)

                    print(
                        f"Minion health: "
                        f"{max(0, minion.health)}"
                    )

                    break

                else:
                    print(
                        "\nYou swing at the Minion but miss!\n"
                        "It's too small to hit consistently!"
                    )

                    time.sleep(2.5)

                    # Miss still counts as the player's turn
                    break

            else:
                print(
                    "Invalid input. Please press 1 to attack."
                )

        if minion.health <= 0:
            print("\nYou defeated the Minion!")
            stats.append("Minion defeated")
            time.sleep(2.5)
            break

        print(f"\nHealth: {player.health}")
        time.sleep(2.5)


def dragon_combat():
    combat(dragon, "Dragon", 7)


# =========================
# SCENE 1
# =========================

def scene_1():

    print(
        "\nYou fall into a berry shrub and land in a dark world "
        "in which everything is conscious.\n\n"
        "You don't know how you got here but everything feels calm.\n"
        "You look around.\n\n"
        "Total darkness."
    )

    time.sleep(6)

    choice_1 = menu()

    if choice_1 == "1":

        print(
            "\nYou look up at the moon. It has a face.\n"
            "It's creepy.\n\n"
            "You look around and see a towering castle on a hill.\n"
            "Everything moves.\n\n"
            "You see a small gnome smoking a pipe."
        )

        time.sleep(3)

        print(
            "\nEverything is weird, but you feel calm.\n"
            "You feel safe.\n"
            "You feel free."
        )

        time.sleep(3)

        print(
            "\nYou look down at your feet and see a leather tunic set "
            "laying next to you with a stone sword."
        )

        armour.append("Leather Tunic Set")
        weapons.append("Stone Sword")

        time.sleep(2.5)

        print(
            "\nYou start walking toward the castle and the gnome.\n"
            "You hear an eerie but soothing song of a woman singing."
        )

        time.sleep(2.5)

        print(
            "\nYou make your way up to the hill and hear a giggle "
            "from behind you."
        )

        time.sleep(4)

        print(
            "\nYou turn around and see a goblin attacking you!\n"
            "You have to react!"
        )

        while True:

            choice_2 = input(
                "\nPress 1 to fight or 2 to run:\n> "
            )

            if choice_2 == "1":
                goblin_combat()
                break

            elif choice_2 == "2":

                print("\nYou run from the goblin!")

                time.sleep(2.5)

                print(
                    "\nYou escaped him and keep climbing "
                    "from a different point."
                )

                time.sleep(2.5)

                print("\nHe disappears into the abyss.")

                break

            else:
                print("Invalid input. Please choose 1 or 2.")

    elif choice_1 == "2":
        rest()

    elif choice_1 == "3":
        exit()


# =========================
# SCENE 2
# =========================

def scene_2():

    while True:

        all_choice_1 = all_choice()

        if all_choice_1 == "1":
            print(f"\nArmour: {armour}")

        elif all_choice_1 == "2":
            print(f"\nWeapons: {weapons}")

        elif all_choice_1 == "3":
            print(f"\nHealth: {player.health}")

        elif all_choice_1 == "4":
            print(f"\nStats: {stats}")

        elif all_choice_1 == "5":
            break

    print(f"\nYour health is {player.health}")

    time.sleep(2.5)

    choice_3 = menu()

    if choice_3 == "1":

        print(
            "\nYou reach the top of the hill and enter "
            "the gates of the castle."
        )

        time.sleep(2.5)

        print(
            "\nYou see a dimly lit hallway with an armour stand "
            "to the side.\n\n"
            "It displays chainmail and an iron blade at its feet."
        )

        while True:

            choice_4 = input(
                "\nDo you take the chainmail? (y/n): "
            ).strip().lower()

            if choice_4 == "y":

                print(
                    "\nYou take the chainmail and the iron blade "
                    "that comes with it."
                )

                armour.append("Chainmail")
                weapons.append("Iron Blade")

                if "Leather Tunic Set" in armour:
                    armour.remove("Leather Tunic Set")

                if "Stone Sword" in weapons:
                    weapons.remove("Stone Sword")

                player.damage_bonus = 10
                player.absorption = 0.25

                print(
                    "\nYou feel stronger with the iron blade "
                    "(+10 damage).\n"
                    "You are more protected with the chainmail "
                    "(25% damage absorption)."
                )

                break

            elif choice_4 == "n":

                print(
                    "\nYou leave the chainmail and iron blade."
                )

                break

            else:
                print("Invalid input. Please choose y or n.")

        print(
            "\nYou venture up the stairs to find a hallway "
            "with a door at the end."
        )

        time.sleep(2.5)

        print(
            "\nYou open the door and enter a dark room with "
            "a chest in the centre.\n\n"
            "You open it and find nothing."
        )

        time.sleep(3)

        print("\nSuddenly you hear a rumble beneath you.")

        time.sleep(2)

        print("\nYou hear the clanking of bones to the left of you.")

        print("\nA skeleton emerges from the shadows!")

        time.sleep(2.5)

        while True:

            choice_5 = input(
                "\nPress 1 to fight or 2 to run:\n> "
            )

            if choice_5 == "1":

                skeleton_combat()
                break

            elif choice_5 == "2":

                print(
                    "\nYou try to run, but the door is locked!"
                )

                time.sleep(2.5)

                print("\nYou have to fight!")

                skeleton_combat()

                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print(
            "\nYou go on with your journey and go up into "
            "the castle using the passage the skeleton came from."
        )

        choice_6 = menu()

        if choice_6 == "1":

            print(
                "\nYou follow the dark corridor into a dead end.\n"
                "You see a button.\n\n"
                "You look around and see a key hole "
                "with red lining around it."
            )

            time.sleep(4)

            print("\nYou have no other way. You press the button.")

            time.sleep(2)

            for _ in range(50):
                print(random.choice(random_characters), end="")

            print()

            time.sleep(1.5)

            print(
                "\nYou fall into what seems to be a basement.\n"
                "You see better now."
            )

            time.sleep(3)

            print(
                "\nYou keep walking into the dimly lit corridor.\n"
                "Suddenly you hear a screech."
            )

            time.sleep(2.5)

            print(
                "\nYou see a blue figurine in the distance hovering "
                "with a mysterious item in its small hands.\n\n"
                "It's a blue minion."
            )

            time.sleep(3)

            print(
                "\nYou don't know it yet but you brush it off as a bat.\n"
                "You try to feel the walls around you.\n\n"
                "Until a glimpse of the mysterious item catches your eye."
            )

            time.sleep(4)

            print(
                "\nYou try to reach for it but the minion runs off.\n"
                "You chase it into the abyss, desperate to get "
                "your hands on it."
            )

            time.sleep(3)

            print(
                "\nIt's a key.\n"
                "A blue key.\n\n"
                "You try to get your hands on it but the minion "
                "screeches and hits you with its claws."
            )

            damage_taken = minion.damage * (1 - player.absorption)

            player.health -= damage_taken

            print(f"\nYou took {damage_taken:.1f} damage!")
            print(f"Health: {player.health}")

            check_death()

            minion_combat()

            print(
                "\nYou get the blue key and keep wandering down "
                "the corridor.\n\n"
                "Suddenly you step on what seems to be "
                "a pressure plate."
            )

            time.sleep(3)

            print(
                "\nThe walls rumble and you feel them pushing "
                "against your outstretched palms.\n\n"
                "The walls are getting closer!"
            )

            time.sleep(2.5)

            print(
                "\nYou run as fast as you can and slam into a wall.\n"
                "You see 10 key holes, all black.\n\n"
                "Only 1 can save you."
            )

            time.sleep(3)

            print(
                "\nYou try 1 lock after another as fast as you can,\n"
                "frantically searching for the one that works."
            )

            time.sleep(2)

            print("\nYou try the 5th lock and it works!")

            time.sleep(1.5)

            print(
                "\nThe walls stop moving just as they were going "
                "to crush you.\n\n"
                "You fall past the key hole wall and land face first "
                "in a dusty room."
            )

            time.sleep(4)

        elif choice_6 == "2":
            rest()

        elif choice_6 == "3":

            print("\nThanks for playing! Exiting...")

            time.sleep(3)

            exit()

    elif choice_3 == "2":
        rest()

    elif choice_3 == "3":

        print("\nThanks for playing! Exiting...")

        time.sleep(3)

        exit()


# =========================
# SCENE 3
# =========================

def scene_3():

    all_choice()

    time.sleep(3)

    print("\n--------------------")

    choice_7 = menu()

    if choice_7 == "1":

        print(
            "\nYou lift yourself up from the floor and are greeted "
            "by the presence of light and what seems to be a miracle."
        )

        time.sleep(3)

        print(
            "\nYou look around to see a beautiful bed and a table "
            "with a glass of water on it."
        )

        time.sleep(2.5)

        print(
            "\nTo your right you see an armour stand with a sword "
            "being held up by a clear holder sitting on a shelf "
            "under a window."
        )

        time.sleep(2.5)

        print(
            "\nYou look around in awe and set your gaze upon a book "
            "on the other side of the table."
        )

        time.sleep(4)

        print(
            f"\nWELCOME {player.name}!\n\n"
            "You may rest here for a couple days.\n"
            "You'll have everything you need here.\n\n"
            "If you need anything just ask the gnome behind you."
        )

        time.sleep(3)

        print(
            "\nYou turn around and see the gnome from earlier "
            "still smoking the pipe.\n\n"
            "You look out the window and see nothing but the "
            "seemingly endless grass plains and the creepy gaze "
            "of the moon above."
        )

        time.sleep(4)

        print(
            "\nYou stay for a couple days, although it's never day here.\n"
            "You feel refreshed and ready to continue your journey."
        )

        time.sleep(2.5)

        print(
            "\nYou look at the room one last time and sip your last "
            "cup of water after having your lunch of mysterious "
            "mushrooms and exotic berries."
        )

        time.sleep(2.5)

        print(
            "\nYou pick up the diamond armour and sword and begin "
            "to head to the spiral stairs."
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
            "\nYou feel stronger with the Diamond Blade (+25 damage)\n"
            "and more protected with the Diamond Set "
            "(50% damage absorption)."
        )

        time.sleep(3)

        print(
            "\nYou are about to approach the spiral stairs until "
            "the gnome stops you.\n\n"
            "He asks you to choose a potion in a raspy but calm voice."
        )

        while True:

            choice_8 = input(
                "\nChoose a potion to drink for its permanent effects:\n\n"
                "1. Absorption Potion (+10% damage absorption)\n"
                "2. Damage Potion (+30 damage)\n\n"
                "> "
            )

            if choice_8 == "1":

                player.absorption = 0.60

                print(
                    "\nYou feel more protected with the "
                    "Absorption Potion.\n"
                    "(+10% damage absorption)"
                )

                time.sleep(2.5)

                break

            elif choice_8 == "2":

                player.damage_bonus = 55

                print(
                    "\nYou feel stronger with the Damage Potion.\n"
                    "(+30 damage)"
                )

                time.sleep(2.5)

                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print(
            "\nYou say thanks to the gnome and head to the spiral stairs,\n"
            "taking the book with you.\n\n"
            "Your stay brought you back up to full health."
        )

        player.health = 100

        time.sleep(2.5)

        print(
            "\nYou climb for what feels like forever.\n"
            "Your legs ache but you are filled with determination."
        )

        time.sleep(2.5)

        print(
            "\nYou reach the top of the stairs and finally see something."
        )

        time.sleep(1.5)

        print(
            "\nIt's an extremely tall room with what seems to be "
            "a mountain inside it."
        )

        time.sleep(2.5)

        print(
            "\nYou don't think much of it and head towards it.\n\n"
            "However, something catches your eye and you see a skeleton."
        )

        time.sleep(3)

        print(
            "\nNot one that you have fought before.\n"
            "It looks almost human."
        )

        time.sleep(2.5)

        print(
            "\nYou see a note where its eye was supposed to be.\n"
            "BEWAR3 0F TH3 T1T@N"
        )

        time.sleep(3)

        print(
            "\nYou look around the room and see a small red exit door "
            "around the mountain."
        )

        while True:

            choice_9 = input(
                "\n1. Do you run to the door to get out of there "
                "as quick as you can?\n\n"
                "2. Do you carefully sneak around and try to "
                "find something?\n\n"
                "> "
            )

            if choice_9 == "1":

                print(
                    "\nYou try to run but you hear the ground beneath "
                    "you shake and a boulder blocks the door.\n\n"
                    "There was not a mountain in this room.\n"
                    "It was a Titan."
                )

                time.sleep(5)

                print(
                    "\nThe Titan rises from the ground, "
                    "blocking your path!"
                )

                time.sleep(2.5)

                titan_combat()

                break

            elif choice_9 == "2":

                print(
                    "\nYou wander around and see nothing.\n"
                    "You quietly head towards the red door "
                    "and manage to get through.\n\n"
                    "You see a note saying you survived the Titan.\n"
                    "Then you realise..."
                )

                break

            else:
                print("Invalid input. Please choose 1 or 2.")

        print(
            "\nYou make it past the Titan and escape the dungeon."
        )

        time.sleep(2.5)

        print(
            "\nYou manage to escape the room and move on trying "
            "to find a way out.\n\n"
            "You reach the end of another staircase.\n"
            "Another bedroom waits there for you."
        )

        time.sleep(2.5)

        print("\nIt's not nearly as nice as the last one.")

        time.sleep(2.5)

        while True:

            choice_10 = menu()

            if choice_10 == "1":

                print(
                    "\nYou explore the room and find nothing "
                    "of interest."
                )

                time.sleep(2.5)

                print(
                    "\nYou remember the red key hole from a few "
                    "rooms before.\n"
                    "You wonder what it is."
                )

                time.sleep(1.5)

                print(
                    "\nYou head towards the exit door and open it.\n\n"
                    "CLANK HEHEHEEEHE SCREEACSH"
                )

                time.sleep(2.5)

                print(
                    "\nAll 3 of your past enemies are here!\n"
                    "You have to fight!"
                )

                skeleton_combat()

                time.sleep(2)

                minion_combat()

                time.sleep(2)

                goblin_combat()

                time.sleep(2)

                print(
                    "\nCongrats!\n"
                    "Here is a health potion. Drink it!"
                )

                while True:

                    choice_11 = input(
                        "\nDo you want to drink it? (y/n): "
                    ).strip().lower()

                    if choice_11 == "y":

                        player.health = 100

                        print(
                            f"\n{player.name} drinks the potion."
                        )

                        print(
                            f"Health: {player.health}"
                        )

                        break

                    elif choice_11 == "n":

                        print(
                            "\nYou decide not to drink it."
                        )

                        break

                    else:

                        print(
                            "Invalid input. Please choose y or n."
                        )

                break

            elif choice_10 == "2":

                rest()

            elif choice_10 == "3":

                print(
                    "\nThanks for playing! Exiting..."
                )

                time.sleep(3)

                exit()

    elif choice_7 == "2":
        rest()

    elif choice_7 == "3":

        print(
            "\nThanks for playing! Exiting..."
        )

        time.sleep(3)

        exit()


# =========================
# SCENE 4
# =========================

def scene_4():

    all_choice()

    print("\n-------------------")

    while True:

        choice_12 = menu()

        if choice_12 == "1":

            print(
                "\nYou make it past everything.\n"
                "You get greeted by yet another room with "
                "an abundance of moonlight.\n\n"
                "You begin to get tired of rooms."
            )

            time.sleep(2.5)

            print(
                "\nYou see a beam of light being focused on "
                "a mysterious mushroom.\n\n"
                "You hear the door behind you slam shut.\n"
                "You run back and try to open it.\n"
                "It's no use."
            )

            time.sleep(5)

            print(
                "\nYou sense something pulsing in your pocket.\n"
                "It's the book.\n\n"
                "You open it.\n"
                "It reads:\n\n"
                "Y0U H@V3 TO EAT TH3 MUSHRO0M TO CONTINUE."
            )

            time.sleep(5)

            print(
                "\nYou eat the mushroom.\n"
                "You feel a surge of dizziness and fall.\n\n"
                "You wake up to see that you're falling "
                "in some kind of portal.\n\n"
                "The woman's voice intensifies."
            )

            time.sleep(3)

            print(
                "\nYou see a surge of bright light near the end "
                "of your fall.\n\n"
                "The book flies out your pocket and opens to pages "
                "that don't read in your head."
            )

            for _ in range(100):
                print(random.choice(random_characters), end="")

            print()

            time.sleep(3)

            print(
                "\nYou pass out from the intense light."
            )

            time.sleep(3)

            print(
                "\nYou wake to the sound of the book flapping pages.\n"
                "You try to pick it up, but it doesn't let you."
            )

            time.sleep(3)

            print(
                "\nYou see the red key.\n"
                "Hanging right above you.\n"
                "You feel the need to grab it."
            )

            time.sleep(2)

            print(
                "\nYou grab it and fall.\n"
                "You fall, fall, fall and fall.\n\n"
                "You begin to think about what even are you,\n"
                "why do you bother doing anything?\n\n"
                "Why not enjoy the peace of the room "
                "with anything you want?"
            )

            time.sleep(7)

            print(
                "\nYou don't know who you are or where,\n"
                "but you are filled with determination.\n\n"
                "To find out what this place is and why it's "
                "riddled with evil but calmness."
            )

            time.sleep(4)

            print(
                "\nYou land.\n\n"
                "It's the same room with the red key hole "
                "you were in.\n"
                "You force it in."
            )

            time.sleep(2)

            print(
                "\nYou end up in an open field.\n"
                "The sun is out.\n\n"
                "This is the first time you've seen it in weeks.\n\n"
                "In front of you stands armour that you've "
                "never seen before."
            )

            time.sleep(3)

            print(
                "\nThe book rises behind the armour.\n\n"
                "B3H0LD THE M00N ARMOUR @ND TH3 SUN BL@D3"
            )

            print("\nYou take the armour.")

            if "Diamond Set" in armour:
                armour.remove("Diamond Set")

            if "Diamond Blade" in weapons:
                weapons.remove("Diamond Blade")

            armour.append("Moon Armour")
            weapons.append("Sun Blade")

            player.damage_bonus = 25
            player.absorption = 0.60

            time.sleep(3)

            print(
                "\nThe book flaps to a page.\n"
                "RESTORE OUR LIGHT"
            )

            time.sleep(1.5)

            print(
                "\nYou get teleported to the top of the castle."
            )

            print(
                "\nThe gnome stands with you.\n"
                "He offers you the pipe.\n"
                "You smoke it."
            )

            time.sleep(2.5)

            print(
                "\nYou hear the flap of wings in front of you.\n"
                "A massive figure flies in front of you."
            )

            print(
                "\nIt gets closer.\n"
                "It's a dragon.\n\n"
                "It has a glowing orb in its chest.\n"
                "It looks like a sun."
            )

            time.sleep(2.5)

            print("\nThe Dragon attacks!")

            dragon_combat()

            print(
                "\nThe sun drops onto the floor waiting for "
                "someone or something to pick it up.\n\n"
                "You lunge to get it but are stopped in your tracks."
            )

            print(
                "\nAll of the evil forces are trying to reclaim it."
            )

            time.sleep(3)

            print(
                "\nThe book throws you a potion you've never "
                "seen before.\n"
                "You drink it."
            )

            time.sleep(3.5)

            player.health = 300

            print(f"\nHealth: {player.health}")

            time.sleep(2)

            print("\nGET READY")

            time.sleep(5)

            # FINAL BATTLE
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

            break

        elif choice_12 == "2":

            rest()

        elif choice_12 == "3":

            print(
                "\nThanks for playing! Exiting..."
            )

            time.sleep(3)

            exit()

        else:

            print("Invalid input!")


# =========================
# ENDING
# =========================

def end_message():

    print(
        """
The final monster fell, and for the first time in centuries,
the world was silent.

The darkness that had swallowed kingdoms began to fade.

Across the ruined lands, the people looked towards the sky
as a single ray of light broke through the endless clouds.

The evil that had controlled them was gone.

Chains were broken.
Kingdoms were freed.
The creatures that had haunted the world were no more.

But the hero stood alone among the ruins,
watching the light return.

They had fought through darkness so that others
would never have to.

And as the sun finally rose over the broken world,
a new age began.

The darkness was defeated.

The light had returned.

And the world was free.
"""
    )


# =========================
# MAIN
# =========================

def main():

    scene_1()
    scene_2()
    scene_3()
    scene_4()
    end_message()


# =========================
# START GAME + TIMER
# =========================

main()

completion_time = time.time() - start_time

minutes = int(completion_time // 60)
seconds = int(completion_time % 60)

print(
    f"\nYour time was: "
    f"{minutes} minutes and {seconds} seconds!"
)