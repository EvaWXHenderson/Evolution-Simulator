import random as rand
import Map as map
import Display as dsp



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

      def birth_one(self):
            for creature in self.creatures:
                  creature.birth_one(self.new_borns)

      def birth_multi(self):
            for creature in self.creatures:
                  creature.birth_multi(self.new_borns)

      def grow_(self):
            for creature in self.creatures:
                  creature.grow() 

      def death_(self):
            for creature in self.creatures:
                  creature.check_death()

      def day_expenditure(self):
            for creature in self.creatures:
                  creature.energy_ -= 1
                  creature.thirst_ -= 2

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
      
      def growth_birth(self):
            for creature in self.creatures:
                  choice = rand.randint(0,1)
                  
                  if choice == 0:
                        self.birth_one()
                  elif choice == 1:
                        self.grow_()
                
      def day(self):
            global babies, food_eaten

            self.day_number += 1

            self.new_borns = []
            map.creature_points = []
            
            self.move_()

            self.fight()
            self.eat_()  
            self.drink_()

            self.growth_birth()

            self.day_expenditure()
            self.death_()

            for item in map.food_source:
                  map.food.ageing(item)
                  map.food.decay(item, decay_rate=10)

            map.create_food(rand.randint(5,25)) #use if want random amount of food to grow each year independent of amount eaten
            
            map.food_points = []

            map.create_food_points()

            for baby in self.new_borns:
                  map.world.creatures.append(baby)

            dsp.day_stats()
            self.map_creatures()


class Creature:
    def __init__(self, world, pos_x = None, pos_y = None, energy = 25, strength = rand.randint(1,50), thirst = 25, r_k = rand.randint(1, 25), birth_t = rand.randint(10,25), baby_exp = rand.randint(1,24), growth_t = rand.randint(10,25), growth_exp = rand.randint(1,24)):

        self.energy_ = energy
        self.thirst_ = thirst
        self.strength_ = strength

        self.r_k_selection_ = r_k
      
        if pos_x == None and pos_y == None:
            self.position_x = rand.randint(1,50)
            self.position_y = rand.randint(1,50)
        else:
              self.position_x = pos_x
              self.position_y = pos_y

        self.last_x = self.position_x
        self.last_y = self.position_y
        
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
                  #print("creature growth!!!")
                  self.strength_ += self.growth_expenditure
                  self.energy_ -= self.growth_expenditure

    def birth_one(self, new_borns):
          global babies

          if self.energy_ >= self.birth_threshold and self.energy_ >= self.baby_expenditure:
            dsp.babies += 1
            self.energy_ -= self.baby_expenditure
      
            child_energy = 10 + self.baby_expenditure
            child_thirst = 10 + self.thirst_

            child_strength = 0

            child_r_k_selection = 0
            child_birth_t = 0
            child_baby_exp = 0
            child_growth_t = 0
            child_growth_exp = 0
            
            child_strength = random_mutation(child_strength, self.strength_, 1, 0, 10, -2, 2)
            child_r_k_selection = random_mutation(child_r_k_selection, self.r_k_selection_, 4, 0, 10, -2, 2)
            child_birth_t = random_mutation(child_birth_t, self.birth_threshold, 8, 0, 10, -2, 2)
            child_baby_exp = random_mutation(child_baby_exp, self.baby_expenditure, 3, 0, 10, -2, 2)
            child_growth_t = random_mutation(child_growth_t, self.growth_threshold, 7, 0, 10, -2, 2)
            child_growth_exp = random_mutation(child_growth_exp, self.growth_expenditure, 10, 0, 10, -2, 2)

            new_borns.append(Creature(world = map.world, pos_x = self.position_x, pos_y = self.position_y, energy=child_energy, strength=child_strength, thirst=child_thirst, r_k=child_r_k_selection, birth_t=child_birth_t, baby_exp=child_baby_exp, growth_t=child_growth_t, growth_exp=child_growth_exp))
          
    def birth_multi(self, new_borns):

          #print("baby_t: " + str(self.birth_threshold))
          #print("baby_exp: " + str(self.baby_expenditure))          
          if self.energy_ >= self.birth_threshold and self.energy_ >= self.baby_expenditure:
            #print("new babies!!!")
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
          dsp.deaths += 1
          world.creatures.remove(self)

    def move(self):
            move = rand.randint(-1,1) #produces back and forth movement
            
            self.last_x = self.position_x
            self.last_y = self.position_y

            for x in range(self.hori_move_):   
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
      eat = False

      for point in range(len(map.food_source)):
            if self.position_x == map.food_points[point][0] and self.position_y == map.food_points[point][1]:
                  self.energy_ += 15
                  map.food_source.remove(map.food_source[point])

                  eat = True

                  break

      if eat == True:
            dsp.food_eaten += 1
   
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
            if parent <= v_range_max:
                  random = abs(random)
            elif parent > v_range_max:
                  inherited = parent + rand.randint(v_range_min, v_range_max)
      else:
            inherited = parent
      return(inherited)
