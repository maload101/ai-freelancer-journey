import json


PROFILE_FILE = "profile.json"

OPTION_INTRODUCE_USER = "1"
OPTION_SET_GOAL = "2"
OPTION_SET_LEVEL = "3"
OPTION_SET_FOCUS = "4"
OPTION_SHOW_GOAL = "5"
OPTION_SHOW_PROFILE = "6"
OPTION_SHOW_STUDY_PLAN = "7"
OPTION_SHOW_SKILLS = "8"
OPTION_EXIT = "9"


def show_welcome_message():
    print("Welcome to AI Freelancer Journey!")
    print("Let's build useful projects and turn them into real opportunities.")
    print()


def show_main_menu():
    print("1 - Introduce myself")
    print("2 - Set my current goal")
    print("3 - Set my current level")
    print("4 - Set my current focus")
    print("5 - Show my current goal")
    print("6 - Show user profile")
    print("7 - Show today's study plan")
    print("8 - Show skills to learn")
    print("9 - Exit")


def get_menu_choice():
    valid_choices = [
    OPTION_INTRODUCE_USER,
    OPTION_SET_GOAL,
    OPTION_SET_LEVEL,
    OPTION_SET_FOCUS,
    OPTION_SHOW_GOAL,
    OPTION_SHOW_PROFILE,
    OPTION_SHOW_STUDY_PLAN,
    OPTION_SHOW_SKILLS,
    OPTION_EXIT
]

    while True:
        choice = input("Choose an option: ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid option. Please choose 1, 2, 3, 4, 5, 6, 7, 8, or 9.")


def set_profile_field(prompt, error_message, confirmation_message):
    value = get_required_input(prompt, error_message)
    print(f"{confirmation_message}: {value}")
    return value


def get_required_input(prompt, error_message):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print(error_message)


def get_user_name():
    return get_required_input(
        "What is your name? ",
        "Name cannot be empty. Please try again."
    )


def introduce_user():
    name = get_user_name()
    print(f"Nice to meet you, {name}!")
    return name


def get_current_goal():
    return get_required_input(
        "What is your current goal? ",
        "Goal cannot be empty. Please try again."
    )


def set_current_goal():
    return set_profile_field(
        "What is your current goal? ",
        "Goal cannot be empty. Please try again.",
        "Your current goal is now"
    )


def set_user_level():
    return set_profile_field(
        "What is your current level? ",
        "Level cannot be empty. Please try again.",
        "Your level is now"
    )


def set_user_focus():
    return set_profile_field(
        "What is your current focus? ",
        "Focus cannot be empty. Please try again.",
        "Your focus is now"
    )

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
    with open(PROFILE_FILE, "w") as file:
        json.dump(user_profile, file, indent=4)

    print("User profile saved successfully.")


def create_empty_user_profile():
    return {
        "name": "",
        "current_goal": "",
        "level": "beginner",
        "focus": "Automation and IA"
    }


def load_user_profile():
    user_profile = create_empty_user_profile()

    try:
        with open(PROFILE_FILE, "r") as file:
            saved_profile = json.load(file)

        user_profile.update(saved_profile)

        print("Saved profile loaded.")

    except FileNotFoundError:
        print("No saved profile found. Starting with an empty profile.")

    except json.JSONDecodeError:
        print("Saved profile is corrupted. Starting with an empty profile.")

    return user_profile


def main():
    user_profile = load_user_profile()

    show_welcome_message()

    while True:
        show_main_menu()

        choice = get_menu_choice()

        if choice == OPTION_INTRODUCE_USER:
            user_profile["name"] = introduce_user()
            save_user_profile(user_profile)

        elif choice == OPTION_SET_GOAL:
            user_profile["current_goal"] = set_current_goal()
            save_user_profile(user_profile)

        elif choice == OPTION_SET_LEVEL:
            user_profile["level"] = set_user_level()
            save_user_profile(user_profile)

        elif choice == OPTION_SET_FOCUS:
            user_profile["focus"] = set_user_focus()
            save_user_profile(user_profile)

        elif choice == OPTION_SHOW_GOAL:
            show_current_goal(user_profile["current_goal"])

        elif choice == OPTION_SHOW_PROFILE:
            show_user_profile(user_profile)

        elif choice == OPTION_SHOW_STUDY_PLAN:
            show_study_plan()

        elif choice == OPTION_SHOW_SKILLS:
            show_skills_to_learn()

        elif choice == OPTION_EXIT:
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()