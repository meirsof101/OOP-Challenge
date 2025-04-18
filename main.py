from pet import Pet

# Create pet with type and level system
import sys
sys.stdout.reconfigure(encoding='utf-8')



def create_pet():
    print("Choose your pet type: 🦁 Lion, 🐘 Elephant, 🦒 Giraffe")
    import sys
    sys.stdout.flush()
    pet_type = input("Enter your pet type: ").lower()

    if pet_type == "lion":
        my_pet = Pet("Mufasa 🦁")
    elif pet_type == "elephant":
        my_pet = Pet("Biggie 🐘")
    elif pet_type == "giraffe":
        my_pet = Pet("Murife 🦒")
    else:
        print("Invalid pet type. Defaulting to lion.")
        my_pet = Pet("Mufasa 🦁")

    return my_pet

# Define custom actions for each pet
def custom_actions():
    print("\nChoose your action:")
    print("1. Eat 🍽️")
    print("2. Sleep 😴")
    print("3. Play 🎾")
    print("4. Tell a joke 😂")
    print("5. Dance 💃")
    print("6. Show Status 📝")
    print("7. Teach a new trick 🧠")
    print("8. Check pet's goal 🎯")
    print("0. Exit 🚪")

# Game loop with conversation, leveling and goals
def game_loop(my_pet):
    while True:
        # Ask the pet what to do
        print(f"\n{my_pet.name} says: 'What would you like to do today?'")
        custom_actions()
        choice = input("Enter your choice: ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            if isinstance(my_pet, Pet):  # Pet-specific jokes
                if my_pet.name == "Mufasa 🦁":
                    print(f"{my_pet.name} says: 'Why did the lion eat the comedian? Because he wanted to hear some ROAR-ing laughter! 😂'")
                elif my_pet.name == "Biggie 🐘" :
                    print(f"{my_pet.name} says: 'Why don’t elephants use computers? Because they’re afraid of the mouse! 🐘😂'")
                elif my_pet.name == "Murife 🦒":
                    print(f"{my_pet.name} says: 'What do you call a giraffe’s elevator music? High notes! 🎶🦒'")
        elif choice == "5":
            print(f"{my_pet.name} is dancing! 💃🎶")
            my_pet.happiness = min(10, my_pet.happiness + 2)
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            trick = input("What trick do you want to teach? ")
            my_pet.train(trick)
        elif choice == "8":
            print(f"{my_pet.name}'s goal: Learn 5 tricks to unlock a super move!")
            print(f"Tricks learned: {len(my_pet.tricks)} / 5")
            if len(my_pet.tricks) >= 5:
                print(f"{my_pet.name} has unlocked a super trick! 🎉")
        elif choice == "0":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again! 😅")


# Main flow
def main():
    my_pet = create_pet()
    game_loop(my_pet)

# Run the game
if __name__ == "__main__":
    main()


