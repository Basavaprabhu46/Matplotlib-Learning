import pandas as pd

 
from matplotlib import pyplot as plt

# flights=pd.read_csv("dataset/flights.csv")

# year=flights["year"]
# passengers=flights["passengers"]

# plt.plot(year,passengers,label='passengers per year')
# plt.xlabel("year")
# plt.ylabel("passengers")


tips=pd.read_csv("dataset/tips.csv")
tip=tips["tip"].sort_values(ascending=True)
total_bill=tips["total_bill"].sort_values(ascending=True)
size=tips.sort_values(by='tip')['size']
# format Strings
# a format string consists of a part of colot , marker and a line
#  fmt='[marker'][line][color]'
# u can use this in plt.plot() eg below used is 'ob--' 
# ( o is marker, b is blue , -- is dashed)
# u can do that cleanly like:
# color='blue' , linestyle='--' , marker='o'

print(tips.sort_values(by='total_bill',ascending=True))
plt.plot(total_bill,tip,color='black',label="tips by total bill")
plt.grid()
plt.bar(total_bill,size,color='orange',label='size')
plt.legend()

plt.savefig('plot.png')

plt.show()
