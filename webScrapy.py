from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from googlesearch import search
from webdriver_manager.chrome import ChromeDriverManager

# it will directly install chromeDriveManager into the system
driver = webdriver.Chrome(ChromeDriverManager().install())
Names = []  # List to store name of the product
company = []  # List to store price of the product
Location = []  # List to store rating of the product
driver.get('https://thebrokerlist.com/search_profiles?lightbox=0&order=profiles.last_sign_in_at+DESC&page=10')

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# results = soup.find("div", {"class": "listing"})
# print(results.prettify())

for EachPart in soup.find_all("li", {"class": "profile_search_result_item"}):
    name = EachPart.find('div', attrs={'class': 'broker_name'})
    Company = EachPart.find('div', attrs={'class': 'businesses'})
    Location = EachPart.find('div', attrs={'class': 'location'})

    # print('PersonName: ' + name.text + ' Company: ' + Company.text + ' Location: ' + Location.text)
    Names.append(name.text)
    company.append(Company.text)
df = pd.DataFrame({'Name': Names, 'company': company})
df.to_csv('products.csv', mode='a', index=False, encoding='utf-8')
