# RottenTomatoes web scraper
### Required:
* Python 3
* BeautifulSoup 4

### Instructions:
* Place urls from `https://www.rottentomatoes.com/` of intended movies in movie_urls.txt, each line should represent a new url.
* Run `python main.py` in terminal at file location.
* All data is exported to `data.csv`

### Notes:
* All data is listed as it's collected in the terminal. To switch this off change line 14 in main.py to `debug = False`
* Not all pages are created equal, although i tried to broaden the data collection to work with as many titles as possible some urls will return no data. For specific data variables this will be listed as 'error' in the csv file. 