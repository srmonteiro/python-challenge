#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 
#________________________________________________________________________________________# 


#________________________________________________________________________________________#  Import Modules
import os #______________________________________________________________________________#  Import os to assist with reading relative paths on different computers
import csv #_____________________________________________________________________________#  Import csv so that we can read content of budget_data.csv
import statistics #______________________________________________________________________#  Import csv to perform operations like average, min, and max

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Declaring Variables that will impact all code, 
row = [] #_______________________________________________________________________________#  Declaring 'row' as an empty list that will later point to each row in the csv
profit = [] #____________________________________________________________________________#  Declaring 'profit' as an empty list that will later point to each vain the csv
total_profit = 0 #_______________________________________________________________________#  Declaring 'total_profit' as a integer with a value of 0, to use in loops when summing Profit/Loss and calculating the average Profit/Loss each month
monthly_profit_change = 0 #______________________________________________________________#  Declaring 'monthly_profit_change' to calculate Profit/Loss each month and average Profit/Loss 
monthly_profit_change_list = [] #________________________________________________________#
monthly_profit_lastmonth = 0 #___________________________________________________________#  
monthly_profit_thismonth = 0 #___________________________________________________________#  
avg_monthly_profit_change = 0 #__________________________________________________________# 
max_monthly_profit_increase = 0 #________________________________________________________# 
max_monthly_profit_decrease = 0 #________________________________________________________#
max_increase_month = () #________________________________________________________________#
max_decrease_month = () #________________________________________________________________#
month = [] #_____________________________________________________________________________#
skip_start_month = True

#________________________________________________________________________________________#  
#________________________________________________________________________________________#  Locating relative path so that this code will work on both the Poll and Election Data
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv') #______________________________#  Locate csv relative path
with open(csvpath) as csv_file: #________________________________________________________#  Open csv file to begin analysis
    csvreader = csv.reader(csv_file, delimiter=',') #____________________________________#  Set syntax for csvreader given csv file type
    csv_header = next(csvreader) #_______________________________________________________#  Skip the header row
    # print(csvreader) #_________________________________________________________________#  Test Row _ confirmed that we are reading the file print(csvreader) and skipping headers
    data = list(csvreader) #_____________________________________________________________#  Transform csvreader into list "data" so that we can perform functions on the values in each csv column
    month_count = len(data) #____________________________________________________________#  Store the total amount of months (rows) as "month_count" and to use to calculate averages

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Initiate for loop to cycle through values in each row
    for row in data: #___________________________________________________________________#  Initiate for loop to cycle through values in each row
        month.append(row[0]) #___________________________________________________________#  populate list of dates 
        total_profit += float(row[1]) #__________________________________________________#  Continuously sum the values in the Profit/Loss column and store as "total_profit" 
        if skip_start_month == False: #__________________________________________________#
            monthly_profit_change = float(row[1]) - monthly_profit_lastmonth #___________# 
            monthly_profit_change_list.append(monthly_profit_change) #___________________# 
        monthly_profit_lastmonth = float(row[1]) #_______________________________________#
        if skip_start_month == True: #___________________________________________________#
            skip_start_month = False #___________________________________________________#

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  
    avg_monthly_profit_change = statistics.mean(monthly_profit_change_list) #____________# 
    max_monthly_profit_increase = max(monthly_profit_change_list) #______________________# 
    max_monthly_profit_decrease = min(monthly_profit_change_list) #______________________# 
    max_increase_index = monthly_profit_change_list.index(max_monthly_profit_increase) #_# get index number
    max_decrease_index = monthly_profit_change_list.index(max_monthly_profit_decrease) #_#
    max_increase_month = month[(max_increase_index + 1)] #_______________________________# use index number to identify month/year
    max_decrease_month = month[(max_decrease_index + 1)] #_______________________________# (+1 because we don't have pl_change for first month)

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Print Blank row & Strings for the Title and Header line of the output table
    print("") #__________________________________________________________________________#  Print Blank row, stylistic only
    print("Financial Analysis") #________________________________________________________#  Print Title, stylistic only
    print("______________________") #____________________________________________________#  Print Line Break, stylistic only
    print("") #__________________________________________________________________________#  Print Blank row, stylistic only
    print(f'Total Months: {month_count}') #______________________________________________#
    print('Average: $' + '{:,.2f}'.format(avg_monthly_profit_change)) #__________________#
    print('Total: $' + '{:,.2f}'.format(total_profit)) #_________________________________#
    print('Greatest Increase in Profits: $' + '{:,.2f}'.format(max_monthly_profit_increase)+' ('+max_increase_month+')') #_# 
    print('Greatest Decrease in Profits: $' + '{:,.2f}'.format(max_monthly_profit_decrease)+' ('+max_decrease_month+')') #_# 

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  output results to text file
    text_file = open("PyBank_finalreport.txt", "w") #____________________________________#  create text file in same folder as main.py, assign variable to path
    text_file.write('\n') #______________________________________________________________#
    text_file.write('Financial Analysis\n') #____________________________________________#
    text_file.write('----------------------------\n') #__________________________________#
    text_file.write('\n') #______________________________________________________________#
    text_file.write('Total Months: '+str(month_count)+'\n') #____________________________#
    text_file.write('Average Change: $'+'{:,.2f}'.format(avg_monthly_profit_change)+'\n')#
    text_file.write('Total: $'+'{:,.2f}'.format(total_profit)+'\n') #____________________#
    text_file.write('Greatest Increase in Profits: $'+'{:,.2f}'.format(max_monthly_profit_increase)+' ('+max_increase_month+')\n')
    text_file.write('Greatest Decrease in Profits: $'+'{:,.2f}'.format(max_monthly_profit_decrease)+' ('+max_decrease_month+')\n') 
    text_file.close() #__________________________________________________________________#