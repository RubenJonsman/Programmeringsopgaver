import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Fixing random state for reproducibility
np.random.seed(19680801)


fig = plt.figure()
ax = Axes3D(fig)

colors = ['y', 'r', 'g', 'b', 'y']
yticks = [4, 3, 2, 1, 0]


for c, k in zip(colors, yticks):
    # Generate the random data for the y=k 'layer'.
    xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ys = [2, 1, 3, 4, 6, 12, 1, 3, 21, 32, 21]

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    #cs = [c] * len(xs)
    #cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=k, zdir='y', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# On the y axis let's only label the discrete values that we have data for.
ax.set_yticks(yticks)

plt.show()


import numpy as np
import matplotlib.pyplot as plt


# setup the figure and axes
fig = plt.figure(figsize=(8, 5))
ax1 = Axes3D(fig)
#ax2 = Axes3D(fig)

# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded')

#ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
#ax2.set_title('Not Shaded')

plt.show()