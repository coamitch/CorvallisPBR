# general imports
import pandas as pd

# local file imports
import Utility.Constants as const

# %%
bracketDirPath = const.bracketDirPath
bracket = 'Frt Pnch Frdy 8 Melee Singles Bracket.csv'

# %%
df = pd.read_csv(f'{bracketDirPath}{bracket}')
print(df)