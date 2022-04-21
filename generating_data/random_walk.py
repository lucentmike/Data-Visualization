import matplotlib.pyplot as plt
import random 

#create class for random walk
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    #method to fill up values with steps
    def fill_walk(self):

        # while number of values is less than points keep going
        while len(self.x_values) < self.num_points:

            #choice and direction and distance, multiply to get step value
            x_direction = random.choice([-1, 1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance 

            #choice and direction and distance, multiply to get step value
            y_direction = random.choice([-1,1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance 

            #if step value is 0 continue 
            if x_step ==0 and y_step ==0:
                continue

            #add last value to the step to get new step the append to values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == "__main__":

    #genrate a random walk instance and use fill walk method to create points
    rw = RandomWalk(num_points=6000)
    rw.fill_walk()

    #plot walk
    plt.style.use('classic')
    fig, ax =plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

