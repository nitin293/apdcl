import pandas as pd
from openpyxl import Workbook


#taking input from user
col_name = input("Enter the name of the Columns : ")
row_s = int(input("Enter the Starting Rows : "))
row_e = int(input("Enter the Ending Rows : "))


#Selecting Specific Rows and Columns
sel_c = pd.read_csv('sample.csv', usecols = [col_name])
sel_r = sel_c.loc[row_s:row_e]


#convert to excel file
intern_proj = pd.ExcelWriter('sample_excel.xlsx')
sel_r.to_excel(intern_proj, index = False)


#saving the file
intern_proj.save()