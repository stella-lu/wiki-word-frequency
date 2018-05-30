import matplotlib
matplotlib.use('TkAgg')

import tkinter as tk
import main
import matplotlib.pyplot as plt

if __name__ == "__main__":
	root = tk.Tk()

	w = tk.Label(root, text="Hello Tkinter!")
	w.pack()
	main.main()
	root.mainloop()