expected_user = "luhan"
expected_password = "2802"

user = input("Enter your username: ")
password = input("Enter your password: ")

if(user == expected_user and password == expected_password):
    print("Logged in")
else:
    print("Wrong username or password")