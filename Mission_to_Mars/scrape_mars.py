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