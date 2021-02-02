file_name = "D:\gson\movies.csv"
csv_reader = [row for row in open(file_name,"r",encoding="utf8")]
csv_reader1 = []
for row in open(file_name,"r",encoding="utf8"):
    csv_reader1.append(row)

print(len(csv_reader1))
print(csv_reader)
