'''
print("Welcome to python")

a = 5
b = 10
c = a + b
print(c)

x = input("Enter first number : ")
y = input("Enter Second number : ")
z = int(x) + int(y)
print(z)

if c > z:
    print("C is the largest value")
else:
    print("Z is the largest value")
'''    


'''
run = []
total_run = 0
for i in range(4):
    run.append(int(input(f"Enter run {i+1}: ")))
    total_run += run[i]
batting_average = total_run/4
print(batting_average)
'''


'''
# Area of a circle
import math

r = int(input("Enter the radius of circle: "))
print("Area of circle: ", math.pi*r*r)
'''


'''
cost1comp = int(input("Enter cost of one computer: "))
compnum = int(input("Enter the number of computers to be bought: "))
compcost = cost1comp * compnum

cost1table = int(input("Enter the cost of 1 table: "))
tablenum = int(input("Enter the number of tables to be bought: "))
cost1chair = int(input("Enter the cost of 1 chair: "))
chairnum = int(input("Enter the number of chairs to be bought: "))
furniturecost = cost1table*tablenum + cost1chair*chairnum

wagesph = int(input("Number of wages per hour: "))
numhours = int(input("Number of hours worked: "))
labourcost = wagesph*numhours

budget = compcost + furniturecost + labourcost
print("Budget: ", budget)
'''



