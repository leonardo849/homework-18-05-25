import sys

buildingValue = int(input("type the building's value"))
monthlySalary = int(input("type your monthly salary"))
years = int(input("how many years do you want to pay over"))
installmentValue = buildingValue / (years * 12)
print(installmentValue)

if installmentValue > monthlySalary * 0.3:
    print("The loan can't be greater than 30% of your monthly salary")
    sys.exit(1)
else:
    print(f"you can buy that building, installmentValue {installmentValue}. The loan can't be greater than 30% of your monthly salary")