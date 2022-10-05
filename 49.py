age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")

if(age > 12 and age < 20):
    if(gender == "male"):
        print("you are a teenage boy.")
    else:
        print("you are a teenage girl.")
else:
    print("You are not a teenager.")
