from tkinter import *

from Forms.SplashLayout import SplashLayout

class CovidCheckLayout(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# saving the parent (container: frame) and controller (self: CPBRApp)
		self.parent = parent
		self.controller = controller

		# setting the splash screen button header
		self.splashBtnLabel = 'Covid Check'
		
		# loading in current covid player data

	def buildForm(self):
		label = Label(self, text="A list of Grocery items.")
		label.pack()

		choices = ["apple", "orange", "banana"]
		strChoices = StringVar(value=choices)
		self.listbox = Listbox(self, listvariable=strChoices)
		
		choices.append("peach")
		strChoices.set(choices)
		
		bttn = Button(self, text="Submit", command=self.hndlBack)
		bttn.pack(side="bottom")

	def hndlBack(self):
		print(self.listbox.curselection())
		self.controller.showFrame(self.controller.frames[SplashLayout])
