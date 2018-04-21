# # Step 2
# # - Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your
# # - scraping code from above and return one Python dictionary containing all of the scraped data.


# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# Initialize Browser
def init_browser():
    executable_path = {'executable_path': 'C:/Users/navba/Downloads/chromedriver_win32/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

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

    time.sleep(.5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    results = soup.find('div', class_='list_text')

    # Set the latest title and paragraphs as varibles
    news_title = results.find('div', class_='content_title').text
    news_p = results.find('div', class_='article_teaser_body').text

    # Store the variables in the mars data dictionary
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

    # Store the variables in the mars data dictionary
    mars_data["featured_image_url"] = featured_image_url


    # ## Mars Weather
    # -----
    # - Visit the Mars Weather twitter account (https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

    # URL of Mars site
    weather_url = "https://twitter.com/marswxreport?lang=en"

    # Visit browser and click the links
    browser.visit(weather_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Examine the results, then determine element that contains sought info
    weather_results = soup.find('div', class_='stream')

    # Set the variable for the latest tweet text
    mars_weather = weather_results.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # Store the variables in the mars data dictionary
    mars_data["mars_weather"] = mars_weather


    # ## Mars Facts
    # -----
    # - Visit the Mars Facts webpage (https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # - Use Pandas to convert the data to a HTML table string.

    # Visit the Mars Facts page and scrape the table data into Pandas
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    # Use Pandas to convert the data to a HTML table string
    html_data = pd.read_html(facts_url)
    mars_facts_df = pd.DataFrame(html_data[0])
    mars_facts_df.columns = ["Mars", "Data"]
    mars_facts_df = mars_facts_df.set_index("Mars")

    mars_info = mars_facts_df.to_html(classes='mars_info')
    mars_info = mars_info.replace('\n', ' ')

    # Store the variables in the mars data dictionary
    mars_data["mars_table"] = mars_info


    # ## Mars Hemispheres
    # -----
    # - Visit the USGS Astrogeology site (https://space-facts.com/mars/) to obtain high resolution images for each of Mar's hemispheres.
    # - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # - Save both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    # Visit the USGS Astrogeology site and scrape pictures of the 4 Mars hemispheres
    executable_path = {'executable_path': 'C:/Users/navba/Downloads/chromedriver_win32/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    astro_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astro_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Create a list to hold image titles/urls
    hemisphere_image_urls = []

    # Loop through the 4 h3 tags (for each hemi image) and load the image title/image URL as key/value pairs in separate dictionaries
    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()

        # Create BeautifulSoup object; parse with 'html.parser'
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Find the image title and urls and add them to the hemi_dict
        partial_url = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2", class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial_url
        hemi_dict = {"title":img_title,"img_url":img_url}

        # Append the urls to the hemi image urls list
        hemisphere_image_urls.append(hemi_dict)

        # Make the browser return to original page to select the next hemisphere
        browser.back()

    # Store the variables in the mars data dictionary
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls

    # Return the mars data dictionary
    return mars_data
