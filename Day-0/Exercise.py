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
# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill? $"))
# percent_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
# percent_number = (int(percent_tip) / 100)
# tip_value = percent_number * total_bill
# added_tip = (total_bill) + tip_value
# spliting_people = input("How many people to split the bill? ")

# spliting_people2int = int(spliting_people)

# each_to_pay = round(added_tip / spliting_people2int, 2)

# result = f"Each person should pay: ${each_to_pay}"
# print(result)

# Day 3.
# To calculate BMI (Body Mass Index)
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# BMI = round(weight / (height ** 2))

# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI <25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI  < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

# Day 4.
# To calculate Leap year
# year = int(input("Which year do you want to check? "))

# This to help understand.
# print(f"by 4= {year / 4}")
# print(f"by 100= {year / 100}")
# print(f"by 400= {year / 400}")

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Not Leap Year")    

# Day 3: build a pizza order program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill =+ 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")