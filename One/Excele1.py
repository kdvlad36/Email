import openpyxl
book = openpyxl.open('sender_base.xlsx', read_only = True)
sheet = book.active
print(sheet['A2'].value)
for row in range(1,3):
    desk_email = sheet[row][0].value
    print(desk_email)