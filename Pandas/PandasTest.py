import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, date
df = pd.read_csv("D:\gson/1000employee.csv")
df2 = pd.read_csv("D:\gson/OfficeSupplies.csv")

# data_url = "http://bit.ly/2cLzoxH"
# # data_get = pd.read_csv(data_url)
# country_list = ["Hong Kong China","Japan","Korea Rep"]
# condition1 = data_get[data_get.continent=="Asia"]
# condition2 = condition1[~condition1.country.isin(country_list)]
# condition3 = condition2.nsmallest(condition2.size,"gdpPercap")
# condition = data_get.nsmallest(5,"gdpPercap",keep="first")
# # print(condition)
# print(condition3)
#
# df = pd.read_csv("D:\gson/OfficeSupplies.csv")
# frame2 = df[["Rep", "Item"]]
# frame2.to_csv("rep_item.csv")
# print(frame2)
# sheet = pd.read_excel('DanhSach.xlsx', 'Sheet1')  #Thông kê tuổi
# print('Min: ', sheet['Age'].min())
# print('Max: ', sheet['Age'].max())
# print('Sum: ', sheet['Age'].sum())
# print("----- Short by Age ------")
# print(sheet['Age'].sort_values())
# print("----- Cell at row[1] of column['Xưng hô'] ------")
# print(sheet['Xưng hô'][1])
# print("----- column Age ---------")
# print(sheet['Age'].values)
# Loop through data frame for index, row in sheet.iterrows():   print(f"{row[0]} - {row[1]} {row[2]} có tuổi là {row[4]}")
# nestdict = {'red': {2012: 22, 2013: 33, 2014: 20},
#             'white': {2011: 13, 2012: 22, 2013: 16},
#             'blue': {2011: 17, 2012: 27, 2013: 18},
#             'green': {2011: 12, 2013: 22, 2014: 35}}
# frame2 = pd.DataFrame(nestdict)
# df = pd.read_csv("D:\gson/OfficeSupplies.csv")
# frame2 = df[["Rep", "Item", "Units", "Unit Price"]].head(20)
# frame2.to_csv("rep_item.csv")
# # print(frame2)
# # print(frame2.T)
# df["Total Price"] = df["Units"] * df["Unit Price"]
# sort_by_unit = df.groupby(["Rep"]).sum()
#     # .sum().sort_values("Total Price", ascending=False)
# print(sort_by_unit)

# bins = [20, 25, 30, 35, 40, 45, 50, 55, 60]
# df = pd.read_csv("D:\gson/1000employee.csv")
# group = df.groupby([pd.cut(df.Age, bins),"Gender"]) #nhom theo tuoi va gioi tinh
#
# # print(group)
# group_size = group.size()
# # print(group_size)
# age_group = group_size.unstack()
# print(age_group)

# age_group.plot(kind="bar", stacked = True)
# plt.show()
# frame = df[["Age"]]
# frame.to_csv("age.csv")
# print([pd.cut(df.Age, bins)])
# print(age_group)
# age_group.plot(kind='bar')
# plt.show()




# df = pd.read_csv("D:\gson/1000employee.csv")
# df["Living Days"] = df['Date of Birth'].apply(lambda x: (pd.to_datetime('today') - pd.to_datetime(x[:-2] + "19" + x[-2:], format="%m/%d/%Y")).days)
# print(df[['Date of Birth', 'Living Days']])
df = pd.DataFrame({
   'name':['john','mary','peter','jeff','bill','lisa','jose'],
   'age':[23,78,22,19,45,33,20],
   'gender':['M','F','M','M','M','F','M'],
   'state':['california','dc','california','dc','california','texas','texas'],
   'num_children':[2,0,0,3,2,1,4],
   'num_pets':[5,1,0,5,2,2,3]
})

print(df.head(6))
# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter', x='age', y='num_children', color='red')

plt.show()
# col = 'Date of Birth'
# df[col] = pd.to_datetime(df[col])
# future = df[col] > pd.Timestamp(year=2050, month=1, day=1)
# df.loc[future, col] -= timedelta(days=365.25 * 100)
# df["Livingday"] = (pd.to_datetime('today') -
# pd.to_datetime(df[col])).apply(lambda x: x.days)
# # pd2.to_datetime(df[col])).apply(lambda x: x.days)
# print(df[["Livingday", "Date of Birth"]])
