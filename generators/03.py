# Read large CSV file
def csv_reader(file_name):
    for row in open(file_name,"r",encoding="utf8"):
        yield row


filereader = csv_reader("D:\gson\movies.csv")
line_count = 0
while True:
    val = next(filereader, 'end')
    if val == 'end':
        print('list end')
        break
    else:
        line_count += 1
        print(val)

print(line_count)

