# BM named it calcAverage.py

ages = [10, 20, 30, 40]
incomes = [100, 200, 300, 400]

def calculate_average(list):
    sum = 0
    for i in list:
        sum = sum + i

    return sum/len(list)

print(calculate_average(ages))
print(calculate_average(incomes))