# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def init_browser():
    executable_path = {'exectuable_path': "ChromeDriverManager().install()"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    latest_title = {}
    latest_paragraph = {}
    time.sleep(1)

    
# Url
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

# HTML object
    html = browser.html

# Parser the html
    soup = bs(html, "html.parser")
    
# Scrape latest title
    latest_title = soup.select('div.content_title')[1]
    latest_title

# Scrape paragraph of latest title
    latest_paragraph = soup.find_all('div', 'article_teaser_body')[0]
    latest_paragraph
    browser.quit()
    return latest_paragraph, latest_title

# JPL Url
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html = browser.html
    soup = bs(html, 'html.parser')
    print(soup.prettify())

# JPL featured image
    featured_image_url = soup.find(name = 'a', class_ = 'button fancybox')['data-fancybox-href']
    featured_image_url
    return featured_image_url

# Mars Facts pandas
    url3 = 'https://space-facts.com/mars/'
    browser.visit(url3)


# Read Mars table
    Mars_facts_table = pd.read_html(url3)
    Mars_facts_table

    type(Mars_facts_table)

# Store table into a dataframe
    df = Mars_facts_table[0]
    df

# Renamed header columns
    renamed = df.rename(columns={0 : " ", 1 : "Mars"})
    renamed

# Removed index column
    No_index = renamed.rename(index={0 :" ",
                    1:" ",
                    2:" ",
                    3:" ",
                    4:" ",
                    5:" ",
                    6:" ",
                    7:" ",
                    8:" "})
    No_index

# DF table to HTML table
    html_table = No_index.to_html()
    html_table

# Remove newlines
    html_table.replace('\n', '')

# Store HTML table as a file
    No_index.to_html('table.html')

# Url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

# Dictionary for Mars images
    hemisphere_image_urls = [
        {"title" : "Valles Marineris Hemisphere", "img_url" : "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg" },
        {"title" : "Cereberus Hemisphere", "img_url" : "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg" },
        {"title" : "Schiaparelli Hemisphere", "img_url" : "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg" },
        {"title" : "Syrtis Major Hemisphere", "img_url" : "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg" }
    ]
    hemisphere_image_urls

    browser.quit()
    
    return No_index
