import requests
from bs4 import BeautifulSoup

URL = "http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=25&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=1&cnt=100&page=1"

page_text = requests.get(URL).text

soup = BeautifulSoup(page_text, "html.parser")
table_tag = soup.find("table", class_ = "tinytable") # The table in which all of the purchases are kept
tbody_tag = table_tag.find("tbody") # The body of the table in which all of the purchases are kept (not including the headers)
tr_tags = tbody_tag.find_all("tr") # Each purchase is located in a tr tag. find_all method creates a list of all the purchases on the webpage (# of purchases can be customized)
for tr_tag in tr_tags: 
    td_tags = tr_tag.find_all("td") # Each column of the purchase has its own td tag. the find_all method creates a list of all the td tags within the given tr tag
    filing_date = td_tags[1].next_element.next_element.text # Found this to be the only way to get the element I wanted. Basically the filing date is held in an "a" tag which is inside of a "div" tag. And I put .text at the end to only get the text and not the other html code
    print(filing_date)
