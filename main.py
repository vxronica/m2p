import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 3, self.attack_power + 3) #randomizing damage
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    #adding healing magic
    def heal(self):
        heal_amount = random.randint(5, 30)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def warrior_attack(self, opponent):
        damage = random.randint(self.attack_power * 2 - 5, self.attack_power * 2 + 5)
        opponent.health -= damage
        print(f"{self.name} uses the Warrior Special Attack for {damage} damage!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        min_damage = int(self.attack_power * 1.77 - 5)
        max_damage = int(self.attack_power * 1.77 + 5)
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        print(f"{self.name} casts a special spell for {damage} damage!")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=22)

    def quick_shot(self, opponent):
        min_damage = int(self.attack_power * 1.75 - 5)
        max_damage = int(self.attack_power * 1.75 + 5)
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def evade(self):
        print(f"{self.name} prepares to evade the next attack!")
        return True


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)

    def holy_strike(self, opponent):
        min_damage = int(self.attack_power * 1.55 - 5)
        max_damage = int(self.attack_power * 1.55 + 5)
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        print(f"{self.name} uses the Holy Strike for {damage} damage!")

    def divine_shield(self):
        print(f"{self.name} uses the Divine Shield, blocking the next attack!")
        return True 


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    #initialize flags for evasion and shield
    evade_flag = False
    shield_flag = False

    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.warrior_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                make_choice = input("Enter your choice (1 or 2): ")
                if make_choice == '1':
                    player.quick_shot(wizard)
                elif make_choice == '2':
                    evade_flag = player.evade()
                else:
                    print("Invalid choice. You just wasted your turn.")
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                make_choice = input("Enter your choice: ")
                if make_choice == '1':
                    player.holy_strike(wizard)
                elif make_choice == '2':
                    shield_flag = player.divine_shield()
                else:
                    print("Invalid choice. You just wasted your turn.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            print("\n--- Evil Wizard Turn ---")
            wizard.regenerate()
            if evade_flag:
                print(f"{player.name} evades the attack!")
                evade_flag = False
            elif shield_flag:
                print(f"{player.name} blocks the attack with Divine Shield!")
                shield_flag = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()