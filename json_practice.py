import json

user_profile = {
    "name": "Marcello",
    "current_goal": "Learn automation and AI"
}

with open("profile.json", "w") as file:
    json.dump(user_profile, file)

print("Profile saved as JSON.")

with open("profile.json", "r") as file:
    loaded_profile = json.load(file)

print()
print("Loaded profile:")
print(loaded_profile)

print()
print(f"Name: {loaded_profile['name']}")
print(f"Current goal: {loaded_profile['current_goal']}")