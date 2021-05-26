import numpy as np
import matplotlib.pyplot as plt
# Extracted straight from their respective .ipynb notebooks
thinned_fourrooms_list = [25, 45, 45, 40, 60, 55, 70, 80, 70, 65, 60]
thinned_small_list = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
thinned_maze6x6_list = [0, 0, 55, 65, 30, 55, 50, 70, 50, 65, 50]
thinned_maze11x11_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
thinned_spiral7x7_list = [0, 0, 0, 75, 70, 65, 75, 70, 80, 10, 20]
thinned_spiral9x9_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x_axis = np.arange(0, len(thinned_fourrooms_list) * 5000, 1 * 5000)
plt.figure(figsize=(10,5))
plt.plot(x_axis, thinned_fourrooms_list, label='Thinned FourRooms')
plt.plot(x_axis, thinned_small_list, label='Thinned Small')
plt.plot(x_axis, thinned_maze6x6_list, label='Thinned Maze6x6')
plt.plot(x_axis, thinned_maze11x11_list, label='Thinned Maze11x11')
plt.plot(x_axis, thinned_spiral7x7_list, label='Thinned Spiral7x7')
plt.plot(x_axis, thinned_spiral9x9_list, label='Thinned Spiral9x9')
plt.xlabel('Cleanup steps')
plt.ylabel('Success rate')
plt.legend()
plt.title('Success rate over cleanup steps')
plt.savefig('successes.jpg')
plt.clf()
plt.close()