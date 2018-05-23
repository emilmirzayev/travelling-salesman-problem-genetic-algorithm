import math
import random
import itertools
import copy
from collections import OrderedDict
from operator import itemgetter
from tsp import *



for _ in range(5):
    city = dict()
    a = City()
    city["id"] = a.id
    city["x"] = a.x
    city["y"] = a.y
    list_of_all_cities.append(city)
# calculate the distances of between every city and saves it into global distances variable


calc = Calculators()
calc.calculateRoute(list_of_all_cities)



for city in list_of_all_cities:
    city_id_list.append(city["id"])



print(list_of_all_cities)



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
    for _ in range(populationSize):
        initial_population_list.append(populationGenerator.generate(city_id_list))
    print(initial_population_list, "this is initial population")
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
            print(population)
            route_dist = 0
            #try:
            for pair in pairwise(population):
                print(pair)
                start, destination = pair
                route_dist += distances[start-1][start][destination]
                distances_dict[populationIndex] = route_dist
            # except: TypeError
            # pass
        # Now we sort this dictionary by values, and extract the best route with minimum distance, save it
        ordered_dict = OrderedDict(sorted(distances_dict.items(), key = itemgetter(1)))
        # idx = list(ordered_dict.keys())[0]
        best_distance_this_generation = list(ordered_dict.items())[0][1]
        if best_distance_this_generation < bestDistance:
            bestDistance = best_distance_this_generation
            best_route = initial_population_list[list(ordered_dict.items())[0][0]]


    
        # generating the temporary list of routes which next generation will be based on
        next_population_temp = random.choices(initial_population_list, distances_dict.values(), k = 10)

        # making crossover and mutation
        for _ in range(50):
            parentRoute1 = random.choice(next_population_temp)
            parentRoute2 = random.choice(next_population_temp)
            childRoute = populationGenerator.crossover(parentRoute1, parentRoute2)
            # childRoute = populationGenerator.mutate(childRoute)
            next_population_list.append(childRoute)
        

        initial_population_list = next_population_list
    print(best_distance, best_route)




geneticAlgorithm(numberOfGenerations = 50, populationSize = 50)




