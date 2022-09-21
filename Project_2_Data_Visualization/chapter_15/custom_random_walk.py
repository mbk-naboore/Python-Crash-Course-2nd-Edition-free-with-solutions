import matplotlib.pyplot as plt
from random import choice

""" This project can make some fantastic patterns(photos)
 visually you will have fun making it, 
 and enjoying some of the created patterns."""

""" To have an infinity loop and each time you close the matplotlib
window another is created you can comment (the last three lines), but be aware
that in order to stop the loop you have to kill the code yourself..."""


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    pass


while True:
    # Make a random walk.
    rw = RandomWalk(100000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 15), dpi=130)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.plasma, edgecolor="none")

    # Emphasize the first and last points.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Make it a full-screen:
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


