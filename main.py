import re
import requests
import string
import webbrowser
from bs4 import BeautifulSoup

def get_text(str_to_remove, page):
	soup = BeautifulSoup(page.text, 'html.parser') # Create a BeautifulSoup object
	p_text = soup.find_all('p')
	str_text = make_one_string(p_text)
	text = ' '.join(str_text) # One string including html tags
	
	# Remove html tags and other irrelevant strings
	text = remove_html_tags(text)
	for s in str_to_remove:
		if s in text:
			text = text.replace(s, '')
	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator)

def make_one_string(p_text):
	for i in range(len(p_text)):
		p_text[i] = str(p_text[i])
	return p_text

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

if __name__ == "__main__":
	#str_to_remove = ['[clarification needed]', '\xa0', '(', ')', '.', ',', ';', '"']
	str_to_remove = ['[clarification needed]', '\xa0']
	main_page = 'https://en.wikipedia.org/wiki/Tuareg_rebellion_(1990%E2%80%931995)'
	page = requests.get(main_page)

	text = get_text(str_to_remove, page)
	print(text)