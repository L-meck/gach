import csv
from hashlib import new
from operator import ne

path = "C:\\Users\\kanai\\webAppsProjects\\gachie\\assets\\lab.csv"
lines = [line for line in open(path)]

# print(lines[0])
# print(lines[2])

print('\n')
print(lines[2])
print(lines[2].strip())
print(lines[2].strip().split(','))

print('\n')


# print(dir(csv))

#USING CSV MODULE
print('USING CSV MODULE')

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) #the first line is a header
data = [row for row in reader] #remaining of the data

print(header)
print(data[2])

print('\n')

# print(data) #ALL DATA


