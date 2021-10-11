import pygal
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

rw_points = []
for value in range(1, rw.num_points):
    point = (rw.x_values[value], rw.y_values[value])
    rw_points.append(point)

# Plot the random walk using Pygal.

rw_plot = pygal.XY(stroke=False, dotsize=1)

rw_plot.title = "Random Walk"

rw_plot.add('Steps', rw_points)
rw_plot.render_to_file('rw_visualization.svg')
