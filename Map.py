import random as rand
import Evolution as evo

creature_points = []
water_source = []
food_source = []
food_points = []
world = None
image = None

class food:
    def __init__(self):
        self.age = 0
        self.f_point = (rand.randint(0,50), rand.randint(0,50))

    def ageing(self):
        self.age += 1

    def decay(self, decay_rate = 10):
        if self.age > decay_rate:
            food_source.remove(self)

def create_creature_points():
      global creature_points
    
      for creature in world.creatures:
            new_point = (creature.position_x, creature.position_y)
            creature_points.append(new_point)

def create_water_points(water_source, size = 25):

    base_point = (rand.randint(0,50), rand.randint(0,50))
    water_source.append(base_point)

    for x in range(size):
        new_point = (water_source[-1][0]+rand.randint(-1,1), water_source[-1][1]+rand.randint(-1,1))

        if new_point[0] > 0 and new_point[0] < 50 and new_point[1] > 0 and new_point[1] < 50:
            water_source.append(new_point)

def create_food(items = 50):
    global food_source, water_source

    for x in range(items):
        food_item = food()

        for point in water_source:
            if food_item.f_point == point:
                create_food(1)
        else:
            food_source.append(food_item)

def create_food_points():
    global food_source, food_points
    
    for item in food_source:
        food_points.append(item.f_point)

def create_base_map():
      create_water_points(water_source=water_source, size=75)
      create_water_points(water_source=water_source, size=200)
      create_water_points(water_source=water_source, size=200)
      create_water_points(water_source=water_source, size=50)
      create_food(50)
      create_food_points()
      evo.World.map_creatures(world)

def Z_update(size_ = 51):
      global creature_points
      
      size = size_
      Z = [[0 for x in range(size)] for x in range(size)]
      
      for x in range(len(water_source)):
        Z[water_source[x][0]] [water_source[x][1]] = 1

      for x in range(len(food_source)):
        Z[food_points[x][0]] [food_points[x][1]] = 2

      for x in range(len(creature_points)):
        try:
          Z[creature_points[x][0]] [creature_points[x][1]] = 3
        except:
            print("x:",x)
            print("c:",creature_points[x])

      return Z

def update_map(frame):
    world.day()
    Z = Z_update()
    image.set_data(Z)
    return[image]
    