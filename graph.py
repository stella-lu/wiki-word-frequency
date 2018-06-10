import re
import requests
import string
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

str_to_remove = ['[clarification needed]', '\xa0']
pronouns = ['ALL', 'ANOTHER', 'ANY', 'ANYBODY', 'ANYONE', 'ANYTHING', 'AS', 'BOTH', 'EACH', 'EITHER', 'EVERYBODY', 'EVERYONE', 'EVERYTHING', 'FEW', 'HE', 'HER', 'HERS', 'HERSELF', 'HIM', 'HIMSELF', 'HIS', 'I', 'IT', 'ITSELF', 'MANY', 'ME', 'MINE', 'MOST', 'MY', 'MYSELF', 'NEITHER', 'NO', 'ONE', 'NOBODY', 'NONE', 'NOTHING', 'ONE', 'OTHER', 'OTHERS', 'OUR', 'OURS', 'OURSELVES', 'SEVERAL', 'SHE', 'SOME', 'SOMEBODY', 'SOMEONE', 'SOMETHING', 'SUCH', 'THAT', 'THEE', 'THEIR', 'THEIRS', 'THEM', 'THEMSELVES', 'THESE', 'THEY', 'THINE', 'THIS', 'THOSE', 'THOU', 'THY', 'US', 'WE', 'WHAT', 'WHATEVER', 'WHICH', 'WHICHEVER', 'WHO', 'WHOEVER', 'WHOM', 'WHOMEVER', 'WHOSE', 'YOU', 'YOUR', 'YOURS', 'YOURSELF', 'YOURSELVES']
conjunctions = ['AND', 'OR', 'BUT', 'NOR', 'SO', 'FOR', 'YET', 'AFTER', 'ALTHOUGH', 'AS', 'AS IF', 'AS LONG AS', 'BECAUSE', 'BEFORE', 'EVEN IF', 'EVEN THOUGH', 'IF', 'ONCE', 'PROVIDED', 'SINCE', 'SO THAT', 'THAT', 'THOUGH', 'TILL', 'UNLESS', 'UNTIL', 'WHAT', 'WHEN', 'WHENEVER', 'WHEREVER', 'WHETHER', 'WHILE', 'ACCORDINGLY', 'ALSO', 'ANYWAY', 'BESIDES', 'CONSEQUENTLY', 'FINALLY', 'FOR EXAMPLE', 'FOR INSTANCE', 'FURTHER', 'FURTHERMORE', 'HENCE', 'HOWEVER', 'INCIDENTALLY', 'INDEED', 'IN FACT', 'INSTEAD', 'LIKEWISE', 'MEANWHILE', 'MOREOVER', 'NAMELY', 'NOW', 'OF COURSE', 'ON THE CONTRARY', 'ON THE OTHER HAND', 'OTHERWISE', 'NEVERTHELESS', 'NEXT', 'NONETHELESS', 'SIMILARLY', 'SO FAR', 'UNTIL NOW', 'STILL', 'THEN', 'THEREFORE', 'THUS']
prepositions = ['ABOARD', 'ABOUT', 'ABOVE', 'ACROSS', 'AFTER', 'AGAINST', 'ALONG', 'AMID', 'AMONG', 'AROUND', 'AS', 'AT', 'BEFORE', 'BEHIND', 'BELOW', 'BENEATH', 'BESIDE', 'BETWEEN', 'BEYOND', 'BUT', 'BY', 'CONCERNING', 'CONSIDERING', 'DESPITE', 'DOWN', 'DURING', 'EXCEPT', 'FOLLOWING', 'FOR', 'FROM', 'IN', 'INSIDE', 'INTO', 'LIKE', 'MINUS', 'NEAR', 'NEXT', 'OF', 'OFF', 'ON', 'ONTO', 'OPPOSITE', 'OUT', 'OUTSIDE', 'OVER', 'PAST', 'PER', 'PLUS', 'REGARDING', 'ROUND', 'SAVE', 'SINCE', 'THAN', 'THROUGH', 'TO', 'TOWARD', 'UNDER', 'UNDERNEATH', 'UNLIKE', 'UNTIL', 'UP', 'UPON', 'VERSUS', 'VIA', 'WITH', 'WITHIN', 'WITHOUT']
articles = ['THE', 'A', 'AN']
parts_of_speech = pronouns+conjunctions+prepositions+articles

def modify_text(page):
	soup = BeautifulSoup(page.text, 'html.parser')
	p_text = soup.find_all('p') 
	str_text = make_one_string(p_text)
	text = ' '.join(str_text) # String including unwanted strings & chars

	# Remove html tags and other irrelevant strings
	text = remove_html_tags(text)
	text = remove_misc_str(text, str_to_remove)
	translator = str.maketrans('', '', string.punctuation)
	text = text.translate(translator)
	
	# Turn long string into list of individual words
	text = re.sub("[^\w]", " ",  text).split()
	
	return text

def remove_words(lst):
	new_lst = [word for word in lst if word.upper() not in parts_of_speech]
	return new_lst

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
	""" Return 20 most frequent words """
	labels, freq, remaining_labels, remaining_freq = labels[:20], freq[:20], labels[20:], freq[20:]
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

def main(url):
	page = requests.get(url, headers={'Connection': 'close'})

	lst_of_text = modify_text(page)
	lst_of_text = remove_words(lst_of_text)
	labels, freq = count(lst_of_text)
	labels, freq = order_lists(labels, freq)
	labels, freq = trim_words(labels, freq)
	make_pie(labels, freq)
