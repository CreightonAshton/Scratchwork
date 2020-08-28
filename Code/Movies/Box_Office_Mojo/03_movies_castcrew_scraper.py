# imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

# read in summary df
summary_df = pd.read_csv('../../../Data/Movies/Box_Office_Mojo/movies_summary.csv')

# get ids
imdb_ids = summary_df['imdb_id'].values
bom_ids = summary_df['bom_id'].values

# create a set of empty lists that we will populate with our movie data
running_titles = []
running_crew = []
running_cast = []

# timer
t0 = time.time()
counter = 0

# Cast and Crew Scraper
options = Options()
options.headless = True

DRIVER_PATH = '/usr/local/bin/chromedriver'

# set up the driver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

for counter, imdb_id in enumerate(imdb_ids):

    # go to cast and crew page
    driver.get(f'https://www.boxofficemojo.com/title/{imdb_id}/credits/')

    # Scrape data
    # title
    try:
        title_ele = driver.find_element_by_xpath('//*[@id="a-page"]/main/div/div[1]/div[1]/div/div/div[2]/div/h1')
        title = title_ele.text
    except:
        title = "ERROR!!"

    # crew
    try:
        crew_eles = driver.find_elements_by_xpath('//*[@id="principalCrew"]/tbody/tr/td')
        crew = [crew_ele.text for crew_ele in crew_eles]
    except:
        crew = "ERROR!!"

    # cast
    try:
        actor_eles = driver.find_elements_by_xpath('//*[@id="principalCast"]/tbody/tr/td[1]/a')
        actors = [actor_ele.text for actor_ele in actor_eles]
    except:
        actors = "ERROR!!"

    # add data to running lists
    running_titles.append(title)
    running_crew.append(crew)
    running_cast.append(actors)

    # timer
    if counter % 500 == 0:
        print(f'scraped {counter} movies')
        print(f'current runtime is {round((time.time() - t0)/60,2)} mins')
        print('----------')

# close the driver
driver.quit()

print(f'total runtime is {round((time.time() - t0)/60,2)} mins') #timer

castcrew_dict = {
    'bom_id' : bom_ids,
    'imdb_id' : imdb_ids,
    'title' : running_titles,
    'crew' : running_crew,
    'cast' : running_cast
}

castcrew_df = pd.DataFrame(castcrew_dict)

# save our file
castcrew_df.to_csv('../../../Data/Movies/Box_Office_Mojo/movies_castcrew.csv', index=False)
