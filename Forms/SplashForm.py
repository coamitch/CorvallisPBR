import npyscreen as nps
from Forms.KeyShortcuts import registerFkeys
from Forms.FormText import *
from Forms.FormUtilities import *

class CPBRSplashForm(nps.ActionForm):
	def __init__(self, *args, **keywords):
		super().__init__(*args, **keywords)

		# registering hotkeys (F1, F2, F4, and alt+F4)
		registerFkeys(self)

	def create(self):
		self.formObjs = dict()

		self.formObjs['title1'] = [self.add(nps.FixedText, name=None, value=x, editable=False) for x in cpbrAsciiList]
		self.formObjs['title2'] = [self.add(nps.FixedText, name=None, value=x, editable=False) for x in menuAsciiList]

		self.formObjs['devTeam'] = self.add(nps.FixedText, name=None,
												 value='Enlore Software Development',
												 editable=False)

		self.formObjs['version'] = self.add(nps.FixedText, name=None,
											value='Version 1.0.0', editable=False)

		self.space2 = self.add(nps.FixedText, name=None, value=' ', editable=False)

		self.formObjs['options'] = self.add(nps.TitleSelectOne, max_height=6, value=[0, ],
								name='Select Function:',
								values=['Load Start.gg Data', 'View Season Data',
										'Leaderboard', 'Player Info',
										'Ranking Metric Setup'],
								scroll_exit=True)

		self.space3 = self.add(nps.FixedText, name=None, value=' ', editable=False)

		self.shortcutInfo = self.add(nps.FixedText, name=None,
									 value="To see shortcut listings, press F1.",
									 begin_entry_at=0, use_two_lines=False,
									 editable=False)

	def on_ok(self):
		# getting the option selected by the user
		optionValue = self.formObjs['options'].value[0]

		# load 'load start.gg data' form
		if optionValue == 0:
			self.parentApp.switchForm(FM_LOAD_STARTGG)

		# load 'view saved season data' form
		if optionValue == 1:
			self.parentApp.switchForm(FM_VIEW_SEASON)

		# load 'leaderboard' from
		if optionValue == 2:
			self.parentApp.switchForm(FM_LEADERBOARD)

		# load 'player info' form
		if optionValue == 3:
			self.parentApp.switchForm(FM_PLAYER_INFO)

		# load 'ranking metric setup' form
		if optionValue == 4:
			self.parentApp.switchForm(FM_METRIC_SETUP)

	def on_cancel(self):
		# cancel is the same as exit so we call the same handler
		self.hndlQuit()

	def hndlHelp(self, *args, **kwargs):
		# opening help menu in a notify window
		nps.notify_confirm('\n'.join(helpAsciiList), title='Help')

	def hndlOk(self, *args, **kwards):
		# calling the on_ok handler
		self.on_ok()

	def hndlBack(self, *args, **kwargs):
		# no form to return to so this has the same functionality as exiting
		self.hndlQuit()

	def hndlQuit(self, *args, **kwargs):
		# notifying the user that they will exit and form edits will not be saved.
		result = nps.notify_yes_no(
			'Are you sure you want to close the application? Unsaved work will be lost.',
			title='Exit')

		# if the result is okay then we exit the application, otherwise, we stay where we are/do nothing
		if result:
			self.parentApp.switchForm(None)
