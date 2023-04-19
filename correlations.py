import csv
import string
import time
import datetime

purchase_file = 'test_samples/test_sample_5.csv'
stock_data_file = 'stock_data/AFBI___2023-02-16_12-27-07.csv'


# finds filing dates of each purchase in the purchase file and turns them into strings
with open(purchase_file, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        filing_date = row[0]
        ticker_symbol = row[2]
        
        # initiate lists
        date = []
        clock = []
        
        # gathers the characters of the filing date
        for i in range(0,10):
            date.append(filing_date[i])
        for i in range(11,19):
            clock.append(filing_date[i])
        
        # turns the lists of characters into strings
        date = "".join(date)
        clock = "".join(clock)
        
        # puts the filing date into the datetime system so that we can do easy date manipulations by days, months, hours, etc.
        filing_date = datetime.datetime.fromisoformat(date+"T"+clock)
        # creates a stock_data_file for iterating through the times for each stock
        stock_data_file = 'stock_data/'+ticker_symbol.strip(" ")+'___'+date+'_'+clock.replace(":", "-")
        
        
        print(stock_data_file)
# with open(stock_data_file, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
        