import matplotlib.pyplot as plt

left = [1, 6, 9, 8, 12]
height = [30, 20, 15, 25, 12]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label=tick_label, width=0.9, color=['purple', 'yellow'])


plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Bar Chart')

plt.legend()

plt.show()