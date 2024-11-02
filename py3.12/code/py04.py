email = input("Enter your email:")
password = input("Enter your password:")
if '@' in email and len(password) >= 8:
    print("registered successfully!")
else:
    print("Invalid email or password")

