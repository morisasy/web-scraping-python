import random # generate random number
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup

import pandas as pd # pip instal pandas
import re

# load the webpage content

URL = 'https://keithgalli.github.io/web-scraping/webpage.html'

def main():
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    #print(soup.prettify())
    # If you want to search for tags that match two or more CSS classes,
    # you should use a CSS selector
    links = soup.select("ul.socials a")
    # 1 option
    actual_links = [link['href'] for link in links]
    #print(actual_links)

    # 2 option
    findLinks = soup.find('ul', attrs={"class": "socials"})
    links = findLinks.find_all('a')
    aList = [link['href'] for link in links]
    print(aList)

    # 3 option
    links = soup.select("li.social a")
    aList = [link['href'] for link in links]
    print(aList)

    # grab data from table
    l = []
    table = soup.select("table.hockey-stats")[0]
    columns = table.find("thead").find_all("th")
    column_names = [c.string for c in columns]

    table_rows = table.find('tbody').find_all("tr")
    for tr in table_rows:
        td = tr.find_all('td')
        row = [str(tr.get_text()).strip() for tr in td]
        l.append(row)
    #print(l)

    df = pd.DataFrame(l, columns = column_names)
    df.head()

    #print(df)

    # Grab all fun facts that use word 'is'

    facts = soup.select('ul.fun-facts li')
    facts_with_is = [fact.find(string = re.compile("is")) for fact in facts]
    facts_with_is = [fact.find_parent().get_text for fact in facts_with_is if fact]
    print(facts_with_is)

    # solve challenge
    url = 'https://keithgalli.github.io/web-scraping/'
    files = soup.select("div.block a")
    relative_files = [f['href'] for f in files]
    for f in relative_files:
        full_url = url + f
        page = requests.get(full_url)
        from bs4 import BeautifulSoup  as bs
        soup = bs(page.content, 'html.parser')
        secret_word_element = soup.find('p', attrs ={'id': "secret-word"})
        secret_word = secret_word_element.string
        print(secret_word)
        break
    #print(relative_files)
    #print(files)



if __name__ == '__main__':
    main()
