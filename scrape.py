# no need to interact with the browser, just get the content -> bs4
from bs4 import BeautifulSoup as bs
import html5lib
import requests
import re
import csv
import datetime

# retreive the barbie page
barbieURL = "https://www.boxofficemojo.com/title/tt1517268/credits/"
barbiePage = requests.get(barbieURL)
barbieSoup = bs(barbiePage.content, "html5lib")
# retreive the oppenheimer page
oppURL = "https://www.boxofficemojo.com/title/tt15398776/"
oppPage = requests.get(oppURL)
oppSoup = bs(oppPage.content, "html5lib")

# find the domestic box office 
barbieMoney = barbieSoup(class_="money")
barbieBox = barbieMoney[0].string
barbieBox_nc = int(re.sub("[,,$]", "", barbieBox))/1000000

oppMoney = oppSoup(class_="money")
oppBox = oppMoney[0].string
oppBox_nc = int(re.sub("[,,$]", "", oppBox))/1000000

print(f"Barbie has grossed {barbieBox} as of today.")
print(f"Oppenheimer has grossed {oppBox} as of today.")

# write to csv
row = [datetime.datetime.now().strftime("%m/%d"), barbieBox_nc, oppBox_nc]
with open("./data.csv", "a") as data:
    # make a writer
    writer = csv.writer(data)
    # write the row
    writer.writerow(row)
