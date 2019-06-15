# PyBank

# import modules
import os
import csv

# set file path
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# define lists & variables, set anything I need to calc at 0
monthYR = []
monthYR_cnt = 0
totalPL = 0
cmrev = 0
pmrev = 0
ttlrev = 0
revchgs = []


# open and read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csvheader = next(csvreader)

#I need to loop through the data to collect the answers
        
        for row in csvreader:
           
            #make a list of the month-yr
            monthYR_cnt = monthYR_cnt + 1
            monthYR.append(row[0])
                       
            #total up the P&L across
            totalPL += int(row[1])
            
            #changes in rev
            cmrev = int(row[1])
            ttlrev = ttlrev + cmrev
            if monthYR_cnt > 1:
                revchg = cmrev - pmrev
                revchgs.append(revchg)
            pmrev = cmrev
            
# dig into month by month change data
allchanges = sum(revchgs)
avgchange = round(allchanges / (monthYR_cnt - 1), 2)
grinc = max(revchgs)
grdec = min(revchgs)
grincmthindex = revchgs.index(grinc)
grdecmthindex = revchgs.index(grdec)
grincmth = monthYR[grincmthindex]
grdecmth = monthYR[grdecmthindex]
            
            
# print to terminal
       
print ("=====================================================")
print ("Financial Analysis")
print ("-----------------------------------------------------")
print ("Total Months: " + str(monthYR_cnt))
print ("Total Profit: " + "$" + str(totalPL))
print (f"Average Change: ${avgchange}")
print (f"Greatest Increase in Profits: {grincmth} (${grinc})")
print (f"Greatest Decrease in Profits: {grdecmth} (${grdec})")
print ("=====================================================")

output_file = os.path.join("Financial Analysis.txt")
filepath = os.path.join(".", )
with open(output_file, "w") as text:
    text.write("=====================================================" + "\n")
    text.write("Financial Analysis" + "\n")
    text.write("-----------------------------------------------------" + "\n")
    text.write("Total Months: " + str(monthYR_cnt) + "\n")
    text.write("Total Profit: " + "$" + str(totalPL) + "\n")
    text.write(f"Average Change: ${avgchange}" + "\n")
    text.write(f"Greatest Increase in Profits: {grincmth} (${grinc})" + "\n")
    text.write(f"Greatest Decrease in Profits: {grdecmth} (${grdec})" + "\n")
    text.write("=====================================================" + "\n")
    
    
    
    
    