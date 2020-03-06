import xlrd

# bbip_file = os.path.join(current_project_path, 'BBIP_RID.xlsx')
bbip_file = 'read_excel.xlsx'
bbip_book = xlrd.open_workbook(bbip_file)
bbip_sheet = bbip_book.sheet_by_index(0)
bbip_num_of_rows = bbip_sheet.nrows
bbip_num_of_cols = bbip_sheet.ncols

for row_in_bbip_file in range(1, bbip_num_of_rows):
    row_value_bbip_sheet = bbip_sheet.row_values(row_in_bbip_file)
    device = row_value_bbip_sheet[0]
    host = row_value_bbip_sheet[1]
    port = str(row_value_bbip_sheet[2])
    device_type = row_value_bbip_sheet[3]
    username = row_value_bbip_sheet[4]
    password = row_value_bbip_sheet[5]
    global_delay_factor = int(row_value_bbip_sheet[6])
    command_1 = row_value_bbip_sheet[7]
    command_2 = row_value_bbip_sheet[8]
    command_3 = row_value_bbip_sheet[9]

    print(row_value_bbip_sheet)