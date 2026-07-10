profile_text = "Name: Marcello\nCurrent goal: Learn automation and AI"

with open("profile.txt", "w") as file:
    file.write(profile_text)

print("Profile saved successfully.")

with open("profile.txt", "r") as file:
    saved_profile = file.read()

print()
print("Reading saved profile:")
print(saved_profile)