# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

# read in movies_total_gross
tg_df = pd.read_csv('../../../Data/Movies/Box_Office_Mojo/movies_total_gross.csv')

# get list of bom_ids
bom_ids = tg_df['bom_id'].values

# create a set of empty lists that we will populate with our movie data
running_imdb_ids = []
running_titles = []
running_summary_infos = []
running_gross_infos = []

t0 = time.time() # timer
counter = 0

# Movie Summary Scraper
options = Options()
options.headless = True

DRIVER_PATH = '/usr/local/bin/chromedriver'

# set up the driver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# loop through each movie
for counter, bom_id in enumerate(bom_ids):

    # go to page to scrape
    driver.get(f'https://www.boxofficemojo.com/release/{bom_id}')

    # scrape desired information
    # imdb_id
    try:
        ele = driver.find_element_by_xpath('//*[@id="title-summary-refiner"]/a')
        imdb_id = ele.get_attribute('href').split('/')[4]
    except:
        imdb_id = "ERROR!!"

    # title
    try:
        title_ele = driver.find_element_by_xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/h1')
        title = title_ele.text
    except:
        title = "ERROR!!"

    # summary info
    try:
        summary_ele = driver.find_element_by_xpath('//*[@id="a-page"]/main/div/div[3]/div[4]')
        summary = summary_ele.text
    except:
        summary = "ERROR!!"

    # gross info
    try:
        gross_ele = driver.find_element_by_xpath('//*[@id="a-page"]/main/div/div[3]/div[1]/div')
        gross = gross_ele.text
    except:
        gross = "ERROR!!"

    # add scraped info to our running lists
    running_imdb_ids.append(imdb_id)
    running_titles.append(title)
    running_summary_infos.append(summary)
    running_gross_infos.append(gross)

    # timer
    if counter % 500 == 0:
        print(f'scraped {counter} movies')
        print(f'current runtime is {round((time.time() - t0)/60,2)} mins')
        print('----------')

# close the driver
driver.quit()

print(f'total runtime is {round((time.time() - t0)/60,2)} mins') # timer

# set up dictionary
summary_dict = {
    'bom_id' : bom_ids,
    'imdb_id' : running_imdb_ids,
    'title' : running_titles,
    'movie_summary' : running_summary_infos,
    'gross' : running_gross_infos
}

# set DataFrame
summary_df = pd.DataFrame(summary_dict)

# save our file
summary_df.to_csv('../../../Data/Movies/Box_Office_Mojo/movies_summary.csv', index=False)
