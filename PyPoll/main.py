#PyPoll

# import modules
import os
import csv

# set file path
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

# define lists & variables
VoterID = []
Candidate = []

# open and read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csvheader = next(csvreader)

#I need to loop through the data to collect the answers
        
        for row in csvreader:
           
            #make a list of the VoterID's
            VoterID.append(row[0])
            
            #count the VoterIDs to get Total Votes
            total_votes = len(VoterID)
            
            #make a list of the Candidates
            Candidate.append(row[2])
            
            #Run a set to get Candidates
            Candidates = set(Candidate)

            
            
#count Candidate votes
Khan = (Candidate.count('Khan'))
OTooley = Candidate.count("O'Tooley")
Correy = Candidate.count('Correy')
Li = Candidate.count('Li')

#percent of votes per candidate
Khan_pct = round((Khan / total_votes) * 100, 3)
OTooley_pct = round((OTooley / total_votes) * 100, 3)
Correy_pct = round((Correy / total_votes) * 100, 3)
Li_pct = round((Li / total_votes) * 100, 3)
                       

            
# print to terminal
       
print ("======================================")
print ("Election Results")
print ("--------------------------------------")
print ("Total Votes: " + str(total_votes))
print ("--------------------------------------")
print (f"Khan: {Khan_pct}% ({Khan})")
print (f"Correy: {Correy_pct}% ({Correy})")
print (f"Li: {Li_pct}% ({Li})")
print (f"O'Tooley: {OTooley_pct}% ({OTooley})")
print ("--------------------------------------")
print ("Winner: Khan")
print ("======================================")

output_file = os.path.join("Election Analysis.txt")
filepath = os.path.join(".", )
with open(output_file, "w") as text:
    text.write("======================================" + "\n")
    text.write("Election Results" + "\n")
    text.write("--------------------------------------" + "\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("--------------------------------------" + "\n")
    text.write(f"Khan: {Khan_pct}% ({Khan})" + "\n")
    text.write(f"Correy: {Correy_pct}% ({Correy})" + "\n")
    text.write(f"Li: {Li_pct}% ({Li})" + "\n")
    text.write(f"O'Tooley: {OTooley_pct}% ({OTooley})" + "\n")
    text.write("======================================" + "\n")
    
    
    
    