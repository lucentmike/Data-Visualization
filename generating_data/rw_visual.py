from random_walk import RandomWalk
import matplotlib.pyplot as plt


while True:
    rw = RandomWalk(num_points=10000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.scatter(rw.x_values, rw.y_values,c = range(rw.num_points), cmap=plt.cm.Blues, edgecolors='none', s=1)

    #emphasize the first and last point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    while True:
        keep_plotting = input("Plot again? Enter Y or N: ")
        if keep_plotting.lower() != 'n' or 'y':
            pass
        if keep_plotting.lower() == 'y':
            break       
        if keep_plotting.lower() == 'n':
            quit()
