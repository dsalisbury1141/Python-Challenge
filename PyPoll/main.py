import os
import csv

#import file and evaluate data, skip header
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as f:
   
  
    csvreader = csv.reader(f,delimiter =',')
    csvheader = next(csvreader)
    
    #Identify variables
    total_votes = 0  
    candidate_names = "0"  
    Percent_each_candidate = 0 
     
    Khan = 0
    Li = 0
    Correy = 0
    OTooley = 0
    max=max
    
    # identify lists

    voter_id_counter = 0  
    candidate_names_list = ["Khan", "Correy", "Li", "O'Tooley"]    
    total_per_candidate = [0,0,0,0]
    winner = []
    candidate_votes={}
    Winner = max(total_per_candidate)
    
     
    
    
   #For loop to collect votes by candidate hame and vote counts
    for row in csvreader:
        
        
        total_votes += 1  
        if row[2]=="Khan":
            total_per_candidate[0]+=1
        elif row[2]=="Li":
            total_per_candidate[1]+=1
        elif row[2]=="Correy":
            total_per_candidate[2]+=1
        elif row[2]=="O'Tooley":
            total_per_candidate[3]+=1
        
    

   
         #  Total net votes 
    Net_vote_average = sum(total_per_candidate) / len(total_per_candidate) 

    #print out data collected

print(f"""     
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
Total Votes per candidate:
Khan:    ({total_per_candidate[0]})
Correy:  ({total_per_candidate[2]})
Li:      ({total_per_candidate[1]})
O'Tooley:({total_per_candidate[3]})
---------------------------------------
The Winner with the hightest count is:({+max(total_per_candidate)})""")
