import numpy as np
a = np.random.random(100)
a.reshape(5,20)
print(a.reshape(5,20))
count = 0
for i in range(51):
    if i % 4 == 2:
        count += 1
        print(i)
np.l
print(count)