import matplotlib.pyplot as plt

x1 = [1, 6, 9, 8, 12]
y1 = [1, 4, 7, 2, 5]

plt.plot(x1, y1, label = 'line 1')

x2 = [1, 2, 3, 4, 9]
y2 = [ 2, 6, 8, 12, 7]

plt.plot(x2, y2, label = 'Line 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('XY Graph')

plt.legend()

plt.show()