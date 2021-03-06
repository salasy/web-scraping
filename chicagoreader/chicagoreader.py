from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import unicodecsv as csv

BASE_URL = "http://www.chicagoreader.com"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')

def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.find_all('dd')]
    return category_links
    
def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find('h1', 'headline').string
    winner = [h2.string for h2 in soup.find_all('h2', 'boc1')]
    runners_up = [h2.string for h2 in soup.find_all('h2', 'boc2')]
    return {'category': category,
            'category_url': category_url,
            'winner': winner,
            'runners_up': runners_up}
            
if __name__ == '__main__':
    food_n_drink = ('http://www.chicagoreader.com/chicago/'
                    'best-of-chicago-2011-food-drink/BestOf?oid=4106228')
                    
    categories = get_category_links(food_n_drink)
    
    data = []
    for category in categories:
        winner = get_category_winner(category)
        data.append(winner)
        sleep(1)
        
    #print data
    keys = data[0].keys()
    with open('chicagoreader.csv', 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
