# Import libraries
import requests
from bs4 import BeautifulSoup

def scrape_movie(page, debug):

	page = requests.get(page)
	soup = BeautifulSoup(page.text, 'html.parser')

	# Movie name - removing year 
	try:
		movie_name = soup.find(class_='title clearfix visible-xs')
		movie_name = movie_name.text.strip()
		temp = movie_name.split('(')
		movie_name = temp[0].strip()
	except:
		movie_name = 'error'
	
	# Tomato score & audience score - removing '%'
	try:
		scores = list()
		scores = soup.find_all(class_='meter-value')
	except:
		scores = [000, 000]


	tomatometer_score = scores[0].text
	tomatometer_score = tomatometer_score[:-1].strip()

	audience_score = scores[2].text
	audience_score = audience_score[:-2].strip()

	# Rest of movie info - every variable below depends on this list.

	try:
		movie_info = list()

		for info in soup.find_all(class_ = 'meta-value'):
			info = info.text.strip()
			movie_info.append(info)
	except:
		movie_info = ['error', 'error', 'error', 'error', 'error', 'error', 'error', 'error']

	# Rotten tomatoes stores cast and charcter in same class, loop and call to 
	# function to seperate and store in different lists.
	count = 0
	cast_list = list()
	character_list = list()

	try:
		for info in soup.find_all(class_='cast-item'):
			if(count < 5):
				info = info.text.strip()
				person, character = split_cast(info)
				cast_list.append(person)
				character_list.append(character)
				count+=1

	except:
		cast_list.append('error')
		character_list.append('error')
			
	# Movie Rating
	try:
		rating = movie_info[0].split(" ")[0]
	except:
		rating = 'error'

	# Genre, director, & writers all could have multiple values
	genre = split_names(movie_info[1])
	director = split_names(movie_info[2])
	writers = split_names(movie_info[3])

	# Release date - removing 'wide'
	full_date = movie_info[4]
	full_date = full_date.split(' ')
	release_date = full_date[0] + ' ' + full_date[1] + ' ' + full_date[2][:4]

	# Box office - removing $
	box_office = movie_info[6]
	box_office = box_office[1:]

	# Runtime - removing 'mins'
	try:
		runtime = movie_info[7]
		runtime = runtime.split(' ')[0]
	except:
		runtime = 'error'

	# Studio name
	try:
		studio = movie_info[8]
	except:
		studio = 'error'

	data = [[movie_name, release_date, tomatometer_score, audience_score, rating, genre,
	director, writers, box_office,runtime,studio,cast_list,character_list]]

	if(debug):
		print(movie_name)
		print(release_date)
		print(tomatometer_score)
		print(audience_score)
		print(rating)
		print(genre)
		print(director)
		print(writers)
		print(box_office)
		print(runtime)
		print(studio)
		print(cast_list)
		print(character_list)
		print('\n ************************************\n')

	return data

def split_cast(cast_line):

	cast_line = cast_line.replace('\n', ' ')
	line = cast_line.split(" ")

	actor = ''
	character = ''

	break_index = 0

	for i in line:
		if(i != 'as'):
			actor = actor + i + ' '
			break_index += 1
		else:
			break

	for i in range(break_index+1, len(line)):
		character = character + line[i] + ' '


	actor = actor.strip()
	character = character.strip()

	return actor, character

def split_names(_line):

	names = _line.split(',')

	for i in range (len(names)):
		# If name has a new line symbol
		names[i] = names[i].replace('\n', '')
		names[i] = names[i].strip()


	return names
