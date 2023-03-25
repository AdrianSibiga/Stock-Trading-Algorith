# This program grabs data via web scraping from openinsider.com and converts the data into a csv file for easy manipulation with the pandas library

import requests
from bs4 import BeautifulSoup
import csv

URL = "http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=1&cnt=100&page=3"

page_text = requests.get(URL).text # Request to access the website

soup = BeautifulSoup(page_text, "html.parser") # The raw html code from the website
table_tag = soup.find("table", class_ = "tinytable") # The table in which all of the purchases are kept
tbody_tag = table_tag.find("tbody") # The body of the table in which all of the purchases are kept (not including the headers)
tr_tags = tbody_tag.find_all("tr") # Each purchase is located in a tr tag. find_all method creates a list of all the purchases on the webpage (# of purchases can be customized)

data_list = [] # Initiate an empty list which will eventually contain lists of each row

for tr_tag in tr_tags: 
    
    td_tags = tr_tag.find_all("td") # Each column of the purchase has its own td tag. the find_all method creates a list of all the td tags within the given tr tag
    
    filing_date = td_tags[1].text       # 0
    trade_date = td_tags[2].text        # 1
    ticker_symbol = td_tags[3].text     # 2
    company_name = td_tags[4].text      # 3
    insider_title = td_tags[6].text     # 4
    price_bought = td_tags[8].text      # 5
    qty_in_shares = td_tags[9].text     # 6
    now_owned = td_tags[10].text        # 7         # After the listed purchase
    delta_owned = td_tags[11].text      # 8         # How many more shares the insider owns after this purchase, in %
    delta_value = td_tags[12].text      # 9         # How much more money was invested
    
    row = [filing_date, trade_date, ticker_symbol, company_name, insider_title, price_bought, qty_in_shares, now_owned, delta_owned, delta_value]
    data_list.append(row) # Creating a list of lists so that we can format it into a csv file
    print(row)
    
    with open("C:\Stock-Trading-Algorithm\scraping_data.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(data_list) # Turns the list of lists into a csv file called "scraping_data.csv". File will be overwritten if program runs again