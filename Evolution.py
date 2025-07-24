import random as rand
import Map as map


class World:
      
      def __init__(self):
            self.creatures = []
            self.day_number = 0

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
                  creature.birth(self.new_borns)

      def grow_(self):
            for creature in self.creatures:
                  creature.grow() 

      def death_(self):
            for creature in self.creatures:
                  creature.check_death()

      def day_expenditure(self):
            for creature in self.creatures:
                  creature.energy_ -= 1
                  creature.thirst_ -= 1

      def fight(self):
            for c1 in self.creatures:
                  for c2 in self.creatures:
                        if c1 != c2:
                              if c1.position_x == c2.position_x and c1.position_y == c2.position_y:
                                    score = c1.strength_ - c2.strength_
                                    if score == 0:
                                          pass
                                    elif score > 0:
                                          c2.energy_ = 0
                                    elif score < 0:
                                          c1.energy_ = 0

      def food_reset():
            #use if want to reset the amount of food to always have the same amount of food in circulation as when game generated
            global food_eaten

            map.create_food_points(food_eaten)
            food_eaten = 0

      def map_creatures(self):
            for creature in self.creatures:
                  map.create_creature_points()
      
      def day(self):
            self.day_number += 1

            self.new_borns = []
            map.creature_points = []
            self.map_creatures()
            
            self.fight()
            self.eat_()  
            self.drink_()
            self.grow_()

            self.birth_()

            self.move_()

            self.day_expenditure()
            self.death_()

            map.create_food_points(rand.randint(10,25)) #use if want random amount of food to grow each year independent of amount eaten
            
            for baby in self.new_borns:
                  map.world.creatures.append(baby)
            print(len(map.world.creatures))

class Creature:
    def __init__(self, world, energy = 50, strength = rand.randint(1,50),thirst = rand.randint(1,50), r_k = rand.randint(1, 25), birth_t = rand.randint(10,25), baby_exp = rand.randint(1,50), growth_t = rand.randint(10,25), growth_exp = rand.randint(1,25)):

        self.energy_ = energy
        self.thirst_ = thirst
        self.strength_ = strength

        self.r_k_selection_ = r_k

        self.position_x = rand.randint(1,50)
        self.position_y = rand.randint(1,50)
        self.hori_move_ = rand.randint(1,3)
        self.vert_move_ = rand.randint(1,3)

        self.birth_threshold = birth_t
        self.baby_expenditure = baby_exp

        self.growth_threshold = growth_t
        self.growth_expenditure = growth_exp


    def grow(self):
            #print("growth_t: " + str(self.growth_threshold))
            #print("growth_exp: " + str(self.growth_expenditure))
            if self.energy_ >= self.growth_threshold:
                  print("creature growth!!!")
                  self.strength_ += self.growth_expenditure
                  self.energy_ -= self.growth_expenditure

    def birth(self, new_borns):

          #print("baby_t: " + str(self.birth_threshold))
          #print("baby_exp: " + str(self.baby_expenditure))          
          if self.energy_ >= self.birth_threshold:
            print("new babies!!!")
            self.energy_ -= self.baby_expenditure #loss of energy from parent

            for baby in range(self.r_k_selection_):
         
                  child_energy = 20 + self.baby_expenditure/self.r_k_selection_
                  child_thirst = 20 + self.thirst_/self.r_k_selection_

                  child_strength = 0
                  inh_child_strength = self.strength_/self.r_k_selection_

                  child_r_k_selection = 0
                  child_birth_t = 0
                  child_baby_exp = 0
                  child_growth_t = 0
                  child_growth_exp = 0
                  
                  child_strength = random_mutation(child_strength, inh_child_strength, 1, 0, 10, -2, 2)
                  child_r_k_selection = random_mutation(child_r_k_selection, self.r_k_selection_, 4, 0, 10, -2, 2)
                  child_birth_t = random_mutation(child_birth_t, self.birth_threshold, 8, 0, 10, -2, 2)
                  child_baby_exp = random_mutation(child_baby_exp, self.baby_expenditure, 3, 0, 10, -2, 2)
                  child_growth_t = random_mutation(child_growth_t, self.growth_threshold, 7, 0, 10, -2, 2)
                  child_growth_exp = random_mutation(child_growth_exp, self.growth_expenditure, 10, 0, 10, -2, 2)

                  new_borns.append(Creature(world = map.world, energy=child_energy, strength=child_strength, thirst=child_thirst, r_k=child_r_k_selection, birth_t=child_birth_t, baby_exp=child_baby_exp, growth_t=child_growth_t, growth_exp=child_growth_exp))

    def check_death(self):
          if self.energy_ <= 0:
                self.death(map.world)
          elif self.thirst_ <= 0:
                self.death(map.world)

    def death(self, world):
          print("creature died!")
          world.creatures.remove(self)

    def move(self):
            for x in range(self.hori_move_):
                  move = rand.randint(-1,1) #produces back and forth movement
                  self.position_x += move
                  if move == 0:
                        pass
                  else:
                        self.energy_ -= 1

                  if self.position_x > 50:
                       self.position_x -= 50
                  if self.position_x < 0:
                        self.position_x += 50

            for y in range(self.vert_move_):
                  move = rand.randint(-1,1) #produces back and forth movement
                  self.position_y += move
                  if move == 0:
                        pass
                  else:
                        self.energy_ -= 1

                  if self.position_y > 50:
                       self.position_y -= 50 
                  if self.position_y < 0:
                        self.position_y += 50
            
            #print((self.position_x, self.position_y))
    
    def eat(self):
      #print("energy: " + str(self.energy_))
      for point in range(len(map.food_source)):
            if self.position_x == map.food_source[point][0] and self.position_y == map.food_source[point][1]:
                  print("food eaten!!!")
                  self.energy_ += 10
                  map.food_source.remove(map.food_source[point])
                  break
   
    def drink(self):
      #print("thirst: " + str(self.thirst_))
      for point in range(len(map.water_source)):
            #print("water drunk!!!")
            if self.position_x == map.water_source[point][0] and self.position_y == map.water_source[point][1]:
                  self.thirst_ += 10

def create_creature(world, number = 50):
      for x in range(number):
            map.world.creatures.append(Creature(world))

def random_mutation(inherited, parent, random_no, r_range_min, r_range_max, v_range_min, v_range_max):
      random = rand.randint(r_range_min, r_range_max)
      if random == random_no:
            inherited = parent + rand.randint(v_range_min, v_range_max)
      else:
            inherited = parent
      return(inherited)
