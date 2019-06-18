#PyPoll

# import modules
import os
import csv

# set file path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# define lists & variables
VoterID = []
Total_Votes = 0
Candidate_Votes = {}
Candidate_pct = {}
Win_Votes = 0
Winner = []


# open and read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csvheader = next(csvreader)

# loop through the csv file
        
        for row in csvreader:
           
            # make a list of the VoterID's
            VoterID.append(row[0])
            
            # count the VoterIDs to get Total Votes
            Total_Votes = len(VoterID)
            
            # set list of the Candidates for the Candidate_Votes dict
            Candidate = (row[2])
            
            # adding up candidate votes
            if Candidate in Candidate_Votes:
                Candidate_Votes[Candidate] = Candidate_Votes[Candidate] + 1
            
            # create for different Candidates, assumes all names are consistent
            else:
                Candidate_Votes[Candidate] = 1
                
               
# Checking the code to this point to see if I am getting correct outputs
#print("Total Votes: " + str(Total_Votes))
#print(f"Candidate Vote Totals: {Candidate_Votes}")


# calc the vote percentage and identify who won
for Official, Vote_Count in Candidate_Votes.items():
    Candidate_pct[Official] = '{0:.3%}'.format(Vote_Count / Total_Votes)
    if Vote_Count > Win_Votes:
        Win_Votes = Vote_Count
        Winner = Official

# print to terminal     
print ("======================================")
print ("Election Results")
print ("--------------------------------------")
print ("Total Votes: " + str(Total_Votes))
print ("--------------------------------------")
for Official, Vote_Count in Candidate_Votes.items():
    print(f"{Official}: {Candidate_pct[Official]} ({Vote_Count})")
print ("--------------------------------------")
print(f"Winner: {Winner}")
print ("======================================")


# print to csv
output_file = os.path.join("Election Analysis.txt")
filepath = os.path.join(".", )
with open(output_file, "w") as text:
    text.write("======================================" + "\n")
    text.write("Election Results" + "\n")
    text.write("--------------------------------------" + "\n")
    text.write("Total Votes: " + str(Total_Votes) + "\n")
    text.write("--------------------------------------" + "\n")
    for Official, Vote_Count in Candidate_Votes.items():
        text.write(f"{Official}: {Candidate_pct[Official]} ({Vote_Count})" +"\n")
    text.write("--------------------------------------" + "\n")
    text.write(f"Winner: {Winner}" + "\n")   
    text.write("======================================" + "\n")
    