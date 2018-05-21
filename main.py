import re
#import requests
import string
import webbrowser
import wikipedia
#from bs4 import BeautifulSoup

str_to_remove = ['[clarification needed]', '\xa0']

def modify_text(text):
	#soup = BeautifulSoup(page.text, 'html.parser')
	#p_text = soup.find_all('p') + soup.find_all('td') + soup.find_all('span')
	#str_text = make_one_string(p_text)
	#text = ' '.join(str_text) # String including unwanted strings & chars

	# Remove html tags and other irrelevant strings
	text = remove_html_tags(text)
	text = remove_misc_str(text, str_to_remove)
	translator = str.maketrans('', '', string.punctuation)
	text= text.translate(translator)

	# Turn long string into list of words
	text = re.sub("[^\w]", " ",  text).split()
	
	return text

def make_one_string(text):
	""" Takes a list and turns each element into a string """
	for i in range(len(text)):
		text[i] = str(text[i])
	return text

def remove_html_tags(text):
    """ Remove html tags from a string """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_misc_str(text, str_to_remove):
	""" Remove strings in list str_to_remove from text """
	for s in str_to_remove:
		if s in text:
			text = text.replace(s, '')
	return text

def count(lst):
	""" Takes one string and returns a list of labels and a list of word frequencies"""
	labels, freq = [], []

	for word in lst:
		if word not in labels:
			labels.append(word)
			freq.append(1)
		else:
			index = labels.index(word)
			freq[index] = freq[index] + 1

	return labels, freq

if __name__ == "__main__":
	main_page = 'https://en.wikipedia.org/wiki/Mila_Kunis_filmography'
	content = wikipedia.page('Beaurières').content
	#page = requests.get(main_page)

	lst_of_text = modify_text(content)
	labels, freq = count(lst_of_text)

	print(labels, freq)


