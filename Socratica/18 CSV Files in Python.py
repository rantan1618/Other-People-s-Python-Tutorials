# Comma
# Seperated
# Values
# A Popular format for storing data.
# A CSV is a text file that contains data.
# Often times the first row(line) of a file is a header, 
# letting you know what the values represent.
# The remaining lines contain the data, 
# think of each line as a record in a database.
# Note: Because this is a text file there are no datatypes.
# While you may mentally interperate the data as strings, dates and numbers,
# Everything is represented as a string.
# When you read a CSV it will be your responsability to convert the data
# into the correct datatypes.
# Also: When you see two commas in a row that means there is data missing.
# ,,

# today we will learn how to read and write CSVs.
# We will show you how to use the python CSV module by reading a file
# with the first 10 years of Google Stock Data.

# Next, we will analyze the data.
# We will then write the results into a new CSV.
# 
# Here's the path to the google stock data on my computer:
# path = "Other Peoples Tutorials\Socratica\google_stock_data.csv"

# You can use the open() function to display the contents of the file.
'''
file = open(path)
for line in file:
    print(line)
'''
# There is indeed a lot of data there.
# To be useful however we need to store the data.
# we will show you two ways to do this, with and without the CSV module.
# Let us first parse the data without using the CSV module.

# We can quickly read the contents of the file by using a list comprehension.
# lines =  [line for line in open(path)]

# print(lines[0])

# Notice that each line is treated as a single string.
# print(lines[1])

# We can use the strip method to remove any leading or trailing white-space.
# print(lines[0].strip())

# and we can use the split function to divide the string into smaller pieces.
# Just pass in the string or character to partition on.
# print(lines[0].strip().split(','))

# dataset = [line.strip().split(',') for line in open(path)]
# print(dataset[0])
# print(dataset[1])

import csv
from datetime import datetime

# print(dir(csv))
'''
['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 
'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', 
'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', '__version__', 'excel', 'excel_tab', 
'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 
'unix_dialect', 'unregister_dialect', 'writer']
'''
 # Today we will focus on the reader() and writer() functions

path2 = "Other Peoples Tutorials\Socratica\google_stock_data.csv"
file = open(path2, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])

# There is still a problem with this method, the data is still read as strings. We need to convert it to the specific types.

data = []
for row in reader:
    # row  = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # 'open' is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])
    
    # In finance, a Stock Return is just the % percent change in price.
    # A Daily return is the change from one day to the next.
    # People also look at weekly
    # Monthly
    # Quaterly
    # Annual
    # Today we will only consider daily returns.
    # We will store the data that we compute in a file called  "google_returns.csv"
    # Compute and store daily returns.
returns_path = "Other Peoples Tutorials\Socratica\google_returns_data.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
    # To write a row call the write row method with a list of values.
    # Let's first write the header.
writer.writerow(["Date", "Return"])

# We need the adjusted price for two consective days.
# So instead of looping over the data list which would give us only one row at a time
# Let's create a for loop with an index instead.

for i in range(len(data) - 1):
    todays_row = data[i]
    today_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[1+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    write.writerow([formatted_date, daily_return])