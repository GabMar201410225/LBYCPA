#introduction
print("Welcome to GVlib!")

act_name = "Gabriel"
act_pass = "201410225"

while True:
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  if username == act_name and password == act_pass:
    print(f"Welcome, {act_name}!")
    break
  else:
    print("Invalid username or password")

print("Test")
