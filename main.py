import secrets
import string


password_length = int(input("Password length? "))
random = secrets.randbelow(10)
special_chars = input("Special characters? Y/N ").upper()
if special_chars == 'Y':
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)
else:
    alphabet = string.ascii_letters + string.digits
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= password_length / random):
        break
print(password)
