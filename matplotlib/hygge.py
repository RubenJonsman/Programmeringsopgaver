import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Laver vinduet
fig = plt.figure()

# Siger vi laver 3D
ax = Axes3D(fig)

# Antallet af bars
num_bars = 15

# Liste af forskellige x_positioner
x_pos = [8, 10, 15, 5, 6, 7, 0, 9, 14, 17, 2, 19, 12, 13, 18]
y_pos = [5, 6, 4, 14, 13, 18, 3, 10, 16, 0, 7, 17, 12, 11, 1]
z_pos = [0] * num_bars
print(len(y_pos))
# Størrelsen. Brede, længde = 1 Højde = random.
x_size = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]
y_size = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]
z_size = [17, 5, 9, 1, 4, 8, 7, 11, 6, 15, 10, 12, 18, 2, 3]

ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='aqua')
plt.show()