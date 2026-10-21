
import secrets
import string

password_len = int(input("Enter password Length: "))

if password_len < 4:
    print("Password length must be at least 4!")
    quit()

charvalues = string.ascii_letters + string.digits + string.punctuation

password = [
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.digits),
    secrets.choice(string.punctuation)
]

for i in range(password_len - 4):
    password.append(secrets.choice(charvalues))

secrets.SystemRandom().shuffle(password)

print("Your random Password is:", "".join(password))
