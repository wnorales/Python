''''
import openpyxl
wb = openpyxl.load_workbook('C:\example.xlsx')
wb.get_sheet_names()
'''

import openpyxl
wb = openpyxl.load_workbook('C:\example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet2 = wb.get_sheet_by_name('Sheet2')

sheet['A1']
sheet2['B1']
print(sheet['A1'].value)
print(sheet['B1'].value)

