import csv
import string
import time
import datetime

#purchase_file = 'test_samples/test_sample_100_(2-14-23_2-17-23).csv'
purchase_file = 'test_samples/test_sample_5.csv'


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
        

        # turns the lists of characters into strings for finding the file
        date_name = "".join(date)
        clock_name = "".join(clock)

        # creates a stock_data_file for iterating through the times for each stock
        stock_data_file = 'stock_data/'+ticker_symbol.strip(" ")+'___'+date_name+'_'+clock_name.replace(":", "-")+'.csv'

        # round the minute to the nearest 15 minute interval
        minute = int(clock[3]+clock[4])
        if (0 <= minute <= 14):
            clock[3] = '0'
            clock[4] = '0'
        elif (15 <= minute <= 29):
            clock[3] = '1'
            clock[4] = '5'
        elif (30 <= minute <= 44):
            clock[3] = '3'
            clock[4] = '0'
        elif (45 <= minute <= 59):
            clock[3] = '4'
            clock[4] = '5'
        
        # Need to make so it shows the next day if filing date is at off hours

        # seconds = 00
        clock[6] = '0'
        clock[7] = '0'

        # turns the lists of characters into strings with the rounded minutes and 00 seconds
        date = "".join(date)
        clock = "".join(clock)
        
        # puts the filing date into the datetime system so that we can do easy date manipulations by days, months, hours, etc.
        filing_date_time = datetime.datetime.fromisoformat(date+"T"+clock)

        print(filing_date_time, ticker_symbol)

        with open(stock_data_file, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                if row[0] == str(filing_date_time):
                    print(filing_date_time, stock_data_file)