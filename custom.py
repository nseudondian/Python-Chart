import matplotlib.pyplot as plt

x = [1, 6, 9, 8, 12]
y = [1, 4, 7, 2, 5]

plt.plot(x, y, color='purple', linestyle='dashed', linewidth=2,marker='o', markerfacecolor='yellow', markersize=10 )

plt.ylim(1,12)
plt.xlim(1,12)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.show()