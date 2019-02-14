import matplotlib.pyplot as plt
import numpy as np

def average(a, b):
    return (a + b)/2

def babylon(n):
    x = []
    y = []

    # after 10 cycles, est will approximate the root
    est = n/2

    for i in range(10):

        # np.append([1,2], [2])
        # above same as [1,2] + [2]

        x = np.append(x, [est])
        y = np.append(y, [n/est])
        est = average(est, n/est)

    return est, x, y

root, x, y = babylon(int(input("enter number: ")))
print(root)

# we are graphing n/est because if n/est = est, est is the root
# the upper left corner of the graph should contain
# a point where the x and y values are nearly identical

plt.plot(x, y)
plt.show()
