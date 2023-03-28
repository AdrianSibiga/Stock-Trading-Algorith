import requests
import csv
import string

ticker_symbol = "LGTO"
filing_date = "###"

csv_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker_symbol + '&interval=15min&slice=year1month1&apikey=OHLMGAI6A5CXX9Q3'
csv_filename = ticker_symbol + "___" + filing_date + ".csv"
directory = "C:/Stock-Trading-Algorithm/" + csv_filename

with requests.Session() as s:
    download = s.get(csv_url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    with open(directory, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(my_list)