file_name = "D:\gson\movies.csv"
csv_gen = (row for row in open(file_name,"r",encoding="utf8"))
line_count = 0
while True:
    val = next(csv_gen, 'end')
    if val == 'end':
        print('list end')
        break
    else:
        line_count = line_count + 1
        print(val)

# print(line_count)
