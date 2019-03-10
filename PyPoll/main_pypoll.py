#__Thank yous and Acknowledgements_______________________________________________________# 
#__I'm still having trouble with building loops, Alex and Ashraf helped tremendously_____# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 


#________________________________________________________________________________________#  Import Modules
import os #______________________________________________________________________________#  Import os to assist with reading relative paths on different computers
import csv #_____________________________________________________________________________#  Import csv so that we can read content of election_data.csv

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Declaring Variables that will impact all code, 
row = [] #_______________________________________________________________________________#  Declaring 'row' as an empty list that will later point to each row in the csv, also could be called "votes"
candidates = [] #________________________________________________________________________#  Declaring 'candidate' as an empty list that will later point to each candidate the csv
candidatevotecast = [] #_________________________________________________________________#  Declaring 'candidatevotecast' as an empty list that will later point to each candidate the c
vote_count = 0 #_________________________________________________________________________#  Declaring 'vote_count' as a integer with a value of 0 to start sum of vote count
electedvotescast = 0 #___________________________________________________________________#  Declaring 'electedvotescast' as a integer with a value of 0 to start sum of electedvotescast per candidate

#________________________________________________________________________________________#  
#________________________________________________________________________________________#  Locating relative path so that this code will work on both the Poll and Election Data
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv') #____________________________#  Locate csv relative path
with open(csvpath) as csv_file: #________________________________________________________#  Open csv file to begin analysis
    csvreader = csv.reader(csv_file, delimiter=',') #____________________________________#  Set syntax for csvreader given csv file type
    csv_header = next(csvreader) #_______________________________________________________#  Skip the header row
    # print(csvreader) #_________________________________________________________________#  Test Row _ confirmed that we are reading the file print(csvreader) and skipping headers
    
    for row in csvreader: #______________________________________________________________#  Initiate for loop to cycle through values in each row
        vote_count += 1 #________________________________________________________________#  Continuously sum each row as a way to count total votes
        if candidates.count(row[2]) > 0: #_______________________________________________#  Loop to perform action as loong as the candidate column is blank
            candidatevotecast[candidates.index(row[2])] += 1 #___________________________#  Continuously sum each count of a candidate's name as a vote count and index within the candidatevotecast list
        else: 
            candidates.append(row[2]) #__________________________________________________#  Store all of the candidate names as a list
            candidatevotecast.append(1) #________________________________________________#  Store all of the vote count totals as a list
#       print(candidates) #______________________________________________________________#  Test Row _ confirmed that we are reading the candidate name column, and that the column is in the winner order, prints winner order index for ever vote cast
#       print(candidatevotecast) #_______________________________________________________#  Test Row _ confirmed that we are counting votes cast for each candidate in our index, prints running total

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Print Blank row & Strings for the Title and Header line of the output table
print("") #______________________________________________________________________________#  Print Blank row, stylistic only
print("Election Results") #______________________________________________________________#  Print Title, stylistic only
print("______________________") #________________________________________________________#  Print Line Break, stylistic only
print("") #______________________________________________________________________________#  Print Blank row, stylistic only
print(f'Total Votes: {vote_count}') #____________________________________________________#  Print "Total Votes: " and vote count result
print("______________________") #________________________________________________________#  Print Line Break, stylistic only
print("") #______________________________________________________________________________#  Print Blank row, stylistic only
for n in range(len(candidates)): #_______________________________________________________#  Loop through the candidates list from the start to the end
    print(f"{candidates[n]}: {(100*candidatevotecast[n]/vote_count):.3f}% ({candidatevotecast[n]})") # Print out Candidate Name, the calculated vote share per candidate, and the total votes each candidate received 
    if candidatevotecast[n] > electedvotescast: #________________________________________#  The If clause sorts the candidates by number of votes they received in descending order
        electedname = candidates[n] #____________________________________________________#  Thank you to Alex and Ashraf for the support here, 
        electedvotescast = candidatevotecast[n] #________________________________________#  this formatting is much more efficient than anything I could come up with
#       print(electedname) #_____________________________________________________________#  Test Row _ confirmed that we are reading the elected candidates name
#       print(electedvotescast) #________________________________________________________#  Test Row _ confirmed that we are reading the elected candidates vote count

print("______________________") #________________________________________________________#  Print Line Break, stylistic only
print("") #______________________________________________________________________________#  Print Blank row, stylistic only
print(f'Winner: {electedname}') #________________________________________________________#
print("______________________") #________________________________________________________#  Print Line Break, stylistic only
print("") #______________________________________________________________________________#  Print Blank row, stylistic only

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  output results to text file
text_file = open("PyPoll_finalvotetally.txt", "w") #_____________________________________#  create text file in same folder as main.py, assign variable to path
text_file.write('\n') #__________________________________________________________________#  Print Break, stylistic only
text_file.write('Election Results\n') #__________________________________________________#  Print Report header
text_file.write('----------------------------\n') #______________________________________#  Print Line Break, stylistic only
text_file.write('\n') #__________________________________________________________________#
text_file.write('Total Votes: '+str(vote_count)+'\n') #__________________________________#
text_file.write('----------------------------\n') #______________________________________#  Print Line Break, stylistic only  
text_file.write((candidates[0])+': '+str(round((100*candidatevotecast[0]/vote_count), 4))+'% ('+str((candidatevotecast[0]))+')'+'\n')
text_file.write((candidates[1])+': '+str(round((100*candidatevotecast[1]/vote_count), 4))+'% ('+str((candidatevotecast[1]))+')'+'\n')
text_file.write((candidates[2])+': '+str(round((100*candidatevotecast[2]/vote_count), 4))+'% ('+str((candidatevotecast[2]))+')'+'\n')
text_file.write((candidates[3])+': '+str(round((100*candidatevotecast[3]/vote_count), 4))+'% ('+str((candidatevotecast[3]))+')'+'\n')
text_file.write('----------------------------\n') #______________________________________#  Print Line Break, stylistic only 
text_file.write('Winner: '+str(electedname)+'\n') #______________________________________#
text_file.write('----------------------------\n') #______________________________________#  Print Line Break, stylistic only 
text_file.close() #______________________________________________________________________#