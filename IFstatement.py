import datetime

print("check if it is Tuesday!")

# create variable today, inside datastructure today, inside datetime datastructure within datetime package
today = datetime.datetime.today() 
# create a variable to extract weekday from today, which is represented by integers 1-6
day_of_week=today.weekday()

#if statement
if day_of_week == 1:
    print("It is Tuesday")
elif day_of_week == 2:
    print("It is Wednesday")
else:
    print("It is not Tuesday")