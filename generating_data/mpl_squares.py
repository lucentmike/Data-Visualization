import matplotlib.pyplot as plt
print(plt.style.available)

#input = x values
inputs = [1, 2, 3, 4, 5]
#squares = y values
squares = [1, 4, 9, 16 ,25]

#create a figure with subplots, assign style, Then plot the numbers
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(inputs, squares, linewidth=3)

#set chart title and lavel axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#set size of tick labels
ax.tick_params(axis='both', labelsize = 14)

#show the figure and plot
plt.show()

