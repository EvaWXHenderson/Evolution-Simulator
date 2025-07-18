import random as rand
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

creature_points = []
water_source = []
food_source = []

def create_map(size_):
      global creature_points, water_source, food_source

      plt.style.use('_mpl-gallery-nogrid')
      cmap = ListedColormap(["mediumseagreen","powderblue","firebrick","sienna"])

      fig, ax = plt.subplots()

      size = size_
      Z = [[0 for x in range(size)] for x in range(size)]
      
      for x in range(len(water_source)):
        Z[water_source[x][0]] [water_source[x][1]] = 1

      for x in range(len(food_source)):
        Z[food_source[x][0]] [food_source[x][1]] = 2

      for x in range(len(creature_points)):
        Z[creature_points[x][0]] [creature_points[x][1]] = 3

      ax.imshow(Z, origin='lower',cmap=cmap)
      plt.show()

def create_creature_points(x, y, creatures = 50):
      global creature_points

      for x in range(creatures):
            c_point = (x, y)
            creature_points.append(c_point)

def create_water_points(water_source, size = 25):

    base_point = (rand.randint(0,50), rand.randint(0,50))
    water_source.append(base_point)

    for x in range(size):
        new_point = water_source[-1].copy()
        new_point[0] += rand.randint(-1,1)
        new_point[1] += rand.randint(-1,1)
        if new_point[0] > 0 and new_point[0] < 50 and new_point[1] > 0 and new_point[1] < 50:
            water_source.append((new_point[0], new_point[1]))

def create_food_points(items = 50):
    global food_source

    for x in range(items):
        f_point = (rand.randint(0,50), rand.randint(0,50))

        for point in water_source:
            if f_point == point:
                create_food_points()
        else:
            food_source.append(f_point)

"""create_creature_points()
create_water_points(water_source, 25)
create_water_points(water_source, 50)
create_water_points(water_source, 75)
create_food_points()

create_map(51)"""