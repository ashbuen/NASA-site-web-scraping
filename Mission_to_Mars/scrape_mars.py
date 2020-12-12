# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init_browser():
    executable_path = {'exectuable_path': "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars = {}

# Url
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

# HTML object
    html = browser.html

# Parser the html
    soup = bs(html, "html.parser")
    print(soup.prettify())
    
# Scrape latest title
    latest_title = soup.select('div.content_title')[1]
    latest_title

# Scrape paragraph of latest title
    latest_paragraph = soup.find_all('div', 'article_teaser_body')[0]
    latest_paragraph

# Quit Mars scraping
    browser.quit()

# Splinter setup for JPL
    executable_path = {'executable_path' : "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless = False)

# JPL Url
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html = browser.html
    soup = bs(html, 'html.parser')
    print(soup.prettify())

# JPL featured image
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA09178_ip.jpg'

# Quit JPL browser
    browser.quit()