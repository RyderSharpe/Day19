# import openpyxl
#
# def count_numbers_in_rows_and_columns(file_path, rows, cols):
#     # Load the workbook and select the active worksheet
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.active
#
#     # Initialize a dictionary to keep track of number counts
#     number_counts = {}
#
#     # Count numbers in specified rows
#     for row in rows:
#         for cell in sheet[row]:
#             if isinstance(cell.value, (int, float)):
#                 number_counts[cell.value] = number_counts.get(cell.value, 0) + 1
#
#     # Count numbers in specified columns
#     for col in cols:
#         for cell in sheet.iter_cols(min_col=col, max_col=col, min_row=1, max_row=sheet.max_row):
#             for cell_value in cell:
#                 if isinstance(cell_value.value, (int, float)):
#                     number_counts[cell_value.value] = number_counts.get(cell_value.value, 0) + 1
#
#     return number_counts
#
# # Example usage
# file_path = 'lottery.xlsx'  # Path to your Excel file
# rows = range(1, 7)  # Rows you want to count numbers in (1 to 6)
# cols = range(1, 3)  # Columns you want to count numbers in (1 to 2)
#
# number_counts = count_numbers_in_rows_and_columns(file_path, rows, cols)
# print(number_counts)
###############################################

import pandas as pd

# Load the Excel file
file_path = 'lottery.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the data from Sheet2
sheet2_data = pd.read_excel(file_path, sheet_name='Sheet2')

# Combine all relevant columns into one series
combined_data = pd.concat([sheet2_data[col] for col in sheet2_data.columns], ignore_index=True)

# Calculate the frequency of each number
frequency = combined_data.value_counts()

# Display the most common numbers
print(frequency.head(10))





