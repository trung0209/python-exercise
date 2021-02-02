import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/phamdinhkhanh/LSTM/master/international-airline-passengers.csv")
# uncomment 2 line below first and run once then comment them again
data["Passengers"] = data["International airline passengers: monthly totals in thousands. Jan 49 ? Dec 60"]
data = data.drop(columns="International airline passengers: monthly totals in thousands. Jan 49 ? Dec 60")
data['Date'] = data['Month'].apply(lambda x: int(x.split("-")[0][-2:]+x.split("-")[1][-2:]))
# data['Date']=data['Date'].map(dt.datetime.toordinal)

def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0.0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -(2/N) * diff
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff
    return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    for i in range(num_iterations):
        b,m = step_gradient(b, m, x, y, learning_rate)
    return [b, m]

point =int(input("enter number of point"))

year = np.array(data["Month"].head(point))
date = np.array(data["Date"].head(point))
passenger = np.array(data["Passengers"].head(point))

b,m = gradient_descent(date,passenger,0.0001,1000)
ypredict = [m*i+b for i in date]
print(ypredict)
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 1.5, 1.5]) # main axes

sns.lmplot(x="Date",y="Passengers",data=data.head(point))
axes1.scatter(year,passenger)
axes1.plot(year,ypredict)