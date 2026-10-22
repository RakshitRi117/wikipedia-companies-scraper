"""
Wikipedia Companies Scraper
---------------------------
Scrapes the table "List of largest companies in the United States by revenue"
from Wikipedia and saves it as a CSV file.

Libraries: requests, beautifulsoup4, pandas
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {
    #a more descriptive User-Agent (Wikipedia asks for this)
    "User-Agent": "wiki-companies-scraper/1.0 (learning project; https://github.com/<your-username>)"
    }
page = requests.get(url, headers = headers)
page.raise_for_status()
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup) --> prints whole html file
# lets fetch all the tables then we will use indexing to find our working table
table = soup.find_all('table')[0] 

rows = table.find_all('tr') 

# extracting column headers
total_columns = rows[0].find_all('th')
colm_names = [word.text.strip() for word in total_columns]
df = pd.DataFrame(columns = colm_names)

#extract rows from table
for row in rows[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data # think as appending data into df by each row

# lets upload this to csv
df.to_csv(r'C:\Users\YourName\Documents\Companies.csv', index = False)
print("Done! Saved", len(df), "rows to Companies.csv")
