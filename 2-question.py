age = int(input("how old are you?"))

if age < 16:
    print("you can't vote")
elif age > 18 and age <65:
    print("you have to vote")
else:
    print("you don't need to vote, but you can")