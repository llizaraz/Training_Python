import openpyxl

def savefile(fsm_results):

    header = ['Os_Type','Version', 'Hostname', 'Uptime', 'll', 'Image', 'Serial', 'Platform', 'ConfReg']
    values = fsm_results[0]

    wbook =openpyxl.Workbook()
    wsheet = wbook.active

    wsheet.append(header)
    wsheet.append(values)
    wbook.save('saved_result.xlsx')