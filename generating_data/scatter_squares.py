from shutil import which
import matplotlib.pyplot as plt

#input = x values
inputs = range(1, 1001)
#squares = y values - using map and lambda
squares = list(map(lambda input: input**2, inputs))

#plot a single point
#use x and y coordinates, then c and cmap to make color gradiante
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(inputs, squares, c=squares, cmap=plt.cm.Blues, s=10)

#set chart title and lavel axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#set this range of each axis
ax.axis([0, 1100, 0, 1100000])

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize = 14,)

#remove scientific notation
plt.ticklabel_format(style='plain')

#shave plot to file. Show plot
plt.savefig('sqaures_plot.png', bbox_inches ='tight')
plt.show()
