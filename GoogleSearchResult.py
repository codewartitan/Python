from googlesearch import search
import pandas as pd

Names = []  # List to store name of the product
company = []  # List to store price of the product
Links = []  # # List to store links
df = pd.read_csv('listingsites.csv')
names = df['Name']
companyNames = df['company']

# print(companyNames)

# install google libaray for googleSearch to work

# dataset = 'planning Commission' + 'CHEROKEE' + 'ga' + 'US'
#
#
for names in companyNames:
    for url in search(names, tld='com', stop=1):
        # print(url)
        Links.append(url)
        # Names.append(df['Name'])
        # company.append(df['company'])

df = pd.DataFrame({'Name': df['Name'], 'company': df['company'], 'Links': Links})
df.to_csv('CompanyLinks.csv', index=False, encoding='utf-8')
