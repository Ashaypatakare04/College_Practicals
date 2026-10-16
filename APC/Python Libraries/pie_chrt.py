import matplotlib.pyplot as plt
x= [40, 30, 20, 10]
y = ['A', 'B', 'C', 'D']

plt.pie(x, labels=y,startangle=90)
plt.title("Pie Chart")
plt.show()