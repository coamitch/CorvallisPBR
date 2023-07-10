from tkinter import *

class SplashLayout(Frame):
	def __init__(self, parent: Frame, controller):
		Frame.__init__(self, parent)

		# saving the parent (container: frame) and controller (self: CPBRApp)
		self.parent = parent
		self.controller = controller

		# setting the button header and layout key for this layout object
		self.splashBtnLabel = None

	def buildForm(self):
		# creating a dictionary to hold all the buttons
		self.formObjs = dict()

		# defining title and grid
		self.formObjs['formHeader'] = Label(self,
											text='Corvallis Program Based Ranking',
											font=('Verdana', 35))
		self.formObjs['formHeader'].place(relx=0.5, rely=0.1, anchor=CENTER)

		# getting a list of all the fames that require buttons from the splash screen
		frames = [x for x in self.controller.frames.values() if x.splashBtnLabel is not None]

		# getting the button headers for each of the added form layouts and max length
		buttonLabels = [x.splashBtnLabel for x in frames]
		buttonLabelLens = [len(x) for x in buttonLabels if x != None]
		maxLabelLen = max(buttonLabelLens) + 4

		# iterating through all the layouts and adding a button for each one
		i = 0
		for frame in frames:
			if frame.splashBtnLabel is None:
				continue

			btn = Button(self, text=frame.splashBtnLabel, width=maxLabelLen,
						 font=('Verdana', 15),
						 command=lambda: self.controller.showFrame(frame))

			self.formObjs[f'button_{i}'] = btn

			# evenly placing the buttons in the center of the form below the label
			yLoc = 0.2 + (i * 0.05)
			self.formObjs[f'button_{i}'].place(relx=0.5, rely=yLoc, anchor=CENTER)

			i += 1