def show_welcome_message():
    print("Welcome to AI Freelancer Journey!")
    print("Let's build useful projects and turn them into real opportunities.")
    print()


def show_main_menu():
    print("1 - Introduce myself")
    print("2 - Set my current goal")
    print("3 - Show my current goal")
    print("4 - Show user profile")
    print("5 - Save user profile")
    print("6 - Load user profile")
    print("7 - Show today's study plan")
    print("8 - Show skills to learn")
    print("9 - Exit")


def get_menu_choice():
    valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        choice = input("Choose an option: ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid option. Please choose 1, 2, 3, 4, 5, 6, 7, 8 or 9.")


def get_user_name():
    while True:
        name = input("What is your name? ").strip()

        if name != "":
            return name

        print("Name cannot be empty. Please try again.")


def introduce_user():
    name = get_user_name()
    print(f"Nice to meet you, {name}!")
    return name


def get_current_goal():
    while True:
        goal = input("What is your current goal? ").strip()

        if goal != "":
            return goal

        print("Goal cannot be empty. Please try again.")


def set_current_goal():
    goal = get_current_goal()
    print(f"Your current goal is now: {goal}")
    return goal


def show_current_goal(goal):
    if goal == "":
        print("You haven't set a current goal yet.")
    else:
        print(f"Your current goal is: {goal}")


def show_study_plan():
    study_tasks = [
        "Practice Python functions",
        "Use Git to save progress",
        "Build small useful projects",
        "Practice lists",
        "Review today's cheat sheet"

    ]


    print("Today's study plan:")

    for index, task in enumerate(study_tasks, start=1):
        print(f"{index} - {task}")


def show_skills_to_learn():
    skills_learning = [
        "Python",
        "Git",
        "APIs",
        "n8n",
        "AI automation"
    
    ]

    print("Skills I want to learn:")

    for index, skills in enumerate(skills_learning, start=1):
        print(f"{index} - {skills}")



def format_profile_key(key):
    return key.replace("_", " ").capitalize()


def show_user_profile(user_profile):
    print("User profile:")

    for key, value in user_profile.items():
        formatted_key = format_profile_key(key)

        if value == "":
            print(f"{formatted_key}: not set yet")
        else:
            print(f"{formatted_key}: {value}")


def save_user_profile(user_profile):
    with open("profile.txt", "w") as file:
        for key, value in user_profile.items():
            file.write(f"{key}: {value}\n")

    print("User profile saved successfully.")


def load_user_profile():
    user_profile = {
        "name": "",
        "current_goal": ""
    }

    with open("profile.txt", "r") as file:
       for line in file:
        line = line.strip()

        if line == "":
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        
        user_profile[key] = value

    print("User profile loaded successfully.")
    return user_profile


def main():
    user_profile = {
        "name": "",
        "current_goal": ""
    }


    show_welcome_message()

    while True:
        show_main_menu()

        choice = get_menu_choice()

        if choice == "1":
            user_profile["name"] = introduce_user()

        elif choice == "2":
            user_profile["current_goal"] = set_current_goal()
        elif choice == "3":
            show_current_goal(user_profile["current_goal"])

        elif choice == "4":
            show_user_profile(user_profile)

        elif choice == "5":
            save_user_profile(user_profile)

        elif choice == "6":
            user_profile = load_user_profile()
        
        elif choice == "7":
            show_study_plan()

        elif choice == "8":
            show_skills_to_learn()

        elif choice == "9":
            print("Goodbye!")
            break

        print()


if __name__ == "__main__":
    main()