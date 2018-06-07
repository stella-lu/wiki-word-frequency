import matplotlib
matplotlib.use('TkAgg') #Stops crashing
from tkinter import * 
import sys
import graph
sys.path.append('/Users/Cactus/wiki-word-frequency/Google-Search-API')

def check_url(search_term):
	if search_term[:30] == 'https://en.wikipedia.org/wiki/' and len(search_term) > 30:
		graph.main(search_term)
	else:
		print('This is not a valid English Wikipedia page.')

if __name__ == "__main__":
	def get_text_button(): #On button click
		check_url(search.get())
	def get_text_enter(search): #On pressing enter/return
		check_url(search.widget.get())

	root =Tk()
	#root.geometry('{}x{}'.format(600, 400))
	#Make layout look good when uncommenting the above line

	title = Label(root, text="Hello tkinter!")
	title.grid(column=0, row=0, columnspan=2)

	label = Label(root, text="Wikipedia URL: ")
	label.grid(column=0, row=1)

	search = Entry(root, bd=3)
	search.bind("<Return>", get_text_enter)  
	search.grid(column=1, row=1)

	button = Button(root, text="Submit", command=get_text_button)
	button.grid(column=1, row=2, columnspan=1)
	exit = Button(root, text="Exit", command=root.destroy)
	exit.grid(column=0, row=2, columnspan=1)

	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	root.mainloop()