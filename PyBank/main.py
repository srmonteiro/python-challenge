import os
import csv

csvpath = os.path.join('..', 'PyBank','budget_data.csv')

with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    # line_count = 0
    # for row in csv_reader:
       # next(csv_reader, None)  

        # if line_count == 0:
        #    print(f'Column names are {", ".join(row)}')
       #     line_count += 1
      #  else:
     #       print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #        line_count += 1
   # print(f'Processed {line_count} lines.')