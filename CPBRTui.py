# importing packages needed for the gui to run
import curses
import npyscreen as nps

# importing forms
from Forms.FormUtilities import *
from Forms import SplashForm

from Forms import LoadStartGGDataForm
from Forms import ViewSeasonForm
from Forms import LeaderboardForm
from Forms import RankingMetricSetupForm
from Forms import PlayerInfoForm

class CPBRComboLoggerApp(nps.NPSAppManaged):
    def onStart(self):
        # splash form
        self.addForm(FM_MAIN, SplashForm.CPBRSplashForm, name=None)

        # load start.gg data form
        self.addForm(FM_LOAD_STARTGG, LoadStartGGDataForm.LoadStartGGDataForm, name=None)

        # view season form
        self.addForm(FM_VIEW_SEASON, ViewSeasonForm.ViewSeasonForm, name=None)

        # leaderboard form
        self.addForm(FM_LEADERBOARD, LeaderboardForm.LeaderboardForm, name=None)

        # player info form
        self.addForm(FM_PLAYER_INFO, PlayerInfoForm.PlayerInfoForm, name=None)
        
        # ranking metrics setup form
        self.addForm(FM_METRIC_SETUP, RankingMetricSetupForm.RankingMetricSetupForm, name=None)



if __name__ == "__main__":
    App = CPBRComboLoggerApp()
    App.run()