import os
import xlsxwriter

def write_stats_to_excel(operation_stats_list, file_name, open_excel=True):
    output_list = []
    output_list.append(list(operation_stats_list[0].keys()))
    for operation in operation_stats_list:
        output_list.append(list(operation.values()))

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    row = 0
    col = 0

    for method, source, count, average, median, standard_deviation, minimum, maximum, p_25, p_50, p_75 in output_list:
        if row == 0:
            worksheet.write(row, col + 0, method, bold)
            worksheet.write(row, col + 1, source, bold)
            worksheet.write(row, col + 2, count, bold)
            worksheet.write(row, col + 3, average, bold)
            worksheet.write(row, col + 4, median, bold)
            worksheet.write(row, col + 5, standard_deviation, bold)
            worksheet.write(row, col + 6, minimum, bold)
            worksheet.write(row, col + 7, maximum, bold)
            worksheet.write(row, col + 8, p_25, bold)
            worksheet.write(row, col + 9, p_50, bold)
            worksheet.write(row, col + 10, p_75, bold)
        else:
            worksheet.write(row, col + 0, method)
            worksheet.write(row, col + 1, source)
            worksheet.write(row, col + 2, count)
            worksheet.write(row, col + 3, average)
            worksheet.write(row, col + 4, median)
            worksheet.write(row, col + 5, standard_deviation)
            worksheet.write(row, col + 6, minimum)
            worksheet.write(row, col + 7, maximum)
            worksheet.write(row, col + 8, p_25)
            worksheet.write(row, col + 9, p_50)
            worksheet.write(row, col + 10, p_75)
        row += 1

    worksheet.set_column(0, 0, 25)  # Width of column A, set to 25.
    worksheet.set_column(1, 10, 10) # Width of columns B thru K, set to 10.
    workbook.close()

    if open_excel:
        os.system(f"start {file_name}")




