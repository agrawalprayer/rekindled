# convert csv to html using python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("C:/Users/91940/rekindled/internship-database.csv") #Add the location of your csv file here
data.fillna("-", inplace=True)
n = len(data) #number of rows of data to consider
print(n)
#display(data[:n])

program = data['Internship Program'][:n]
organisation = data['Organisation'][:n]
country = data['Country'][:n]
link = data['Link'][:n]
eligibility = data['Eligibility (BSMS years)'][:n]
subject = data['Subject'][:n]
duration = data['Duration'][:n]
deadline = data['Deadline'][:n]
paid = data['Funding'][:n]

html_text_file = open("C:/Users/91940/rekindled/csv_to_html.txt","w")

for i in range(n):
    line1 = "<td> <a href="+str(link[i])+">" +\
            str(program[i]) + "</a></td>"
    line2 = "<td>"+str(organisation[i])+"</td>"
    line3 = "<td>"+str(country[i])+"</td>"
    line4 = "<td>"+str(eligibility[i])+"</td>"
    line5 = "<td>"+str(subject[i])+"</td>"
    line6 = "<td>"+str(deadline[i])+"</td>"
    line7 = "<td>"+str(duration[i])+"</td>"
    line8  = "<td>"+str(paid[i])+"</td>"
    
    each_entry = "<tr>" + line1 + line2 + line3 + line4 +line5 + line6 + line7+ line8 + "</tr>" +"\n"
    html_text_file.write(each_entry)

html_text_file.close()
file = open("C:/Users/91940/rekindled/csv_to_html.txt","r")
print(file.readlines())
file.close()