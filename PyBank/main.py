#__Thank yous and Acknowledgements_______________________________________________________# 
#__Kerry provided patient support with structuing loops and formatting best practices ___# 
#__Brickey helped me significantly with the loop for the Average Profit/Loss, ___________# 
#__particularly with how to skip the first value. Brickey's recommendation to use the ___# 
#__statistics module was very helpful - he has a knack for finding better solutions _____# 
#__outside our in-class toolkit._________________________________________________________# 
#________________________________________________________________________________________#


#________________________________________________________________________________________#  Import Modules
import os #______________________________________________________________________________#  Import os to assist with reading relative paths on different computers
import csv #_____________________________________________________________________________#  Import csv so that we can read content of budget_data.csv
import statistics #______________________________________________________________________#  Import csv to perform operations like average, min, and max

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Declaring Variables, Lists, etc
row = [] #_______________________________________________________________________________#  Declaring 'row' as an empty list that will store each to loop through the rows in the csv
profit = [] #____________________________________________________________________________#  Declaring 'profit' as an empty list that will store each value in the profit/loss the csv
month = [] #_____________________________________________________________________________#  Declaring 'month' as an empty list to that will store month names
total_profit = 0 #_______________________________________________________________________#  Declaring 'total_profit' as a integer with a value of 0, to use in loops when summing Profit/Loss and calculating the average Profit/Loss each month
monthly_profit_change = 0 #______________________________________________________________#  Declaring 'monthly_profit_change' to calculate Profit/Loss each month and average Profit/Loss 
monthly_profit_change_list = [] #________________________________________________________#  Declaring 'monthly_profit_change_list' to store 'monthly_profit_change' values
monthly_profit_lastmonth = 0 #___________________________________________________________#  Declaring 'monthly_profit_lastmonth' to substract from 'thismonth' in average profit calculations
monthly_profit_thismonth = 0 #___________________________________________________________#  Declaring 'monthly_profit_thismonth' to calculate average profit
avg_monthly_profit_change = 0 #__________________________________________________________#  Declaring 'avg_monthly_profit_change' to store result of statistic.mean on 'monthly_profit_change_list'
max_monthly_profit_increase = 0 #________________________________________________________#  Declaring 'max_monthly_profit_increase' to store result of max on 'monthly_profit_change_list'
max_monthly_profit_decrease = 0 #________________________________________________________#  Declaring 'max_monthly_profit_decrease' to store result of min on 'monthly_profit_change_list'
max_increase_month = () #________________________________________________________________#  Declaring 'max_increase_month' to store paired index result of 'max_monthly_profit_increase' so that I can also print out the month
max_decrease_month = () #________________________________________________________________#  Declaring 'max_decrease_month' to store paired index result of 'max_monthly_profit_decrease' so that I can also print out the month
skip_start_month = True #________________________________________________________________#  Declaring 'skip_start_month'

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
        month.append(row[0]) #___________________________________________________________#  Create a list that stores all of the month valutes
        total_profit += float(row[1]) #__________________________________________________#  Continuously sum the values in the Profit/Loss column and store as "total_profit" 
        if skip_start_month == False: #__________________________________________________#  This loop is intentionally set to False so that we skip the first value when calculating statistic.mean
            monthly_profit_change = float(row[1]) - monthly_profit_lastmonth #___________#  Take the value in the current row Profit/Loss column, subtract the previous month value and store as 'monthly_profit_change'
            monthly_profit_change_list.append(monthly_profit_change) #___________________#  Store the current 'monthly_profit_change' as the next term in the list 'monthly_profit_change_list'
        monthly_profit_lastmonth = float(row[1]) #_______________________________________#  Reset the value of 'lastmonth' now that we are moving on to next month
        if skip_start_month == True: #___________________________________________________#  A dumby loop used to skip the first value when cacluating statistic.mean
            skip_start_month = False #___________________________________________________#  Thanks again, Brickey!!! I was really stuck here! I guess I was the real dumby!

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  
    avg_monthly_profit_change = statistics.mean(monthly_profit_change_list) #____________#  Use the statistics.mean function to calculate the average profit/loss per month and store as avg_monthly_profit_change
    max_monthly_profit_increase = max(monthly_profit_change_list) #______________________#  Use the max function to calculate the greatest profit/loss per month and store as max_monthly_profit_increase
    max_monthly_profit_decrease = min(monthly_profit_change_list) #______________________#  Use the min function to calculate the lowest profit/loss per month and store as max_monthly_profit_decrease
    max_increase_index = monthly_profit_change_list.index(max_monthly_profit_increase) #_#  Get the paired index number of the max_monthly_profit_increase month
    max_decrease_index = monthly_profit_change_list.index(max_monthly_profit_decrease) #_#  Get the paired index number of the max_monthly_profit_decrease month
    max_increase_month = month[(max_increase_index + 1)] #_______________________________#  Now we take the max_monthly_profit_increase index to print out the month
    max_decrease_month = month[(max_decrease_index + 1)] #_______________________________#  Finally we take the max_monthly_profit_decrease index to print out the month

#________________________________________________________________________________________# 
#________________________________________________________________________________________#  Print Blank row & Strings for the Title and Header line of the output table
    print("") #__________________________________________________________________________#  Print Blank row, stylistic only
    print("Financial Analysis") #________________________________________________________#  Print Title, stylistic only
    print("______________________") #____________________________________________________#  Print Line Break, stylistic only
    print("") #__________________________________________________________________________#  Print Blank row, stylistic only
    print(f'Total Months: {month_count}') #______________________________________________#  Print out an f-string with Total Months and month_count
    print('Average: $' + '{:,.2f}'.format(avg_monthly_profit_change)) #__________________#  Print out string with Average - thanks again to Brickey for the 2f formatthing. I couldn't make it work with an f-string.
    print('Total: $' + '{:,.2f}'.format(total_profit)) #_________________________________#  Print out string with Total Profit . I couldn't make it work with an f-string.
    print('Greatest Increase in Profits: $' + '{:,.2f}'.format(max_monthly_profit_increase)+' ('+max_increase_month+')') #_# Print out string with Greatest Increase 
    print('Greatest Decrease in Profits: $' + '{:,.2f}'.format(max_monthly_profit_decrease)+' ('+max_decrease_month+')') #_# Print out string with Greatest Increase 

#________________________________________________________________________________________#  Now do it all over again with an txt file
#________________________________________________________________________________________# 
    text_file = open("PyBank_finalreport.txt", "w") #____________________________________#  
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