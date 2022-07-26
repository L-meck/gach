import pandas pd

# DataFrame to read our input CS file
dataFrame = pd.read_csv("C:\Users\amit_\Desktop\SalesRecords.csv")
print("\nInput CSV file = \n", dataFrame)

# sorting according to Car column
dataFrame.sort_values("Car", axis=0, ascending=True,inplace=True, na_position='first')

print("\nSorted CSV file (according to Car Names) = \n", dataFrame)

# sorting according to Reg_Price column
dataFrame.sort_values("Reg_Price", axis=0, ascending=True,inplace=True, na_position='first')

print("\nSorted CSV file (according to Registration Price) = \n", dataFrame)