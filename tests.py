import csv

path = "C:\\Users\\kanai\\webAppsProjects\\gachie\\assets\\lab.csv"
lines = [line for line in open(path)]

# print(lines[0])
# print(lines[2])

print('\n')
# print(lines[2])
# print(lines[2].strip())
# print(lines[2].strip().split(','))

# print('\n')


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



# ////////////////////////////////////
path2 = "C:\\Users\\kanai\\webAppsProjects\\gachie\\assets\\lab.csv"
file2 = open(path2, newline="")
reader2 = csv.reader(file2)

header2 = next(reader2)

data2 = []
for row in reader2:
    # row = [Account , Customer , TSR , Street , Cell , Latest coltage , Latest gas remaining , Days since last task , 'Days since last cooked', 'Grams per day']
    # account = int(row[0])
    # customer = row[1]
    # tsr = row[2]
    # street = row[3]
    # customer_phone = row[4]
    # latest_voltage = float(row[5])
    # gas_remaining = float(row[6])
    # last_task_date = int(row[7])
    # last_cooked = row[8]
    # grams_per_day = float(row[9])
    account = row[0]
    customer = row[1]
    tsr = row[2]
    street = row[3]
    customer_phone = row[4]
    latest_voltage = row[5]
    gas_remaining = row[6]
    last_task_date = row[7]
    last_cooked = row[8]
    grams_per_day = row[9]

    data2.append([account , customer , tsr , street , 
        customer_phone , latest_voltage , gas_remaining , 
        last_task_date , last_cooked , grams_per_day])

print('STUFF WORKING.... \n')
print(data2[2])


       