import json

user_profile = {
    "name": "Marcello",
    "current_goal": "Learn automation and AI"
}

with open("profile.json", "w") as file:
    json.dump(user_profile, file)

print("Profile saved as JSON.")