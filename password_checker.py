password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

length = len(password)

score = 0
if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score == 5:
    strength = "STRONG"
elif score >= 3:
    strength = "MEDIUM"
else:
    strength = "WEAK"

masked = ""
for i in range(length):
    masked += "*"

print("\nPassword:", masked)
print("Password Length:", length)
print("\nPassword Score:", score, "/ 5")
print("Password Strength:", strength)

file = open("password_log.txt", "a")
file.write("Length: " + str(length) + "\n")
file.write("Score: " + str(score) + "/5\n")
file.write("Strength: " + strength + "\n")
file.write("---------------------\n")
file.close()
