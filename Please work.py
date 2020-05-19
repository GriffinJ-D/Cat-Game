import random
from student import Cat
import time
from student import Bird
from student import Attack
Cat1 = Cat("Tomithy", 1, 10, 36, 70, 4, 70, 0)
Cat2 = Cat("Harley", 1, 16, 12, 87, 2.5, 87, 0)
Cat3 = Cat("Thumbs", 1, 7, 10, 53, 3, 53, 0)
Cat4 = Cat("Gloria", 1, 13, 28, 90, 2.5, 90, 0)
Cat5 = Cat("Big Chungus", 1, 26, 42, 100, 2, 100, 0)
Bird1 = Bird(1, 0.2, 3.5, 12)
Bird2 = Bird(2, 0.4, 6, 26)
Bird3 = Bird(1, 0.3, 3.2, 18)
bird_time = 0
deadcat = False
attack1 = Attack("SWIPE", 0.4)
attack2 = Attack("BITE", 0.3)
attack3 = Attack("SCRATCH", 0.5)
attack4 = Attack("SUPER SCRATCH", 0.9)
attack5 = Attack("VENOMOUS BITE", 1.0)
attack6 = Attack("MEGA! ULTRA! SCRATCH!", 1.60)
bruh = "."
attack_set = ["SWIPE", "BITE", "SCRATCH"]
power_set = [0.4, 0.3, 0.5]

# I wrote this

def learn_move(Move_name, Power):
    choice1 = input("Your cat wants to learn " + Move_name + ", do you want to forget an attack and learn " + Move_name + "? Enter yes or no.")
    while choice1.lower() == "yes":
        please = input("You currently know " + str(attack_set) + ". Which attack should you forget in place of " + attack4.name)
        if please.upper() in attack_set:
            for attack in range(len(attack_set)):
                if please.upper() == attack_set[attack]:
                    attack_set[attack] = Move_name
                    power_set[attack] = Power
                    print("You learned " + Move_name + "!\nYou currently know" + str(attack_set))
                    choice1 = "nah"
        else:
            choice1 = input("Do you still want to learn SUPER SCRATCH?")

def level_up(cat):
    if cat.XP > 100:
        cat.level += 1
        cat.attack += 3
        cat.health += 3
        cat.speed += 0.5
        cat.current_health += 3
        cat.XP -= 100
        print("LEVEL UP!\nLevel:" + str(cat.level) + " +1" + "\nWeight(lbs):" + str(round(cat.weight, 1)) + "\nAttack:" + str(
            cat.attack) + " +3" + "\nHealth:" + str(round(cat.current_health)) + "/" + str(round(
            cat.health)) + " +3" + "\nSpeed:" + str(
            cat.speed) + " +0.5" + "\nXP:" + str(cat.XP))
        if cat.level == 2:
            learn_move(attack4.name, attack4.power)
        elif cat.level == 3:
            learn_move(attack5.name, attack5.power)
        elif cat.level == 4:
            learn_move(attack6.name, attack6.power)

def restore_hp(cat):
    while cat.current_health < cat.health:
        cat.current_health += 1
    print("Health:" + str(cat.current_health) + "/" + str(cat.health))

def nap(cat):
    while cat.current_health < cat.health:
        cat.current_health += 1
        print("Health:" + str(cat.current_health) + "/" + str(cat.health))
        time.sleep(1)
    print("a few hours later...")

def take_meds(cat):
    print("Your owner is making you take medicine. How do you react?")
    for period in "...":
        print(period)
        time.sleep(1)
    before = time.time()
    meds = input("React fast!:")
    after = time.time()
    if meds.upper() == "SWIPE" and before + 1.5 > after:
        print("OWW! You fucking scratched me! Now my hand is bleeding... really " + cat.name + "? wtf...")
        restore_hp(cat)
    elif meds.upper() == "BITE" and before + 1.5 > after:
        print("OWW! You fucking bit me! Now my hand is bleeding... really " + cat.name + "? wtf...")
        restore_hp(cat)
    elif meds.upper() == "SCRATCH" and before + 1.5 > after:
        print("OWW! You fucking scratched me! Now my hand is bleeding... really " + cat.name + "? wtf...")
        restore_hp(cat)
    else:
        print("See that wasn't so bad huh?")
        restore_hp(cat)

def stats(cat):
    print("\nLevel:" + str(cat.level) + "\nWeight(lbs):" + str(round(cat.weight, 1)) + "\nAttack:" + str(
        cat.attack) + "\nHealth:" + str(round(cat.current_health, 1)) + "/" + str(round(cat.health, 1)) + "\nSpeed:" + str(
        cat.speed) + "\nXP:" + str(cat.XP))

def sharpen_claws(cat):
    cat.attack += 2
    print(" +2 attack")

def bird_catching(cat, bird):
    sneak = random.randint(0, 2)
    while sneak != 1:
        before = time.time()
        birdguess = input("Type: SNEAK")
        after = time.time()
        if birdguess.upper() == "SNEAK" and before + 2.5 > after:
            sneak = random.randint(0, 2)
            print("Sneaky...")
        else:
            print("The bird noticed you and flew off...")
            break
    if sneak == 1:
        before = time.time()
        birdguess = input("Type: POUNCE")
        after = time.time()
        if birdguess.upper() == "POUNCE" and cat.speed > bird.speed and before + cat.speed > after:
            print("You're Quick! Nice catch!\n+XP\n+weight")
            cat.XP += bird.XP
            cat.weight += bird.weight
            level_up(cat)
        elif birdguess.upper() == "POUNCE" and cat.speed < bird.speed and before + 2 > after:
            print("You're Quick! Nice catch!\n+XP\n+weight")
            cat.XP += bird.XP
            cat.weight += bird.weight
            level_up(cat)
        else:
            print("Too slow")

def good_attack(cat1, cat2, multiplier):
    power = cat1.attack * multiplier
    cat2.current_health -= power
    print("damn that cat got messed up.")
    print("Enemy cats health:" + str(round(cat2.current_health)) + "/" + str(round(cat2.health)))
    cat1.current_health -= 3
    print("Your cats health:" + str(round(cat1.current_health)) + "/" + str(round(cat1.health)))

def missed_attack(cat1, cat2, multiplier):
    power = cat2.attack * multiplier
    cat1.current_health -= power
    print("Damn your cat got messed up." + "\nYour cats health:" + str(round(cat1.current_health)) + "/" + str(round(
        cat1.health)))

def opponent_died(cat1):
    print("Good job defending your turf\n+XP")
    cat1.XP += 68
    level_up(cat1)

def cat_fight(cat1, cat2):
    choice = int(input("Fight for turf(1)? Or run away(2)?"))
    if choice == 2:
        print("You got away safely")
    while choice == 1 and cat1.current_health > 0 and cat2.current_health > 0:
        input("Press enter when you're ready, then type your attack or type 'run' as fast as you can.")
        attack = random.randint(0, 2)
        if attack == 0:
            before = time.time()
            user_attack = input("Type: " + attack_set[0])
            after = time.time()
            if user_attack.upper() == attack_set[0] and before + cat1.speed > after:
                good_attack(cat1, cat2, power_set[0])
                if cat2.current_health <= 0:
                    print("You just took down " + cat2.name + "!")
                    opponent_died(cat1)
                    while cat2.current_health < cat2.health:
                        cat2.current_health += 1
                    break
            elif user_attack.upper() == "RUN" and before + cat1.speed > after:
                print("You got away safely...")
                break
            else:
                missed_attack(cat1, cat2, 0.5)
        elif attack == 1:
            before = time.time()
            user_attack = input("Type: " + attack_set[1])
            after = time.time()
            if user_attack.upper() == attack_set[1] and before + cat1.speed > after:
                good_attack(cat1, cat2, power_set[1])
                if cat2.current_health <= 0:
                    print("You just took down " + cat2.name + "!")
                    opponent_died(cat1)
                    while cat2.current_health < cat2.health:
                        cat2.current_health += 1
                    break
            elif user_attack.upper() == "RUN" and before + cat1.speed > after:
                print("You got away safely...")
                break
            else:
                missed_attack(cat1, cat2, 0.5)
        else:
            before = time.time()
            user_attack = input("Type: " + attack_set[2])
            after = time.time()
            if user_attack.upper() == attack_set[2] and before + cat1.speed > after:
                good_attack(cat1, cat2, power_set[2])
                if cat2.current_health <= 0:
                    print("You just took down " + cat2.name + "!")
                    opponent_died(cat1)
                    while cat2.current_health < cat2.health:
                        cat2.current_health += 1
                    break
            elif user_attack.upper() == "RUN" and before + cat1.speed > after:
                print("You got away safely...")
                break
            else:
                missed_attack(cat1, cat2, 0.5)

def run_game(yours, other1, other2, other3, other4):
    if yours.current_health < (0.3 * yours.health):
        take_meds(yours)
    choice = input("alright, now what? nap, sharpen claws, roam? Or check stats?")
    if choice.upper() == "SHARPEN CLAWS":
        sharpen_claws(yours)
    elif choice.upper() == "STATS":
        stats(yours)
    elif choice.upper() == "NAP":
        nap(yours)
    elif choice.upper() == "ROAM":
        number = random.randint(0, 2)
        if number == 0:
            number1 = random.randint(0, 2)
            if number1 == 0:
                print("you encountered a level " + str(Bird1.level) + " bird!")
                for period in "...":
                    print(period)
                    time.sleep(1)
                bird_catching(yours, Bird1)
            if number1 == 1:
                print("you encountered a level " + str(Bird2.level) + " bird!")
                for period in "...":
                    print(period)
                    time.sleep(1)
                bird_catching(yours, Bird2)
            if number1 == 2:
                print("you encountered a level " + str(Bird3.level) + " bird!")
                for period in "...":
                    print(period)
                    time.sleep(1)
                bird_catching(yours, Bird3)
        elif number == 1:
            print("unrecognised cat approaching!")
            opponent = random.randint(0, 3)
            if opponent == 0:
                cat_fight(yours, other1)
            elif opponent == 1:
                cat_fight(yours, other2)
            elif opponent == 2:
                cat_fight(yours, other3)
            else:
                cat_fight(yours, other4)
        else:
            print("nothing interesting today")

yourcat = input("Choose your cat:\n Tomithy, Harley, Thumbs, Gloria, or Big Chungus?")

if yourcat.upper() == Cat1.name.upper():
    stats(Cat1)
elif yourcat.upper() == Cat2.name.upper():
    stats(Cat2)
elif yourcat.upper() == Cat3.name.upper():
    stats(Cat3)
elif yourcat.upper() == Cat4.name.upper():
    stats(Cat4)
elif yourcat.upper() == Cat5.name.upper():
    stats(Cat5)
else:
    print("Not a valid cat")

while yourcat.upper() == Cat1.name.upper() and Cat1.current_health > 0:
    run_game(Cat1, Cat2, Cat3, Cat4, Cat5)
while yourcat.upper() == Cat2.name.upper() and Cat2.current_health > 0:
    run_game(Cat2, Cat1, Cat3, Cat4, Cat5)
while yourcat.upper() == Cat3.name.upper() and Cat3.current_health > 0:
    run_game(Cat3, Cat2, Cat1, Cat4, Cat5)
while yourcat.upper() == Cat4.name.upper() and Cat4.current_health > 0:
    run_game(Cat4, Cat2, Cat3, Cat1, Cat5)
while yourcat.upper() == Cat5.name.upper() and Cat5.current_health > 0:
    run_game(Cat5, Cat2, Cat3, Cat4, Cat1)
print("you died")
