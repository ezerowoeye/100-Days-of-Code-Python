# 1
# score = 20
# height= 1.8
# isWinning= True

# print(f"Your score is {score}, your height is {height}, you are not {isWinning}")

# 2
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# age = input("What is your current age? ")
# age2int = (90 - int(age))
# days = age2int * 365
# weeks = age2int * 52
# months = age2int * 12
# result = f"You have {days} days, {weeks} weeks, and {months} months left"
# print(result)
# # print(f"You have {days} days, {weeks} weeks, and {months} months left")

# 3
# a tip calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percent_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
percent_number = (int(percent_tip) / 100)
tip_value = percent_number * total_bill
added_tip = (total_bill) + tip_value
spliting_people = input("How many people to split the bill? ")

spliting_people2int = int(spliting_people)

each_to_pay = round(added_tip / spliting_people2int, 2)

result = f"Each person should pay: ${each_to_pay}"
print(result)