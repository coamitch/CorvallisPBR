from tkinter import *

from Forms.SplashLayout import SplashLayout

class LeaderboardLayout(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# saving the parent (container: frame) and controller (self: CPBRApp)
		self.parent = parent
		self.controller = controller

		# setting the splash screen button header
		self.splashBtnLabel = 'Leaderboard'

	def buildForm(self):
		label = Label(self, text="A list of Grocery items.")
		label.pack()

		self.listbox = Listbox(self)

		self.listbox.insert(1, "Bread")
		self.listbox.insert(2, "Milk")
		self.listbox.insert(3, "Meat")
		self.listbox.insert(4, "Cheese")
		self.listbox.insert(5, "Vegetables")
		self.listbox.pack()

		bttn = Button(self, text="Submit", command=self.hndlBack)
		bttn.pack(side="bottom")

	def hndlBack(self):
		print(self.listbox.curselection())
		self.controller.showFrame(self.controller.frames[SplashLayout])
