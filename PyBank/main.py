import os
import csv

#import file and evaluate data
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, newline='') as f:
   
  
    csvreader = csv.reader(f,delimiter =',')
    csvheader = next(csvreader)
    
    total = 0
    total_months = 0
    
    month = []
    net_change_list = []
    greatest_increase = ["",0]
    greatest_decrease = ["", 9999999999999]
    
    # Read through each row of data sum of total months, net avarage, profit / Losses over entire period
   
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    total += int(first_row[1])
    total_months += 1
    for row in csvreader:
        
        total += int(row[1])
        total_months += 1
        net_change = int(row[1]) - previous_net 
        previous_net = int(row[1])
        net_change_list += [net_change]
        month += [row[0]]

    # Read through each row of data sum of total net change, with the greatest increase and decrease
        if net_change > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]: 
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change  
    Net_monthly_average = sum(net_change_list) / len(net_change_list) 

    #print out data collected

    print("Financial Analysis\n"
 " ----------------------------\n"
  f"Total Months: {total_months}\n"
  f"Total: ${total}\n"
  f"Average  Change: ${Net_monthly_average}\n"
  f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n"
  f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}") 
      

      
      
      