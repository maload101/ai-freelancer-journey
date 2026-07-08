current_goal = ""


def show_welcome_message():
    print("Welcome to AI Freelancer Journey!")
    print("Let's build useful projects and turn them into real opportunities.")
    print()


def show_main_menu():
    print("1 - Introduce myself")
    print("2 - Set my current goal")
    print("3 - Show my current goal")
    print("4 - Show today's study plan")
    print("5 - Exit")
    print()


def get_user_name():
    name = input("What is your name? ").strip()
    return name


def introduce_user():
    name = get_user_name()
    print(f"Nice to meet you, {name}!")


def get_current_goal():
    goal = input("What is your current goal? ").strip()
    return goal


def set_current_goal():
    goal = get_current_goal()
    print(f"Your current goal is now: {goal}")
    return goal


def show_current_goal():
    if current_goal == "":
        print("You haven't set a current goal yet.")
    else:
        print(f"Your current goal is: {current_goal}")


def show_study_plan():
    print("Today's study plan:")
    print("1 - Practice Python functions")
    print("2 - Use Git to save progress")
    print("3 - Build small useful projects")


show_welcome_message()

while True:
    show_main_menu()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        introduce_user()

    elif choice == "2":
        current_goal = set_current_goal()


    elif choice == "3":
        show_current_goal()

    elif choice == "4":
        show_study_plan()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, 4, or 5.")

    print()