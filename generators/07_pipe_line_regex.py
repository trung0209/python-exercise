import re
from imdb import IMDb
import pandas as pd
file_name = "D:\gson\Book1.csv"
lines = (line for line in open(file_name,encoding="utf8"))
list_line = (s.rstrip().split(",") for s in lines)
line_count = 0
line = next(list_line) #skip the first line
df = pd.read_csv(file_name)
ia = IMDb()
while True:
    try:
        line = next(list_line)
        line_count += 1
        genres = line[-1].split("|")

        title = line[-2] if len(line) == 3 else ",".join(line[1:-1])

        movie = ia.search_movie(title)

        print(movie)
        id = []
        for i in range(len()):
            id.append(movie[i].movieID)
        title = title.strip()
        yearstr = title[-5:-1] if title[-1] != '"' else title[-6:-2]
        try:
            year = int(yearstr)
        except ValueError:
            year = re.search("\d{4}", title)
            # In ra bộ phim không có năm sản xuất
            if year is None:
               print(title)
    except StopIteration:

        break
