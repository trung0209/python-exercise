import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML


df = pd.read_csv('D:\gson\gdp_csv.csv',
                 usecols=['Country Name', 'Country Code', 'Year', 'Value'])

code = set(df['Country Code'].values)
colour_list = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(len(code))]

colour = []
for i in range(len(code)):
    temp = "#" + "".join([random.choice('0123456789ABCDEF') for i in range(6)])
    colour.append(temp)
print(colour)
# default = ['#adb0ff' for i in range(len(code))] #1 color only

colors = dict(zip(code, colour))
group_lk = df.set_index('Country Name')['Country Code'].to_dict()

fig, ax = plt.subplots(figsize=(15, 8))
print(colors)
def draw_barchart(year):
    dff = (df[df['Year'].eq(year)].sort_values(by='Value', ascending=False).head(10))
    dff = dff[::-1]
    ax.clear()
    ax.barh(dff['Country Name'], dff['Value'], color=[colors[group_lk[x]] for x in dff['Country Name']])
    dx = dff['Value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['Value'], dff['Country Name'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value - dx, i - .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'GDP', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'GDP',transform=ax.transAxes, size=24, weight=600, ha='left')

    plt.box(False)

animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1960, 2017))
HTML(animator.save("mymovie.html"))
