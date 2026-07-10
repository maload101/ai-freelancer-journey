def show_welcome_message():
    print("Welcome to AI Freelancer Journey!")
    print("Let's build useful projects and turn them into real opportunities.")
    print()


def show_main_menu():
    print("1 - Introduce myself")
    print("2 - Set my current goal")
    print("3 - Show my current goal")
    print("4 - Show user profile")
    print("5 - Show today's study plan")
    print("6 - Show skills to learn")
    print("7 - Exit")


def get_menu_choice():
    valid_choices = ["1", "2", "3", "4", "5", "6", "7"]

    while True:
        choice = input("Choose an option: ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid option. Please choose 1, 2, 3, 4, 5, 6 or 7.")


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


def show_user_profile(user_profile):
    print("User profile:")

    if user_profile["name"] == "":
        print("Name: not set yet")
    else:
        print(f"Name: {user_profile['name']}")

    if user_profile["current_goal"] == "":
        print("Current goal: not set yet")
    else:
        print(f"Current goal: {user_profile['current_goal']}")

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
            show_study_plan()

        elif choice == "6":
            show_skills_to_learn()

        elif choice == "7":
          print("Goodbye!")
          break

        print()


if __name__ == "__main__":
    main()