import pandas as pd
df = pd.read_csv("D:\gson/movies.csv")
df["Years"] = df['title'].apply(lambda x: x[-5:-1])
movies_1995 = df[df.Years == '1995']
movies_1995_gernes = movies_1995["genres"].apply(lambda x : x.split("|"))


print(movies_1995_gernes)

