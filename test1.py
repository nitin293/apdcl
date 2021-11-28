import pandas as pd
import numpy as np
from openpyxl import Workbook

#import the csv file
df = pd.read_csv('sample.csv')

#convert to excel file
intern_proj = pd.ExcelWriter('sample1.xlsx')
df.to_excel(intern_proj, index = False)

intern_proj.save()