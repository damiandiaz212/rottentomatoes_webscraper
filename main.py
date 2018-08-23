import scraper 
import csv

''' 
Rotten Tomatoes web scraper
Created by Damian Diaz - https://github.com/damiandiaz212
Last modified (8/21/2018)

See readme for instructions & details.

'''

# If you want results outputted to terminal
debug = True

infile = open("movie_urls.txt","r")
outfile = open('data.csv', 'w')

lines = infile.readlines()
labels = [['movie_name', 'release_date', 'tomato_score', 'audience_score', 'rating', 
'genre', 'directors', 'writers', 'box_office', 'runtime', 'studio', 'cast', 'characters']]

writer = csv.writer(outfile)
writer.writerows(labels)

for line in lines:
	writer.writerows(scraper.scrape_movie(line, debug))

print('Done')