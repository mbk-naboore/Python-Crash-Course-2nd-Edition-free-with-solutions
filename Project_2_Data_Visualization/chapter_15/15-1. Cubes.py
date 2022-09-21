import matplotlib.pyplot as plt

#making the x-y values
x_values = list(range(0, 5001))
y_values = [x**3 for x in x_values]

#creating the plot and style
plt.style.use(["fivethirtyeight", "bmh"])
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=2.5)

# title and labels
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value*Value*Value(cube)", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

# showing the output
plt.show()


