import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


#read in the CSV file

with open(csvpath, newline='') as data:
    bank_data = csv.reader(data)
    print(bank_data)
    
    bank_header = next(bank_data)
    print(f"CSV Header: {bank_header}")

#create lists to be used to store variable values at each row
row_list = []
revenue_list = []
month_list = []

for row in bank_data:
    row_list.append(1)
    revenue_list.append(int(row[1]))
    month_list.append(row[0])

Total_Months = sum(row_list)
Total = sum(revenue_list)

#create and update change list for monthyl change of revenuee

change_list = []
for i in range(1, len(revenue_list)):
    change_list.append(revenue_list[i]-revenue_list[i-1])

#finding of statists to be printed in financial analysis

Average_change = round(sun(change_list/len(change_list)),2)
Greatest_increase = max(change_list)
Greatest_decrease = min(change_list)
Increase_index = change_list.index(Greatest_increase)
Decrease_index = change_list.index(Greatest_decrease)
Increase_month = month_list[Increase_index+1]
Decrease_month = month_list[Decrease_index+1]

#financial analysis

print("Financial Analysis")
Print("____________________________________")
Print(f'Total Month: {Total_Months}')
Print(f'Total: {Total}')
Print(f'Average Change: {Average_change}')
Print(f'Greatest Increase in Profits: {Increase_month} (${Increase_index})')
Print(f'Greatest Decrease in Profits: {Decrease_month} (${Decrease_index})')

#ffff