import random # generate random number
import requests # pip install requests
from bs4 import BeautifulSoup as bs # pip install beautifulsoup

import pandas as pd # pip instal pandas
import re

# load the webpage content

URL = 'https://keithgalli.github.io/web-scraping/'

def main():
    r = requests.get(URL+"webpage.html")

    page = bs(r.content, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster
    #print(page.content)

    #print(page.prettify())
    # If you want to search for tags that match two or more CSS classes,
    # you should use a CSS selector
    images = page.select("div.row div.column img")
    image_url = images[0]['src']
    full_url= URL + image_url
    img_data =requests.get(full_url).content

    with open('lake_como.jpg', 'wb') as f:
        f.write(img_data)
    #print(images)



if __name__ == '__main__':
    main()
