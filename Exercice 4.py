password = "DEV@2023"
number_of_attempts = 3
while number_of_attempts > 0:
    a = input("Enter the password: ")
    if a == password:
        print("Hello")
        break

    else:
        number_of_attempts = number_of_attempts-1
        if number_of_attempts != 0:
            print("Bad password. You still have",number_of_attempts,"attempts.")
        else:
            print("Attempts exhausted!")
if number_of_attempts == 0:
    x = input("What is the name of your favorite movie?")
    print("Answer noted. Please contact support if you have forgotten your password.")
