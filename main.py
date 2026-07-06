while True:
    print("Welcome to AI Freelancer Journey!")
    print()
    print("1 - Introduce myself")
    print("2 - Show my current goal")
    print("3 - Exit")
    print()

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What is your name? ")
        print(f"Nice to meet you, {name}!")

    elif choice == "2":
        goal = input("What is your current goal? ")
        print(f"Your current goal is: {goal}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

    print()