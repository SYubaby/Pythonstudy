
'''
计算
'''

# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost = miles_driven * (dollars_per_gallon / miles_per_gallon)
    return cost


# Type your code here.
miles_per_gallon = float(input())
dollars_per_gallon = float(input())


driving_f1 = driving_cost(miles_per_gallon, dollars_per_gallon, 10)
print(f'{driving_f1:.2f}')
driving_f2 = driving_cost(miles_per_gallon, dollars_per_gallon, 50)
print(f'{driving_f2:.2f}')
driving_f3 = driving_cost(miles_per_gallon, dollars_per_gallon, 400)
print(f'{driving_f3:.2f}')