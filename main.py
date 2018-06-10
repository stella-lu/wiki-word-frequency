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
		graph.main(url)
	else:
		warning.grid()
		

if __name__ == "__main__":
	def get_text_button(): #On button click
		check_url(search.get())
	def get_text_enter(search): #On pressing enter/return
		check_url(search.widget.get())

	root =Tk()

	title = Label(root, text="Wikipedia Word Frequency", width=60, height=2)
	label = Label(root, text="Wikipedia URL: ", width=20, height=4)
	search = Entry(root, bd=3, width=40)
	search.bind("<Return>", get_text_enter)
	submit = Button(root, text="Submit", command=get_text_button)
	exit = Button(root, text="Exit", command=root.destroy)
	empty = Label(root, text="      ")
	
	title.grid(column=0, row=0, columnspan=2)
	label.grid(column=0, row=1)
	search.grid(column=1, row=1)
	submit.grid(column=1, row=2)
	exit.grid(column=0, row=2)
	empty.grid(column=0, row=3, columnspan=2)

	warning = Label(root, text="This is not a valid English Wikipedia page.")
	warning.grid(column=0, row=3, columnspan=2)
	warning.grid_remove()

	root.mainloop()