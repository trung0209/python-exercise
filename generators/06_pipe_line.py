file_name = "D:\gson\movies.csv"
lines = (line for line in open(file_name,encoding="utf8"))
list_line = (s.rstrip().split(",") for s in lines)
line_count = 0
line = next(list_line)
while True:
    try:
        line = next(list_line)
        line_count += 1
        genres = line[-1].split("|")

        title = line[-2] if len(line) == 3 else ",".join(line[1:-1])
        title = title.strip()
        yearstr = title[-5:-1] if title[-1] != '"' else title[-6:-2]
        try:
            year = int(yearstr)
        except ValueError:
            print(title)

    except StopIteration:
        break
