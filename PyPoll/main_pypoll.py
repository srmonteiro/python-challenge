#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 


#________________________________________________________________________________________#  Import Modules
import os #______________________________________________________________________________#  Import os to assist with reading relative paths on different computers
import csv #_____________________________________________________________________________#  Import csv so that we can read content of election_data.csv
import statistics #______________________________________________________________________#  Import csv to perform operations like average, min, and max

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Declaring Variables that will impact all code, 
row = [] #_______________________________________________________________________________#  Declaring 'row' as an empty list that will later point to each row in the csv, also could be called "votes"
candidates = [] #________________________________________________________________________#  Declaring 'candidate' as an empty list that will later point to each candidate the csv
candidatevotecast = []
vote_count = 0 #_________________________________________________________________________#  Declaring 'vote_count' as a integer with a value of 0
electedvotescast = 0
#monthly_profit_change = 0 #______________________________________________________________#  Declaring 'monthly_profit_change' to calculate Profit/Loss each month and average Profit/Loss 
#monthly_profit_change_list = [] #________________________________________________________#
#monthly_profit_lastmonth = 0 #___________________________________________________________#  
#monthly_profit_thismonth = 0 #___________________________________________________________#  
#avg_monthly_profit_change = 0 #__________________________________________________________# 
#max_monthly_profit_increase = 0 #________________________________________________________# 
#max_monthly_profit_decrease = 0 #________________________________________________________#
#max_increase_month = () #________________________________________________________________#
#max_decrease_month = () #________________________________________________________________#
#month = [] #_____________________________________________________________________________#
#skip_start_month = True

#________________________________________________________________________________________#  
#________________________________________________________________________________________#  Locating relative path so that this code will work on both the Poll and Election Data
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv') #____________________________#  Locate csv relative path
with open(csvpath) as csv_file: #________________________________________________________#  Open csv file to begin analysis
    csvreader = csv.reader(csv_file, delimiter=',') #____________________________________#  Set syntax for csvreader given csv file type
    csv_header = next(csvreader) #_______________________________________________________#  Skip the header row
    # print(csvreader) #_________________________________________________________________#  Test Row _ confirmed that we are reading the file print(csvreader) and skipping headers
    
    for row in csvreader: #______________________________________________________________#  Initiate for loop to cycle through values in each row
        vote_count += 1
        if candidates.count(row[2]) > 0: #_______________________________________________#  populate list of candidate names across each votes
            candidatevotecast[candidates.index(row[2])] += 1
        else: 
            candidates.append(row[2])
            candidatevotecast.append(1)
#       print(candidates) #______________________________________________________________#   Test Row _ confirmed that we are reading the candidate name column, and that the column is in the winner order, prints winner order index for ever vote cast
#       print(candidatevotecast) #_______________________________________________________#   Test Row _ confirmed that we are counting votes cast for each candidate in our index, prints running total

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Print Blank row & Strings for the Title and Header line of the output table
print("") #__________________________________________________________________________#  Print Blank row, stylistic only
print("Election Results") #__________________________________________________________#  Print Title, stylistic only
print("______________________") #____________________________________________________#  Print Line Break, stylistic only
print("") #__________________________________________________________________________#  Print Blank row, stylistic only
print(f'Total Votes: {vote_count}') #________________________________________________#
print("______________________") #____________________________________________________#  Print Line Break, stylistic only
for n in range(len(candidates)):
    if candidatevotecast[n] > electedvotescast:
        electedname = candidates[n]
        electedvotescast = candidatevotecast[n]

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  output results to text file
#    text_file = open("PyBank_finalreport.txt", "w") #____________________________________#  create text file in same folder as main.py, assign variable to path
#    text_file.write('\n') #______________________________________________________________#
#    text_file.write('Financial Analysis\n') #____________________________________________#
#    text_file.write('----------------------------\n') #__________________________________#
#    text_file.write('\n') #______________________________________________________________#
#    text_file.write('Total Months: '+str(vote_count)+'\n') #____________________________#
#    text_file.write('Average Change: $'+'{:,.2f}'.format(avg_monthly_profit_change)+'\n')#
#    text_file.write('Total: $'+'{:,.2f}'.format(total_profit)+'\n') #____________________#
#    text_file.write('Greatest Increase in Profits: $'+'{:,.2f}'.format(max_monthly_profit_increase)+' ('+max_increase_month+')\n')
#    text_file.write('Greatest Decrease in Profits: $'+'{:,.2f}'.format(max_monthly_profit_decrease)+' ('+max_decrease_month+')\n') 
#    text_file.close() #__________________________________________________________________#