# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

years_to_scrape = range(1977, 2020)

# create a set of empty lists that we will populate with our movie data
running_ids = []
running_titles = []
running_tot_grosses = []
running_theaters_per_movie = []
running_release_dates = []
running_year = []

# Scraper
t0 = time.time() # timer
counter = 0

options = Options()
options.headless = True

DRIVER_PATH = '/usr/local/bin/chromedriver'

# set up the driver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# let's loop through each year
for counter, year_to_scrape in enumerate(years_to_scrape):

    # Go to the site we want to scrape
    driver.get(f'https://www.boxofficemojo.com/year/{year_to_scrape}/')

    # get the total number of entries per year
    entries = len(driver.find_elements_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr'))

    # scrape the data we're after
    titles = driver.find_elements_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr/td[2]/a')
    ids = [title.get_attribute('href').split('/')[4] for title in titles]
    total_grosses = driver.find_elements_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr/td[8]')
    theaters_per_movie = driver.find_elements_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr/td[7]')
    release_dates = driver.find_elements_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr/td[9]')

    # get the text from the web elements and save them to our running lists
    running_ids += ids
    running_titles += [title.text for title in titles]
    running_tot_grosses += [total_gross.text for total_gross in total_grosses]
    running_theaters_per_movie += [theaters.text for theaters in theaters_per_movie]
    running_release_dates += [release_date.text for release_date in release_dates]
    running_year += [year_to_scrape for _ in range(entries-1)]

    # timer
    if counter % 5 == 0:
        print(f'scraped {counter} years')
        print(f'current runtime is {round((time.time() - t0)/60,2)} mins')
        print('----------')


# close the driver
driver.quit()

movies_dict = {
    'bom_id': running_ids,
    'title': running_titles,
    'total_gross' : running_tot_grosses,
    'theaters' : running_theaters_per_movie,
    'release_date' : running_release_dates,
    'year' : running_year
}

movies_df = pd.DataFrame(movies_dict)

# remove an duplicates while keeping the entry with the year of original release
movies_df = movies_df.drop(
    movies_df.loc[movies_df.duplicated('bom_id', 'first')].index
)

# save out the DataFrame
movies_df.to_csv('../../../Data/Movies/Box_Office_Mojo/raw/movies_total_gross.csv', index=False)
