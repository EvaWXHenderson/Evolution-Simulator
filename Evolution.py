import random as rand
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import Map as map

creature_points = ()
water_source = ()
food_source = ()

class World:
      
      def __init__(self):
            self.creatures = []

      def eat_(self):
            for creature in self.creatures:
                  creature.eat()

      def drink_(self):
            for creature in self.creatures:
                  creature.drink()

      def move_(self):
            for creature in self.creatures:
                  creature.move()

      def birth_(self):
            for creature in self.creatures:
                  creature.birth()

      def grow_(self):
            for creature in self.creatures:
                  creature.grow() 

      def death_(self):
            for creature in self.creatures:
                  creature.check_death()

      def day_expenditure(self):
            for creature in self.creatures:
                  creature.energy -= 1
                  creature.thirst -= 1

      def fight(self):
            for c1 in self.creatures:
                  for c2 in self.creatures:
                        if c1 != c2:
                              if c1.position_x == c2.position_x and c1.position_y == c2.position_y:
                                    score = c1.strength - c2.strength
                                    if score == 0:
                                          pass
                                    elif score > 0:
                                          c2.death(world = self)
                                    elif score < 0:
                                          c1.death(world = self)

      def day(self):
            self.fight()
            self.eat_()           
            self.drink_()
            self.grow_()
            self.birth_()
            self.move_()
            self.day_expenditure()
            self.death_()
      



class Creature:
    def __init__(self, world, energy = rand.randint(1,50), size = rand.randint(1,50), speed = rand.randint(1,50), strength = rand.randint(1,50), health = rand.randint(1,50), thirst = rand.randint(1,50), r_k = rand.randint(1, 50), birth_t = (1,50), baby_g = (1,50), growth_t = (1,50), growth_exp = (1,50)):

        energy_ = energy
        thirst_ = thirst
        strength_ = strength

        r_k_selection_ = r_k

        position_x = rand.randint(1,100)
        position_y = rand.randint(1,100)
        hori_move_ = rand.randint(1,5)
        vert_move_ = rand.randint(1,5)

        birth_threshold = birth_t
        baby_gift = baby_g

        growth_threshold = growth_t
        growth_expenditure = growth_exp

        world.creatures.append(self)

    def grow(self):
            if self.energy >= self.birth_threshold:
                  x = rand.randint(1,50)
                  self.strength += x
                  self.energy -= 2*x

    def birth(self):
          if self.energy >= self.birth_threshold:

            for x in range(self.r_k_selection):
                  child_energy = self.baby_gift/x
                  child_thirst = self.thirst
                  child_size = self.size
                  child_speed = self.speed
                  child_strength = self.strength
                  child_r_k_selection = self.r_k_selection

                  (Creature(child_energy, child_size, child_speed, child_strength, child_health, child_thirst))

    def check_death(self):
          if self.energy <= 0:
                self.death()
          if self.thirst <= 0:
                self.death()

    def death(self, world):
          world.creatures.remove(self)

    def move(self):
            for x in range(len(self.hori_move)):
                  self.position_x += x
                  self.energy -= 1
            for y in range(len(self.vert_move)):
                  self.position_y += y
                  self.energy -= 1
    
    def eat(self):
      global food_source

      for point in food_source:
            if self.position_x == food_source[point][0] and self.position_y == food_source[point][1]:
                  self.energy += 10
                  food_source.remove(food_source[point])
   
    def drink(self):
      global water_source

      for point in water_source:
            if self.position_x == water_source[point][0] and self.position_y == water_source[point][1]:
                  self.thirst += 10
                  water_source.remove(water_source[point])



def create_creature(world, number = 50):
      for x in range(number):
            Creature(world)

world_1 = World

create_creature(world_1)

map.create_food_points(50)
map.create_water_points(75)
map.create_water_points(75)
map.create_creature_points(Creature.position_x, Creature.position_y, 50)

map.create_map(51)

"""while x < 100:
      for creature in World.creatures:
            World.day(creature)
      
      x += 1"""