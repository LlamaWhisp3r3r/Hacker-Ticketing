import time
from gui import GUI
from tkinter import *

def run():
	master = Tk()
	gui = GUI(master)
	gui.launch_page()
	master.mainloop()

if __name__ == '__main__':
	run()
 