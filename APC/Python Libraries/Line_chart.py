import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, color='blue', marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()