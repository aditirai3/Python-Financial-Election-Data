#import the modules
import os
import csv

#Establish Path to csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Define variables and lists to store data

months = 0
total_profit = 0


#read the csv file
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# #Skip reading header and print number of months in csv
    header = next(csv_reader)
    
    for row in csv_reader:
       months = months + 1
       total_profit = total_profit + int(row[1])

# #Store values in lists

       months.append(row[0])
       total_profit.append(int(row(1))
  #calculate change  
    change = int(total_profit[i+1]) - int(total_profit[i]) 
    monthly_change.append(change)
    avg = round(sum(monthly_change)/len(monthly_change),2)
    
#     #Greatest increase and decrease
   max_increase_value = max(monthly_change)
   max_decrease_value = min(monthly_change)

# print(months)
# print(net_amount)
#print(avg)
