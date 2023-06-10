# 1 create a way for check if what month will be in a leap year or not leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    """My Code result"""
    if month > 12 or month < 1:
        return("Invalid Input")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    the_days = month_days[month - 1]
    if is_leap(year):
        the_days += 1
        return the_days
    elif is_leap(year) == False:
        return the_days
    
    # if is_leap(year) and month == 2:
    #     return 29
    # return(month_days[month - 1])



#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# DOCSTRINGS:
# they are for adding what functions does.