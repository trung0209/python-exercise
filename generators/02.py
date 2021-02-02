def csv_reader(file_name):
    file = open(file_name,encoding="utf8")
    result = file.read().split("\n")
    return result

result = csv_reader("D:\gson\movies.csv")
print(len(result))