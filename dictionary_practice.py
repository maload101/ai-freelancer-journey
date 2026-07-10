user_profile = {
    "name": "Marcello",
    "goal": "Learn automation and AI",
    "level": "beginner"
}

print(user_profile["name"])
print(user_profile["goal"])
print(user_profile["level"])


user_profile["level"] = "early beginner"
user_profile["focus"] = "automation"

print()
print("Updated profile:")
print(user_profile)


print()
print("Profile summary:")
print(f"Name: {user_profile['name']}")
print(f"Goal: {user_profile['goal']}")
print(f"Level: {user_profile['level']}")
print(f"Focus: {user_profile['focus']}")

print()
print("Profile using loop:")

for key, value in user_profile.items():
    print(f"{key}: {value}")
    