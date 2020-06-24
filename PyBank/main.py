import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, newline='') as f:
    #with open(csvpath) as csvfile:
  
    csvreader = csv.reader(f,delimiter =',')
    #csvreader = csv.reader(file, delimiter=",")
    #print(csvreader)
    csvheader = next(csvreader)
    Lines = len(list(csvreader))
    print("Total Months: ", Lines)
    #csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    total = 0
    
    #for row in csvreader:
     #   total = sum(int(row[1])
    #print(total)

    

    #csvreader = reader(read_obj)
    
    #print(csvreader)
    #csvreader = csv.DictReader(f)
    #csvheader = next(csvreader)

    #profit = []
    #month = []
    
    #total = 0

            # Read through each row of data sum of profit / Losses 
    #for row in csvreader:


    #print(f"csv Header: {header}")
    
##columns1 = index(Total_Profit/Losses)
    
    #for row in csvreader:
        #total += int(row[1])
        #total = sum(float(row[1]) for row in csvreader)
        #total += (int(row[1])) 
        #total += float(row[column[1]])
        #total = sum(int(row[1]) for row in csvreader)
    
        #profit.append(row[1])
        #month.append(row[0])
        #total = sum(int(profit))
        #total = sum(int(row[1]))
                #total += int(row[1])
        
        #totals = totals + int(row[1])
        #total = sum([float(row[1]) for row in csvreader])
    #for col in row[1]:
            #total += int(col)
        #print total
        

    #header = next(csvreader)
    # Read header  first (skip if there is no header)
    #BudgetData = []
   # for each_line in csvreader:
    #    BudgetData += each_line
     #   BudgetData = sum(row[1]
    #print (BudgetData)
    #BudgetData = 0 
   
    #total = sum(list.index(row[1]))
    
#csvreader = csv.reader(csvreader, delimiter =',')

#Total = sum (row[1])
    #for row in csvreader:
        #total = sum(row[1]
    #row[1] = int()    
    # #total = sum(float(row[1]) for row in csvreader)
    #numbers = (float(row[1])for row in csvreader)
#total = 0 
#for row in csvreader:
 #       _total = row[1]
  #      _total = float(_total)
        #_total = 0 
   #     _total += _total

    #Total = sum(float(row[1]) for row in csvreader)
    #Total = sum(Total)
    #f.next()
    
    #numbers = (float(row[1])for row in csv.reader(csvreader))
    #Total = sum(numbers)
   
   #for row in csv.reader(csvreader):
    #Total += float(row[1])
    #Total = 0

    #list1 = 
    #print (list1)
    #for row in csv.reader(csvreader):
        #print
        #for row in row[2]:
            
        #print(Total)
        
            #Print Values

#print(total)
    #print(Total)

    #for count in range(0,len(Date)
    
        #Total_Months = len()
        #print (len("budget_data.csv"))

        #if header != None:
           
        
            
            

            #print(csvreader)
            
            #print(f"csv Header: {header}")
            # Read through each row of data  
            #for row in csvreader:
                #print(row)
            
    
# set columns data and Profit and losses
        #Total_Months = int(0)
        #Total = int(row[1])
        #Average_change = int(row[2])
        #Greatest_increase = int(row[3])
        #Greatest_decrease = int(row[4])
# Average of the changes in P&L over entire period

    #Greatest increase in profits , Date and Amount entire period
    #Greatest_increase = Max(budget_data_csv)
    # Greatest decrease  in losses (date and amount) over entire period
    #Greatest_decrease = min(budget_data_csv)
#def average(Greatest_increase, Greatest_decrease):
    #print(Average_change)
    #def len(Total_Months):print(Total_Months)
#def sum (Total):Print(Total = sum(csvpath))