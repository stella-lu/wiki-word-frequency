import re
import requests
import string
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

str_to_remove = ['[clarification needed]', '\xa0']

def modify_text(page):
	soup = BeautifulSoup(page.text, 'html.parser')
	p_text = soup.find_all('p') 
	str_text = make_one_string(p_text)
	text = ' '.join(str_text) # String including unwanted strings & chars

	# Remove html tags and other irrelevant strings
	text = remove_html_tags(text)
	text = remove_misc_str(text, str_to_remove)
	translator = str.maketrans('', '', string.punctuation)
	text= text.translate(translator)
	
	# Turn long string into list of individual words
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

def order_lists(labels, freq):
	""" Orders labels & freq in parallel from most to least frequentyly occurring word """
	def freq_of_word(elem):
		return elem[1]

	zipped = list(zip(labels, freq))
	zipped.sort(key=freq_of_word, reverse=True)
	unzipped = list(zip(*zipped))
	labels = list(unzipped[0])
	freq = list(unzipped[1])
	return labels, freq

def trim_words(labels, freq):
	labels, freq, remaining_labels, remaining_freq = labels[:30], freq[:30], labels[30:], freq[30:]
	labels.append('Other')
	freq.append(sum(remaining_freq))
	return labels, freq

def make_pie(labels, freq):
	def return_freq(freq):
		""" Returns the frequency of a word given its percentage """
		def show_freq(pct):
			total = sum(freq)
			return int(round(pct*total)/100)
		return show_freq

	fig, ax = plt.subplots()
	ax.pie(freq, labels=labels, autopct=return_freq(freq), labeldistance=1.05, startangle=90, counterclock=False, rotatelabels=True)
	ax.axis('equal')  # Ensures that pie is drawn as a circle.
	plt.show()

"""if __name__ == "__main__":"""
def main():
	main_page = 'https://en.wikipedia.org/wiki/Adolf_Hitler'
	page = requests.get(main_page, headers={'Connection': 'close'})

	lst_of_text = modify_text(page)
	labels, freq = count(lst_of_text)
	labels, freq = order_lists(labels, freq)

	if len(labels) > 30:
		labels, freq = trim_words(labels, freq)
	make_pie(labels, freq)



