import math
import random
import itertools
import copy
from collections import OrderedDict
from operator import itemgetter
from tsp import *


number_of_cities = 20
for _ in range(number_of_cities):
    city = dict()
    a = City()
    city["id"] = a.id
    city["x"] = a.x
    city["y"] = a.y
    list_of_all_cities.append(city)
# calculate the distances of between every city and saves it into global distances variable


calc = Calculators()
calc.calculateRoute(list_of_all_cities)

#print(distances)



for city in list_of_all_cities:
    city_id_list.append(city["id"])



#print(list_of_all_cities)



# populationGenerator = Population()

# a = populationGenerator.generate(list_of_all_cities)
# print(a)

def pairwise(iterable:list):
    """
    Creates a pair of touples:
        from [1, 2, 3, 4, 5, 6]
        (1, 2), (2, 3), (3, 4), ..
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def geneticAlgorithm(numberOfGenerations:int, populationSize:int):
    
    initial_population_list = list()  # defining intial population before the first loop
    populationGenerator = Population()
    for i in range(populationSize):
        initial_population_list.append(populationGenerator.generate(city_id_list))
    #print(initial_population_list, "this is initial population")
    bestDistance = math.inf
    bestRoute = None


    


    for generation in range(numberOfGenerations):
        
        next_population_temp = list()
        next_population_list = list()
        populationGenerator = Population()
        calculator = Calculators()
        distances_dict = dict() # this dict will keep the index of route with its distance
        

        
        
        # calculating the distances of initial population
        for populationIndex, population in enumerate(initial_population_list):
            #print(population)
            route_dist = 0
            try:
                for pair in pairwise(population):
                    #print(pair)
                    start, destination = pair
                    route_dist += distances[start-1][start][destination]
                    distances_dict[populationIndex] = route_dist
            except: TypeError
            pass
        # Now we sort this dictionary by values, and extract the best route with minimum distance, save it
        ordered_dict = OrderedDict(sorted(distances_dict.items(), key = itemgetter(1)))
        best_distance_this_generation = list(ordered_dict.items())[0][1]
        index_best_distance_this_generation = list(ordered_dict.items())[0][0]
        #print(index_best_distance_this_generation)
        #print(best_distance_this_generation)
        if best_distance_this_generation < bestDistance:
            bestDistance = best_distance_this_generation
            bestRoute = initial_population_list[index_best_distance_this_generation]
        
        
        
        # Generating the temporary list of routes which next generation will be based on
        # Making crossover and mutation
        next_population_temp = copy.copy(initial_population_list)
        #print(next_population_temp)
        for index, _ in enumerate(next_population_temp):
            next_population_temp[index] = populationGenerator.mutate(next_population_temp[index])
        
        initial_population_list = next_population_temp
        if generation % 50 == 0:
            print(bestDistance)
            print(bestRoute)

    
        
    #     next_population_temp = random.choices(initial_population_list, distances_dict.values(), k = 10)

    #     # making crossover and mutation
    #     for _ in range(50):
    #         parentRoute1 = random.choice(next_population_temp)
    #         parentRoute2 = random.choice(next_population_temp)
    #         childRoute = populationGenerator.crossover(parentRoute1, parentRoute2)
    #         # childRoute = populationGenerator.mutate(childRoute)
    #         next_population_list.append(childRoute)
        

    #     initial_population_list = next_population_list
    # print(bestDistance, best_route)




geneticAlgorithm(numberOfGenerations = 1000, populationSize = 100)



