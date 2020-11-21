#import the modules
import os
import csv

#Establish Path to csv file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Define variables and lists to store data
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
change_list = []
total_change = 0
months = [] 
total_m = 1
net_total= 0

#read the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Skip the header and go to next row
    header = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    net_total = int(first_row[1])

#calculate total number of months and net total of profit/loss    
    for row in csvreader:

        total_m = total_m + 1
        net_total = net_total + int(row[1])
 
 #Net change in profit/loss and average of that change       
        current_value = int(row[1])
        
        change_value = int(current_value-previous_row)

#Store the values in corresponding lists
        change_list.append(change_value)
        months.append(row[0])
        previous_row = int(row[1])

#Sum up the total change over the period and average it
        total_change = total_change + change_value
        avg_change = round(sum(change_list)/len(months), 2)
         
#Calculate greatest increase in Profit/Loss
        if change_value > greatest_increase[1]:
                greatest_increase[0] = str(row[0])
                greatest_increase[1] = change_value

#Calculate greatest decrease in Profit/Loss
        if change_value < greatest_decrease[1]:
                greatest_decrease[0] = str(row[0])
                greatest_decrease[1] = change_value
		
#Print to terminal

print(" Financial Analysis \n")
print("------------------------------\n")
print(f"Total Months: {total_m}\n")
print(f"Total: ${net_total}\n")
print(f"Average  Change: ${avg_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Write the output to txt file    
with open(output_file, 'w', newline='') as txtfile:
    
    txtfile.write(" Financial Analysis \n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {total_m}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average  Change: ${avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")









