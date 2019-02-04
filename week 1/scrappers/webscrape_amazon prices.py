import requests
from bs4 import BeautifulSoup
import pprint
import pymysql
from user_agent import generate_user_agent
pp = pprint.PrettyPrinter(indent=4)


def Sandisk(headers):
    url = "https://www.amazon.com/SanDisk-128GB-microSDXC-Memory-Adapter/dp/B073JYC4XM/ref=sr_1_1?s=electronics&ie=UTF8&qid=1549278114&sr=1-1"
    test_url = requests.get(url, headers=headers)
    readHTML = test_url.text
    soup = BeautifulSoup(readHTML, "html.parser")
    name = soup.find('div', attrs={'id': 'titleSection'})
    cost = soup.find('span', attrs={'id': 'priceblock_ourprice'}).text.strip()
    string_price = (cost.get_text(strip=True).lstrip("$"))
    print(name)
    print(string_price)
    database_connection(name, cost)


def database_connection(name, cost):
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="amazon_products")
    myCursor = conn.cursor()
    # myCursor.execute(""" CREATE TABLE price
    #	(id int primary key,name varchar(20),price varchar(20),date_on date)
    #	""")
    myCursor.execute("INSERT INTO price(name,price,date_on) VALUES(name,cost,curdate())")
    conn.commit()
    conn.close()


if __name__ == '__main__':

    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    Sandisk(headers)
