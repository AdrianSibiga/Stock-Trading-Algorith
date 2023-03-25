# import csv

# filename = "yoyo.csv"
# directory = "C:/Stock-Trading-Algorithm/stock_data/" + filename

# data_list = [[1,2,3,4,5],[6,7,8,9,10]]

# with open(directory, "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data_list)
import string

x = "Hello: World"

y = x.replace(" ", "_").replace(":", "-")
print(y)