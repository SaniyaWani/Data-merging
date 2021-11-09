import pandas as pd
import csv

df1=[]
df2=[]
with open("data2.csv", 'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        df2.append(i)
        
with open("data1.csv", 'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        df1.append(i)
header1 = df1[0]
header2 = df2[0]

data1 = df1[1:]
data2 = df2[1:]

data = []
header = header1 + header2
for i in data1:
    data.append(i)

for i in data2:
    data.append(i)

with open("Total_Stars.csv", 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)   
    csvwriter.writerows(data)    