
import random
import os
import platform
from hero import Hero
from monster import Monster
from functions import get_valid_input, save_game, load_game, collect_loot, use_loot, inception_dream, adjust_combat_strength

# Display OS and Python version
print(f"Operating System: {os.name}")
print(f"Python Version: {platform.python_version()}")

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Initialize Hero and Monster
hero = Hero()
monster = Monster()

# Adjust combat strength based on last game
adjust_combat_strength(hero, monster)

# Roll for weapon
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")
ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
print(ascii_image5)

weapon_roll = get_valid_input("Enter a number between 1 and 6 for your weapon roll (or 0 for auto-roll): ", 0, 6)
if weapon_roll == 0:
    weapon_roll = random.choice(range(1, 7))

# Limit the combat strength to 6
hero.combat_strength = min(6, hero.combat_strength + weapon_roll)
print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

# Weapon Roll Analysis
if weapon_roll <= 2:
    print("--- You rolled a weak weapon, friend")
elif weapon_roll <= 4:
    print("--- Your weapon is meh")
else:
    print("--- Nice weapon, friend!")

if weapons[weapon_roll - 1] != "Fist":
    print("    |    --- Thank goodness you didn't roll the Fist...")

# Roll for player health points
print("    |", end="    ")
input("Roll the dice for your health points (Press enter)")
hero.health_points = random.choice(range(1, 21))
print(f"    |    Player rolled {hero.health_points} health points")

# Roll for monster health points
print("    |", end="    ")
input("Roll the dice for the monster's health points (Press enter)")
monster.health_points = random.choice(range(1, 21))
print(f"    |    Monster rolled {monster.health_points} health points")

# Collect Loot
print("    ------------------------------------------------------------------")
print("    |    !!You find a loot bag!! You look inside to find 2 items:")
print("    |", end="    ")
input("Roll for first item (Press enter)")

# Collect Loot First time
loot_options, belt = collect_loot(loot_options, belt)

print("    ------------------------------------------------------------------")
print("    |", end="    ")
input("Roll for second item (Press enter)")

# Collect Loot Second time
loot_options, belt = collect_loot(loot_options, belt)

print("    |    You're super neat, so you organize your belt alphabetically:")
belt.sort()
print("    |    Your belt: ", belt)

# Use Loot
belt, hero.health_points = use_loot(belt, hero.health_points)

# Roll for the monster's power
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                
                                      """
print(ascii_image4)

power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
monster.combat_strength += min(6, monster.combat_strength + monster_powers[power_roll])
print(f"    |    The monster's combat strength is now {monster.combat_strength} using the {power_roll} magic power")

# Recursive dream sequence
num_dream_lvls = get_valid_input("How many dream levels do you want to go down? (0-3): ", 0, 3)
if num_dream_lvls > 0:
    hero.health_points -= 1
    crazy_level = inception_dream(num_dream_lvls)  # Pass the number of dream levels
    hero.combat_strength += crazy_level
    print(f"combat strength: {hero.combat_strength}")
    print(f"health points: {hero.health_points}")

# Fight Sequence
print("    ------------------------------------------------------------------")
print("    |    You meet the monster. FIGHT!!")
while hero.health_points > 0 and monster.health_points > 0:
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(range(1, 7))
    if attack_roll % 2 != 0:
        input("You strike (Press enter)")
        hero.hero_attacks(monster)  # No return assignment here
    else:
        input("The Monster strikes (Press enter)")
        monster.monster_attacks(hero)  # No return assignment here

# Determine winner
if monster.health_points <= 0:
    winner = "Hero"
    num_stars = 3
else:
    winner = "Monster"
    num_stars = 1

# Display Final Score
hero_name = input("Enter your Hero's name: ")
short_name = hero_name[:2].upper()
print(f"    |    Hero {short_name} gets {'*' * num_stars} stars")

# Save Game
save_game(winner, hero_name=short_name, num_stars=num_stars)
