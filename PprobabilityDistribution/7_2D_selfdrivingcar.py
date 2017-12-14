
# coding: utf-8

# # Self Driving Car 2D World
#
# In the code cell, you'll find skeleton code for a class called
# SelfDrivingCar.
#
#
# The SelfDrivingCar class is initialized with the number of rows and number of
# columns in a 2D grid.
#
# The class also contains four methods.  You will need to implement these three
# methods
# * initialize_grid() - calculates the initial probabilities of each square on
# the grid
# * output_probability() - outputs the probability at a specific point on the
# grid
# * update_probability() - updates the probabilities at specific points on the
# grid
#
# The fourth method, visualize_probability(),visualizes the vehicle's 2D grid.
# This method is already provided for you.
#
# Follow the TODOs in the code.

# In[1]:
import matplotlib.pyplot as plt
from pandas import DataFrame

class SelfDrivingCar():
    def __init__(self, rows, columns):
        
        # initializes a map as a list
        self.grid = []
        for row in range(rows):
            self.grid += [[0] * columns]

        ### TODO:
        # initialize variables
        # self.grid_size is a list containing the number of rows
        # and number of columns in the grid like [10,3].  Use the rows and
        # columns input variables to define self.grid_size
        self.grid_size = [rows,columns]
        
        ### TODO:
        # store the total number of elements in the grid.  The number
        # of elements would be the rows * columns
        self.num_elements = rows * columns
        
    ### TODO:
    # write the function that initializes the grid.  Remember that
    # when the robot turns on, it has no idea where it is.  So if there
    # are 25 points on the grid, the initial probability of each point
    # is 1/25.
    # You will create a 2-D map using a python list.  This can be
    # a bit tricky, and you might have to search online for how to
    # program a 2-D list in python.  A 2-D list will need a for loop
    # within a for loop
    
    def initialize_grid(self):
        
        ### TODO:
        # calculate the probability of being at any element on the grid
        # you can use the self.num_elements variable you defined in the
        # __init__ function
        probability = 1 / self.num_elements
        
        ### TODO:
        # write a for loop to fill out the 2-D map with the value in the
        # probability variable.  For example, if the map has 25 points,
        # the map should be initialized to map[0,0] = 0.04
        # map[0,1] = 0.04
        # map[0, 2] = 0.04
        # etc.
        # python''s list.append() functionality might be helpful
        ###

        #for i in range(self.grid_size[0]):
        #   entry = []
        #   for j in range(self.grid_size[1]):
        #       entry.append(probability)
        #   self.grid.append(entry)


        rows = self.grid_size[0]
        columns = self.grid_size[1]
        for row in range(rows):
            for column in range(columns):
                self.grid[row][column] = probability
        return self.grid
    
    def output_probability(self, grid_point):
        
        ### TODO:
        # Given a point on the grid, such as [0,4] return the
        # current probability at that point.
        # You will need to use the self.map variable and combine it
        # with the grid_point and then return the probability
        return self.grid[grid_point[0]][grid_point[1]]
    
    def update_probability(self, update_list):
        
        #### TODO:
        # Given a list of grid_points and new probabilities,
        # update the probabilities of the grid points.
        # Here is an example input to this function
        # [[3,4,.01], [4,5,.02], [0, 1, .02]]
        # This means first update grid point (3,4) to have probability 0.01
        # Then update grid point (4,5) to have probability 0.02
        # Finally update grid point (0, 1) to have probability 0.02.
        # Your function will be updating the elements in the self.map variable
        for row in update_list:
            val_row = row[0]
            val_column = row[1]
            val = row[2]
            self.grid[val_row][val_column] = val
             
        return self.grid
            
    def visualize_probability(self):
        # this function is given so that you can visualize the results.
        # There is no need to change anything.

        # this line of code ensures TEST RUN button does not produce an error
        # if self.grid is empty.
        if not self.grid:
            self.grid = [[0],[0]]
        else:
            plt.imshow(self.grid, cmap='Greys', clim=(0,.1))
            plt.title('Heat Map of Grid Probabilities')
            plt.xlabel('grid x axis')
            plt.ylabel('grid y axis')
            plt.show()


# Run the cell below to try out your SelfDrivingCar class.

# In[ ]:
car = SelfDrivingCar(5,4)

car.initialize_grid()

# should output 0.05
print(car.output_probability([2,3]))

# should output 0.05
print(car.output_probability([1,2]))

car.update_probability([[2,3,.2], [1,2,.1]])

# should output 0.2
print(car.output_probability([2,3]))

# should output 0.1
print(car.output_probability([1,2]))

# should output a heat map
car.visualize_probability()


