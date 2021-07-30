
import openpyxl

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'sheet页的名字1'
# sheet['A1'] = 'a1单元格的值'
# row1 = ['一', 1]
# sheet.append(row1)
# wb.save('excel的读写.xlsx')


wb = openpyxl.load_workbook('excel的读写.xlsx')
sheet = wb['sheet页的名字1']
a1 = sheet['B2'].value
print(a1)