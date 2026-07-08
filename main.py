def show_welcome_message():
    print("Welcome to AI Freelancer Journey!")
    print("Let's build useful projects and turn them into real opportunities.")
    print()


def show_main_menu():
    print("1 - Introduce myself")
    print("2 - Set my current goal")
    print("3 - Show today's study plan")
    print("4 - Exit")
    print()


def introduce_user():
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")


def set_current_goal():
    goal = input("What is your current goal? ")
    print(f"Your current goal is: {goal}")

def show_study_plan():
    print(f"Today's study plan:")
    print(f"1 - Practice Python functions")
    print(f"2 - Use Git to save progress")
    print(f"3 - Build small useful projects")

show_welcome_message()

while True:
    show_main_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        introduce_user()

    elif choice == "2":
        set_current_goal()

    elif choice == "3":
        show_study_plan()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2,3 or 4.")

    print()