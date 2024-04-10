import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
from time import sleep

# import Configuration


# CONSTANTS used in the program
# conf = Configuration.Configuration()


def get_url(topic_name):
    """
    Going to our homepage
    :return browser, url:
    """
    options = uc.ChromeOptions()
    options.add_experimental_option("prefs", {
        # block image loading
        "profile.managed_default_content_settings.images": 2,
    })
    # options.add_argument("--headless")
    user_agent = conf.get_headers()
    options.add_argument(f'user-agent={user_agent}')
    browser = uc.Chrome(options=options)
    url = f"https://www.researchgate.net/search/publication?q={topic_name}&page=1"
    browser.get(url)
    return browser, url



import csv

# Initialize an empty list to store the album info
album_list = []

# Open the CSV file containing the album info
with open('albums_database.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    # Your code continues...


    # Skip the header row if there is one
    next(csvreader, None)

    # Iterate over each row in the CSV
    for row in csvreader:
        # Assuming the author is in the first column and the album name is in the second
        author = row[2]
        album_name = row[1].replace('/', ' ')
        album_name = album_name.replace(':', ' ')
        album_name = album_name.replace('?', '')
        album_name = album_name.replace('"', '')
        # album_name = filter(lambda x: x.isalnum() or x.isspace(), album_name)
        #
        # album_name = "".join(album_name)

        # Concatenate the author and album name with a whitespace and add to the list
        album_list.append(f"{author} {album_name}")

# Print the list to verify
print(album_list)

browser = webdriver.Chrome()
base_url = f"https://www.ebay.com/"
browser.get(base_url)
def make_directory(folder_name):
    parent_dir = "C:/Users/solom/OneDrive/Desktop/Data Science ITC/Data Science OCT-23/Final Project/pythonProject/scraped_images"
    # The path should include the folder_name
    path = os.path.join(parent_dir, folder_name)
    # Check if the combined path exists before creating the directory
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def perform_search(my_chrome, prompt):
    search_input = my_chrome.find_element(By.XPATH, '/html/body/div[3]/div/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]')
    # Typing my registered email into login input text field
    search_input.send_keys(prompt)
    my_chrome.find_element(By.CSS_SELECTOR,
                           '#gh-btn').click()

def following_search(my_chrome, prompt):
    search_input = my_chrome.find_element(By.XPATH, '/html/body/div[2]/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]')
    # Typing my registered email into login input text field
    search_input.clear()
    search_input.send_keys(prompt)
    my_chrome.find_element(By.CSS_SELECTOR,
                           '#gh-btn').click()


def find_all_offers_on_page(my_chrome):
    """
    Finding all publications on each individual page by class via BS4
    so that the pubs contain all the URLs of each publication in the page
    :param my_chrome:
    :return pubs: List of URLs
    """
    offer_class = "s-item__wrapper clearfix"
    soup = BeautifulSoup(my_chrome.page_source, 'lxml')
    offers = soup.findAll('div', class_=offer_class)
    sleep(1)
    count = my_chrome.find_element(By.XPATH, '/html/body/div[4]/div[4]/div[1]/div/div[1]/div[1]/div[1]/h1/span[1]').text
    # while True:
    #     try:
    #         count = soup.find('div', class_="srp-controls__control srp-controls__count").find('span', class_='BOLD').text
    #         break
    #     except AttributeError:
    #         sleep(1)
    return offers, count

for ind, album in enumerate(album_list):
    # for album in album_list:
    folder_name = album
    prompt = album + ' vinyl'
    if ind == 0:
        perform_search(browser, prompt)
    else:
        following_search(browser, prompt)
    offers, count = find_all_offers_on_page(browser)
    if count == '0':
        continue
    # Create a directory for the images
    path = make_directory(folder_name)
    sleep(1)

    for ind, offer in enumerate(offers[1:6]):
        img_url = offer.find('img')['src']
            # Send a GET request to the image URL
        response = requests.get(img_url)
        path_to_save_image = os.path.join(path, f"{album}_ebay_{ind}")
        with open(path_to_save_image, 'wb') as file:
            file.write(response.content)

