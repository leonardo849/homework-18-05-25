import sys

name = input("what's your name")
age = int(input("how old are you?"))
category = input("what is your category? A, B or C").upper()
monthlyFee = input("what is your monthly fee? M or NM").upper()

additionalValue = 0



values = {
    "A": 58,
    "B": 70,
    "C": 81
}

categories = values.keys()



def calculateAdditionalValue(mothlyFee):
    if mothlyFee == "M":
        return 1.15
    elif mothlyFee == "NM":
        return 1
    else:
        print("there isn't that mothly fee")
        sys.exit(1)

def checkIfThereIsCategory(category):
    if category not in categories:
        print("there isn't: ", category)
        sys.exit(1)

checkIfThereIsCategory(category=category)


additionalValue = calculateAdditionalValue(mothlyFee = monthlyFee)

print(f"name: {name} | category {category}, value {values[category]} | monthlyfee {monthlyFee} | additional {round(((additionalValue - 1) * values[category]))} | total value {round(values[category] * additionalValue)}")

