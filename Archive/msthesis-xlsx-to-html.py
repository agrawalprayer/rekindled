# convert csv to html using python
import numpy as np
import pandas as pd

data = pd.read_excel("ms-thesis-alumni-updated.xlsx", dtype=str) #Add the location of your csv file here
data.fillna("-", inplace=True)
n = len(data) #number of rows of data to consider
print(n)
#display(data[:n])

name = data['Name'][:n]
year = data['Year'][:n]
subject = data['Subject'][:n]
title = data['Title'][:n]
institute = data['Institute'][:n]

html_text_file = open("msthesis-xlsx-to-html.txt","w")
print("okay")
for i in range(n):
    line1 = "<td>"+str(name[i])+"</td>"
    line2 = "<td>"+str(year[i])+"</td>"
    line3 = "<td>"+str(subject[i])+"</td>"
    line4 = "<td>"+str(title[i])+"</td>"
    line5 = "<td>"+str(institute[i])+"</td>"
   
    each_entry = "<tr>" + line1 + line2 + line3 + line4 +line5 + "</tr>" +"\n"
    html_text_file.write(each_entry)

html_text_file.close()
file = open("msthesis-xlsx-to-html.txt","r")
print(file.readlines())
file.close()