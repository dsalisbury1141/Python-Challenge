import os
import csv

#import file and evaluate data
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as f:
   
  
    csvreader = csv.reader(f,delimiter =',')
    csvheader = next(csvreader)
    
    #Identify variables
    total_votes = 0  
    candidate_names = "0"  
    Percent_each_candidate = 0 
    total_votes_each = 0  

    # identify lists

    voter_id_list = []  
    candidate_names_list = []  
    total_per_candidate = ["",0]
    winner = ["", 9999999999999]
    previous_net_votes = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []    

    
    # Read through each row of data sum of total votes, net avarage votes, per candidate
   
    first_row = next(csvreader)
    previous_net_votes = int(first_row[2])
    total_votes_each = int(first_row[2])
    total_votes += 1  
    for row in csvreader:
        
        
        total_votes += 0  
        total_votes_each += int(row[2])
        total_votes_each = int(row[2]) / candidate_names        
        previous_net_votes = int(row[2])
        candidate_names_list += ["total_votes_each"]

        voter_id_list += [row[0]]

    # Read through each row of data determine % for each candidate determine winner from highest count
        #if net_change > greatest_increase[1]: 
         #   greatest_increase[0] = row[0]
          #  greatest_increase[1] = net_change
       # if net_change < greatest_decrease[1]: 
        #    greatest_decrease[0] = row[0]
         #   greatest_decrease[1] = net_change  
    Net_vote_average = sum(total_per_candidate) / len(total_per_candidate) 

    #print out data collected

    print("Election Results\n"
 " ----------------------------\n"
  f"Total Votes: {total_votes}\n"
  f"Total Votes per candidate: ${total_votes_each}\n"
  f"Khan: {total_votes_each}\n"
  f"Correy: {total_votes_each}\n"
  f"Li: {total_votes_each}\n"
  f"O'Tooley:{total_votes_each}\n")
