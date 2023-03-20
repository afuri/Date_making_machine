import xlsxwriter


def write_to_excel(data, filename='Default'):
    workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, '№ урока')
    worksheet.write(0, 1, 'день недели')
    worksheet.write(0, 2, 'дата')

    for row, (weekday, date) in enumerate(data):
        worksheet.write(row + 1, 0, row + 1)
        worksheet.write(row + 1, 1, weekday)
        worksheet.write(row + 1, 2, date)

    workbook.close()
