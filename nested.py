password=input("Enter password: ")

if len(password) > 8:
  print("password too short, must be more than 8 characters.")
if any(number in password for number in "0123456789"):
  print("password must contain a number")
if password != password.lower():
  print("password must contain an uppercase letter")
if password != password.upper():
  print("password must contain a lowercase letter")
else:
  print("Password valid. Account created.")
