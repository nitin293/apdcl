import pandas as pd
from openpyxl import Workbook


sel_c = pd.read_csv('sample.csv')
sel_r = sel_c.loc[1:10]

print(sel_r)