# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path='C:/Users/danib/OneDrive/Documents/Data Analytics/Class Folder/Web_Scrapping/chromedriver.exe', headless=False)

    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere_data(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "URL_and_title": hemisphere_image_urls
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
     
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        # news_title

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
        # news_p
        
    except AttributeError:
        return None, None
        
    return news_title, news_p


# ### Featured Images

def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        # img_url_rel

    except AttributeError:
        return None 

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    # img_url

    return img_url

# ## Mars Facts

def mars_facts():

    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://space-facts.com/mars/')[0]

    except BaseException:
        return None 

    # Assign columns and set index of dataframe
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere_data(browser):

        # 1. Use browser to visit the URL 
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)


        # 2. Create a list to hold the images and titles.
        hemisphere_image_urls = []

        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        # Image 1.1 - Click 
        browser.find_by_css('a')
        images_click = browser.find_by_css('a')[5]
        images_click.click()

        # Image 1.2 - Browser 
        html = browser.html
        hem_image = soup(html, 'html.parser')

        # Image 1.3 - Image and Title 
        hem_image_1 = hem_image.select_one('div.downloads ul li a').get("href")
        # hem_image_1
        title1 = hem_image.find('h2').get_text()
        # title1
        

        # Dict 1.4
        Dict_1 = {
            "image": hem_image_1,
            "title": title1
        }
        # Dict_1

        # Back to main page 1.5
        browser.back()

        # Image 2.1 - Click 
        browser.find_by_css('a')
        images_click = browser.find_by_css('a')[7]
        images_click.click()

        # Image 2.2 - Browser 
        html = browser.html
        hem_image = soup(html, 'html.parser')

        # Image 2.3 - Image and Title 
        hem_image_2 = hem_image.select_one('div.downloads ul li a').get("href")
        # hem_image_2
        title2 = hem_image.find('h2').get_text()
        # title2
        # print(hem_image_2, title2)

        # Dict 2.4
        Dict_2 = {
            "image": hem_image_2,
            "title": title2
        }
        # Dict_2

        # Back to main page 2.5
        browser.back()

        # Image 3.1 - Click 
        browser.find_by_css('a')
        images_click = browser.find_by_css('a')[9]
        images_click.click()

        # Image 3.2 - Browser 
        html = browser.html
        hem_image = soup(html, 'html.parser')

        # Image 3.3 - Image and Title 
        hem_image_3 = hem_image.select_one('div.downloads ul li a').get("href")
        # hem_image_3
        title3 = hem_image.find('h2').get_text()
        # title3
        # print(hem_image_3, title3)

        # Dict 3.4
        Dict_3 = {
            "image": hem_image_3,
            "title": title3
        }
        # Dict_3

        # Back to main page 3.5
        browser.back()

        # Image 4.1 - Click 
        browser.find_by_css('a')
        images_click = browser.find_by_css('a')[11]
        images_click.click()

        # Image 4.2 - Browser 
        html = browser.html
        hem_image = soup(html, 'html.parser')

        # Image 4.3 - Image and Title 
        hem_image_4 = hem_image.select_one('div.downloads ul li a').get("href")
        # hem_image_4
        title4 = hem_image.find('h2').get_text()
        # title4
        # print(hem_image_4, title4)

        # Dict 4.4
        Dict_4 = {
            "image": hem_image_4,
            "title": title4
        }
        # Dict_4

        # Back to main page 4.4
        browser.back()

        # List of Dict
        hemisphere_image_urls = [Dict_1, Dict_2, Dict_3, Dict_4]
        # console.log(hemisphere_image_urls)

        return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())

