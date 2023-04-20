import csv
import requests
import string
import time

scraping_data_name = 'test_samples/test_sample_100_(2-14-23_2-17-23).csv'

with open(scraping_data_name, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        ticker_symbol = row[2].strip()
        filing_date = row[0].replace(" ", "_").replace(":", "-")
        
        csv_url_1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker_symbol + '&interval=15min&slice=year1month2&apikey=OHLMGAI6A5CXX9Q3'
        csv_url_2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker_symbol + '&interval=15min&slice=year1month3&apikey=OHLMGAI6A5CXX9Q3'
        
        csv_filename = ticker_symbol + "___" + filing_date + ".csv"
        directory = "C:/Stock-Trading-Algorithm/stock_data/" + csv_filename
        
        with requests.Session() as s:
            download_1 = s.get(csv_url_1)
            download_2 = s.get(csv_url_2)
            decoded_content_1 = download_1.content.decode('utf-8')
            decoded_content_2 = download_2.content.decode('utf-8')
            cr_1 = csv.reader(decoded_content_1.splitlines(), delimiter=',')
            cr_2 = csv.reader(decoded_content_2.splitlines(), delimiter=',')
            my_list_1 = list(cr_1)
            my_list_2 = list(cr_2)
            with open(directory, "w", newline = "") as f:
                writer = csv.writer(f)
                writer.writerows(my_list_1)
                my_list_2.pop(0)
                writer.writerows(my_list_2)
                print(my_list_2)
        time.sleep(1)