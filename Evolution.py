import random as rand
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class World:
      
      def __init__(self):
            creatures = []

class Creature:
    def __init__(self,world, energy = rand.randint(1,50), size = rand.randint(1,50), speed = rand.randint(1,50), strength = rand.randint(1,50), health = rand.randint(1,50), thirst = rand.randint(1,50)):
        energy_ = energy
        size_ = size
        speed_ = speed
        strength_ = strength
        health_ = health
        thirst_ = thirst

        r_k_selection_ = rand.randint(1, 50)

        position_x = rand.randint(1,100)
        position_x = rand.randint(1,100)
        hori_move_ = rand.randint(1,5)
        vert_move_ = rand.randint(1,5)

        world.creatures.append(self)

    def grow(self):
            x = rand.randint(1,50)
            self.size += x
            self.energy -= 2*x
    def heal(self):
            x = rand.randint(1,50)
            self.health += x
            self.energy -= 2*x
    def stronger(self):
            x = rand.randint(1,50)
            self.strength += x
            self.energy -= 2*x

    def birth(self):
          y = rand() #will represent the amount of energy expenditure desired for kids

          for x in range(self.r_k_selection):
                child_energy = (self.energy / y)/x """all need to appropriately weighted"""
            
                child_size = self.size + self.energy
                child_speed = self.speed
                child_strength = self.strength
                child_health = self.health
                child_thirst = self.thirst
                (Creature(child_energy, child_size, child_speed, child_strength, child_health, child_thirst))

    def move(self):
        self.position_x  = self.position_x + self.hori_move
        self.position_y  = self.position_y + self.vert_move

    def find_food(self):
    def find_water(self):
          
def create_food():
def create_water():
      

def day():
      #eat
      #drink
      #birth
      #fight
      #next day