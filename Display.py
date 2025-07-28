import Evolution as evo
import Map as map

"""PLAN:
No. creatures
No. of babies had
Pieces of food consumed

averages of: strength
            birth threshold + expenditure
            growth threshold + expenditure
            
            horizontal movement
            vertical movement"""

"""be able to click on a creature:
- print of stats in terminal
- requires slow enough interval arg.
"""

food_eaten = 0
babies = 0
deaths = 0

def end_stats():
    number = 1

    for creature in map.world.creatures:
        print("creature: " + str(number))
        print("energy: " + str(creature.energy_))
        print("thirst: " + str(creature.thirst_))
        print("strength: " + str(creature.strength_))
        print("horizontal movement: " + str(creature.hori_move_))
        print("vertical movement: " + str(creature.vert_move_))
        print("baby expenditure: " + str(creature.baby_expenditure))
        print("growth expenditure: " + str(creature.growth_expenditure) + "\n")
    
        number+=1

def day_stats():
        global food_eaten, babies, deaths

        print("Day: " + str(map.world.day_number))
        print("number of creatures: " + str(len(map.world.creatures)))
        print("babies born: " + str(babies))
        print("deaths: " + str(deaths))
        print("food eaten: " + str(food_eaten) + "\n")
        
        food_eaten = 0
        babies = 0
        deaths = 0

def onclick(event):
     global ix, iy
     iy, ix= round(event.xdata), round(event.ydata)

     for creature in map.world.creatures:
          if creature.last_x == ix and creature.last_y == iy:
               print("Position: " + str((ix, iy)) + "\n"
                     "Horizontal bias: " + str(creature.hori_move_) + "\n"
                     "Vertical bias: " + str(creature.vert_move_) + "\n"
                     
                    "Energy: " + str(creature.energy_) + "\n"
                    "Thirst: " + str(creature.thirst_) + "\n"
                    "Strength: " + str(creature.strength_) + "\n"

                    "Growth threshold: " + str(creature.growth_threshold) + "\n"
                    "Growth expenditure: " + str(creature.growth_expenditure) + "\n"

                    "Birth threshold: " + str(creature.birth_threshold) + "\n"
                    "Birth expenditure: " + str(creature.baby_expenditure))
               return 
          
     print("Creature not found at: " + str((ix, iy)))