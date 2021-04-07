import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(string.punctuation)
password_length = int(input("Password length? "))
random = secrets.randbelow(10)
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= password_length / random):
        break
print(password)
