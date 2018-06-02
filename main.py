import matplotlib
matplotlib.use('TkAgg') #Stops crashing
from tkinter import * 
import sys
sys.path.append('/Users/Cactus/wiki-word-frequency/Google-Search-API')
from google import google

def find_url(search_term):
	result = google.search(search_term)
	print(result)

if __name__ == "__main__":
	def do():
		graph.main()
	def get_text_button(): #On button click
		find_url(search.get())
	def get_text_enter(search): #On pressing enter/return
		find_url(search.widget.get())

	root =Tk()
	#root.geometry('{}x{}'.format(600, 400))
	#Make layout look good when uncommenting the above line

	title = Label(root, text="Hello tkinter!")
	title.grid(column=0, row=0, columnspan=2)

	label = Label(root, text="Search term: ")
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