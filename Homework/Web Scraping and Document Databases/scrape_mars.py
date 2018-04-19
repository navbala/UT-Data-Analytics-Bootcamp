# # Step 2
# # - Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your
# # - scraping code from above and return one Python dictionary containing all of the scraped data.


# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize Browser
def init_browser():
    executable_path = {'executable_path': 'C:/Users/navba/Downloads/chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    # Set browser initilization to browser variable
    browser = init_browser()

    # Create dictionary to hold all of the scraped Mars data
    mars_data = {}

    # ### Latest Mars News
    # -----
    # - Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text. Assign the text to variables that you can reference later.

    # Visit URL of Mars news site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    results = soup.find_all('li', class_='slide')

    # Set the latest title and paragraphs as varibles
    news_title = results[0].find('div', class_ = 'content_title').text
    news_p = results[0].find('div', class_ = 'article_teaser_body').text

    # Store the varibales in the mars data dictionary
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p

    # ## JPL Mars Space Images - Featured Image
    # -----
    # - Visit the url for JPL's Featured Space Image (https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest).
    # - Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # - Make sure to find the image url to the full size .jpg image.
    # - Make sure to save a complete url string for this image.

    # URL of Mars site
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Visit browser and click the links to get full size image
    browser.visit(jpl_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.is_text_present('more info', wait_time=5)
    browser.click_link_by_partial_text('more info')

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Set variable for image link from BeatifulSoup object
    image_results = soup.find('figure', class_='lede')
    featured_image_url = image_results.find('img')['src']

    # Obtain the url for the full featured image
    featured_image_url = "https://www.jpl.nasa.gov" + featured_image_url

    
