import matplotlib
matplotlib.use('TkAgg') #Stops crashing
from tkinter import * 
import sys
import graph
sys.path.append('/Users/Cactus/wiki-word-frequency/Google-Search-API')

def check_url(url):
	""" Checks if the url is a valid wikipedia page """
	if url[:30] == 'https://en.wikipedia.org/wiki/' and len(url) > 30:
		warning.grid_remove()
		pos_dict = {}
		pos_dict['pronouns'] = pro_var.get()
		pos_dict['conjunctions'] = con_var.get()
		pos_dict['prepositions'] = pre_var.get()
		pos_dict['articles'] = art_var.get()
		graph.main(url, pos_dict)
	else:
		warning.grid()
		

if __name__ == "__main__":
	def get_text_enter(search): #On pressing enter/return
		check_url(search.widget.get())

	root =Tk()
	root.title("Wikipedia Word Frequency")
	pro_var, con_var, pre_var, art_var = IntVar(), IntVar(), IntVar(), IntVar() # Tkinter IntVars for Checkbuttons' status

	title = Label(root, text="Wikipedia Word Frequency - Stella Lu", width=60, height=2)
	label = Label(root, text="Wikipedia URL: ", width=20, height=4)
	search = Entry(root, bd=3, width=40)
	search.bind("<Return>", get_text_enter)
	exit = Button(root, text="Exit", command=root.destroy)
	empty = Label(root, text="      ")
	warning = Label(root, text="This is not a valid English Wikipedia page.")
	# Checkbuttons for parts of speech
	pos = Label(root, text="Parts of speech to omit:")
	pronouns = Checkbutton(root, text="Pronouns", variable=pro_var)
	conjunctions = Checkbutton(root, text="Conjunctions", variable=con_var)
	prepositions = Checkbutton(root, text="Prepositions", variable=pre_var)
	articles = Checkbutton(root, text="Articles", variable=art_var)
	
	title.grid(column=0, row=0, columnspan=2)
	label.grid(column=0, row=1)
	search.grid(column=1, row=1)
	exit.grid(column=1, row=6)
	empty.grid(column=0, row=7, columnspan=2)
	pos.grid(column=0, row=2)
	pronouns.grid(column=0, row=3, sticky=W)
	conjunctions.grid(column=0, row=4, sticky=W)
	prepositions.grid(column=0, row=5, sticky=W)
	articles.grid(column=0, row=6, sticky=W)
	warning.grid(column=0, row=7, columnspan=2)
	warning.grid_remove() # Widget not displayed, but settings are saved


	root.mainloop()