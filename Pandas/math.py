# import matplotlib.pyplot as plt
# import numpy as np
# # data = {1940: 120, 1941: 122, 1942: 130, 1943: 110,
# # 1944:154, 1945: 165, 1946: 134, 1947: 128, 1948: 180, 1949:
# # 170, 1950:180, 1951:192} # Tạo dictionary
# # year = data.keys()
# # films = data.values()
# # plt.bar(year, films)
# # plt.title("Drama Film by year")
# # plt.legend(["film"])
# # plt.show()
# x = np.linspace(0, 2 *np.pi, 500)
# y = np.linspace(0, 10, 500)# từ 0 đến 2, chia ra 100
# plt.plot(x,np.sin(x),label = "sin")
#
# figure = plt.figure()
# ax1 = figure.add_subplot(221)
# ax2 = figure.add_subplot(222)
# ax3 = figure.add_subplot(223)
# ax4 = figure.add_subplot(224)
#
# ax1.set(label = "sin")
# ax2.set(label = "x^2")
# ax1.plot(x,np.sin(x))
# ax2.plot(y,y**2)
# plt.show()

def exponents(base,powers):
  temp = []
  for i in range(len(base)):
	  for j in range(len(powers)):
		  x = powers[i] * base[j]
		  temp.append(x)
		  result = temp
  return result