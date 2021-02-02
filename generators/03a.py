# Read large CSV file
def csv_reader(file_name):
    for row in open(file_name,"r",encoding="utf8"):
        yield row


filereader = csv_reader("D:\gson\movies.csv")
line_count = 0
while True:
    try:
        val = next(filereader)
        line_count += 1
        print(val)
    except StopIteration:
        break
        

print(line_count)

