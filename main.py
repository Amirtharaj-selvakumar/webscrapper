import requests
from bs4 import BeautifulSoup

# Make a request to the news website
news_url = 'https://www.flipkart.com/gaming/gaming-laptops/pr?sid=4rr,tz1&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_706278fc-30c9-4d92-bd27-27164b0c5aff_1_372UD5BXDFYS_MC.0OOCG5J6F9WH&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop~Gaming%2BLaptops_0OOCG5J6F9WH&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=0OOCG5J6F9WH'
response = requests.get(news_url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
s = soup.find('div', class_='_1AtVbE')

# Extract the news headlines
Pdetails = []
names = []
descr = []
prices = []
urls = []
srcs = []
for name in soup.find_all('div', class_='_4ddWXP'):
    Pname = name.find('a', class_='s1Q9rs').text
    names.append(Pname)
    url = name.find('a', class_='s1Q9rs').get('href')
    urls.append(url)
for desc in soup.find_all('div', class_='_3Djpdu'):
    Pdesc = desc.text
    descr.append(Pdesc)
for price in soup.find_all('div', class_='_30jeq3'):
    Pprice = price.text
    prices.append(Pprice)
for image in soup.find_all('div', class_='CXW8mj'):
    image_src = image.find('img').get('src')
    srcs.append(image_src)

length = len(names)
for i in range(length):
    Pdetails.append({
        'name':names[i],
        'desc':descr[i],
        'price':prices[i],
        'url':urls[i],
        'src':srcs[i]
    })
# Store the data in a dictionary or in a database
# ...
# Render the data on a web page using Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', Pdetails=Pdetails)


if __name__ == '__main__':
    app.run()
