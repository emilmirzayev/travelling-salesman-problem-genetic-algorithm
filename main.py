import math
import random
import itertools
import copy
from collections import OrderedDict
from operator import itemgetter
from tsp import *


number_of_cities = int(input("Please, enter the number of cities to generate: "))
number_of_generations = int(input("Please, enter the number of generations: "))
population_size = int(input("Please, enter the population size: "))


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
    # print(initial_population_list, "this is initial population")
    bestDistance = math.inf
    bestRoute = None


    


    for generation in range(numberOfGenerations):

        #print(initial_population_list)
        
        next_population_temp = list()
        next_population_list = list()
        populationGenerator = Population()
        
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
        
        

        if best_distance_this_generation < bestDistance:
            bestDistance = best_distance_this_generation
            bestRoute = initial_population_list[index_best_distance_this_generation]
        

        
        
        
        # Generating the temporary list of routes which next generation will be based on
        # Making crossover and mutation
        next_population_temp = random.choices(initial_population_list, distances_dict.values(), k = 20)
        
        
        # Generating the half of the next population from previous population's crossover
        for _ in range(len(initial_population_list)//2):
            _parent1, _parent2 = random.sample(next_population_temp, 2)
            childRoute = populationGenerator.crossover(_parent1, _parent2)
            next_population_list.append(childRoute)
        
        # generating the rest half of the population randomly
        for _ in range(len(initial_population_list)//2):
            next_population_list.append(populationGenerator.generate(city_id_list))
        
        # checking the length of the populations for match
        assert len(next_population_list) == len(initial_population_list), "The length of the populations do not match!"
        
        
        # Mutating the population
        for index, _ in enumerate(next_population_list):
            next_population_list[index] = populationGenerator.mutate(next_population_list[index])
        
        initial_population_list = next_population_list
        if generation % 50 == 0:
            # after every 50 generations print the score
            print("Best distance for the generation {} is {}".format(generation ,bestDistance))
            print("Best route so far {}".format(bestRoute))
        




if __name__ == "__main__":
    geneticAlgorithm(numberOfGenerations = number_of_generations, populationSize = population_size)




