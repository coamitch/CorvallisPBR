# general imports
from tkinter import *

# form inputs
from Forms.SplashLayout import SplashLayout
from Forms.CovidCheckLayout import CovidCheckLayout
from Forms.LeaderboardLayout import LeaderboardLayout

class CPBRApp(Tk):
	# constructor
	def __init__(self):
		# calling super init
		super().__init__()

		# setting up app
		self.resizable(False, False)
		self.geometry('1500x1000')

		# creating a frame
		self.container = Frame(self)
		self.container.pack(side='top', fill='both', expand=True)

		# setting up the grid
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		# adding frames to a dictionary
		self.layouts = list()
		self.layouts.append(SplashLayout)
		self.layouts.append(CovidCheckLayout)
		self.layouts.append(LeaderboardLayout)

		# adding the frames
		self.addFrames()

		for frame in self.frames.values():
			frame.buildForm()

		# showing the splash screen first
		self.showFrame(self.frames[SplashLayout])

	def addFrames(self):
		# initializing a dictionary to store the frames
		self.frames = dict()

		# iterating through the frame layouts and adding them to the app
		for layout in self.layouts:
			frame = layout(self.container, self)

			self.frames[layout] = frame

			frame.grid(row=0, column=0, sticky='nsew')

	def showFrame(self, frame):
		frame.tkraise()

if __name__ == '__main__':
	app = CPBRApp()
	app.mainloop()