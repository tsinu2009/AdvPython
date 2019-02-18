import pandas as pd
import sys

print('Name is :',sys.argv[1])
print('Gender is :',sys.argv[2])
print('Age is :',sys.argv[3])
print('Test score is :',sys.argv[4])

name = sys.argv[1]
gender = int(sys.argv[2])
age = int(sys.argv[3])
test_score = int(sys.argv[4])

filepath='DataEntry.xlsx'
data=pd.write_excel(filepath)
print(data)	