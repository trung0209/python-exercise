import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
#

# df = df.loc[df.market == 'MUMBAI', :]
#
# df = df[:30]
#
# df["realdate"] = df["date"].apply(lambda x: datetime.strptime(x, '%B-%Y').date())
#
# final = df.sort_values("realdate", ascending=True)
# print(final["realdate"])
# plt.xticks(rotation=45)
# plt.plot(final["realdate"], final["quantity"])
# plt.show()
#
#
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/MarketArrivals.csv')
# df = df.loc[df.market == 'MUMBAI', :]
# df = df[:30]
#
# print(df)
#
#
# def convert_month(row):
#     month_dict = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
#                   "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
#     return str(row["year"]) + "-" + month_dict[row["month"]]
#
#
# df["strdate"] = df.apply(convert_month, axis=1)
# print(df["strdate"])
# df = df.sort_values("strdate", ascending=True)
# df = df[:10]
# plt.xticks(rotation=45)
# plt.plot(df["strdate"], df["quantity"])
# plt.show()

filename = 'D:\gson/pima-indians-diabetes.csv'
data = pd.read_csv(filename)
output = data.groupby("9. Class variable (0 or 1)").size()
print(output)
print(data.shape)
peek = data.head(10)
print(peek)
print(data.dtypes)
print(data.describe())
pd.set_option('display.width', 100)
pd.set_option('precision', 2)
description = data.describe()
correlations = data.corr(method='pearson')
plt.matshow(data.corr())
data.hist(figsize=(12,8))
array = data.values
X = array[:, 0:8]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

print(rescaledX[0:5, :])
print(array)
le = preprocessing.LabelEncoder()
print(le.fit(["london","paris", "paris", "tokyo", "amsterdam", "hà nội",
"sài gòn"]))
list(le.classes_)
print(le.transform(["tokyo", "tokyo", "paris", "sài gòn"]))
print(list(le.inverse_transform([2, 2, 1, 3, 0])))
enc = preprocessing.OrdinalEncoder()
X = [['male', 'from US', 'uses Safari'],
['female', 'from Europe', 'uses Firefox'],
['male', 'from Asia', 'uses Safari'],
['female', 'from US', 'uses IE'],
['male', 'from Europe', 'uses Chrome'],
['female', 'from US', 'uses Safari'],
['male', 'from Asia', 'uses Chrome'],
['female', 'from Asia', 'uses Firefox']]
enc.fit(X)
result = enc.transform([['female', 'from US', 'uses Safari'],
['male', 'from Asia', 'uses Chrome']])
print(result)
# plt.show()