# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('create_and_write_excel.xlsx')
worksheet = workbook.add_worksheet()

content = []
headers = ['Device', 'IP', 'OS_Type']
data_to_write = [['CRSARA01','1.1.1.1','IOS XR'],['RT01ARA','2.2.2.2','IOS']]

content.append(headers)
for data in data_to_write:
    content.append(data)
print(content)

# iterating through content list
row = 0
for fila in content:
    column = 0
    for item in fila:
        # write operation perform
        worksheet.write(row, column, item)
        # incrementing the value of row by one
        # with each iteratons.
        column += 1
    row += 1

workbook.close()