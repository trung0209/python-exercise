import random
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(6)]
print(color)