import math
import random
import itertools
import copy

list_of_all_cities = list()
distances = list()
city_id_list = list()
mutationProbability = 0.7

class City:
    _ids = itertools.count(1)
    def __init__(self, x = None, y = None):
        """
        Creates a city with random X and Y coordinates within 100 x 100 conditional space
        
        """
        if x is not None:
            self.x = x
        else:
            self.x = random.randint(0, 100)
        if y is not None:
            self.y = y
        else:
            self.y = random.randint(0, 100)
        self.id = next(self._ids)

class Calculators:
    """
    Class of different calculator objects
    """
    
    def calculateEuclideanDistance(self, city1, city2):
        """
        Calculates the euclidean distance between the current and given cities with X and Y coordinates. 
        Calculated by finding a square root of the sum of the squares of coordinate differences:
            sqrt{sum_{i=1}^n (x_i-y_i)^2}
        More info at: https://en.wikipedia.org/wiki/Euclidean_distance
        """
        _xDiff = abs(city1["x"] - city2["x"])
        _yDiff = abs(city1["y"] - city2["y"])
        distance = math.sqrt(_xDiff**2 + _yDiff**2)
        return distance

    def calculateManhattanDistance(self, city1, city2):
        """
        Calculates the Manhattan distance between the current and given cities with X and Y coordinates.
        Calculated by finding the sum of absolute differences:
        More info at: https://en.wikipedia.org/wiki/Taxicab_geometry
        """
        _xDiff = abs(city1["x"] - city2["x"])
        _yDiff = abs(city1["y"] - city2["y"])
        distance = _xDiff + _yDiff
        return distance
    
    def calculateRoute(self, list_of_cities:list):
        """
        -----------EXPERIMENTAL----------
        Calculates the route distances between all cities and stores them in global "distances" object.
        The structure will be as follows:
            1. From (id)
            2. To   (id)
            3. Distance
        Sample output is:
            {1: {2: 101.21264743103995, 3: 71.19691004531025, 4: 13.341664064126334, 5: 49.92995093127971}}
        """
        for city_index, city in enumerate(list_of_cities):

            copy_list_of_cities = copy.copy(list_of_all_cities)
            copy_list_of_cities.pop(city_index)
            
            distance_dict = dict()
            distance_dict[city["id"]] = dict()
            for other_city in copy_list_of_cities:
                # print(other_city["id"])
                distance = self.calculateEuclideanDistance(city, other_city)
                distance_dict[city["id"]][other_city["id"]] = distance
            distances.append(distance_dict)
    
    def calculateFitness(self, distance):
        """"
        Calculate the fitness value based on distance
        """
        fitness = 1/distance
        return fitness



class Population:
    """
    Class of population generator objects
    """
    def generate(self, list_of_all_cities:list):
        """
        Generates a random route from the given list of cities. Will be a list of city ID numbers shuffled randomly: [1, 5, 6, 8, ..]
        List of cities is a list consisting of dictionaries in the following format:
            {"id":1, "x":00, "y":00}
        """
        
        route = copy.copy(city_id_list)
        random.shuffle(route)
        return route


    def crossover(self, parentRoute1:list, parentRoute2:list):
        """
        Generates a new route based on two parent routes via crossover. Child will have 50-50 genes from both parents
        """
        _divisionIndex = round(len(parentRoute1)/2)
        _childPart1 = parentRoute1[:_divisionIndex]
        _childPart2 = parentRoute2[_divisionIndex:]
        childRoute = _childPart1.extend(_childPart2)
        return childRoute

    def mutate(self, route:list):
        """
        Randomly mutates the route based on mutation probability. Mutation here means swapping two random elements of a list named "route"
        """
        if random.random() < mutationProbability:
            _randIndex1 = random.randrange(0, len(route))
            _randIndex2 = random.randrange(0, len(route))
            if _randIndex1 == _randIndex2: #if both indexes are the same, just skip it
                return route
            # if not, swap those two elements
            route[_randIndex1], route[_randIndex2] = route[_randIndex2], route[_randIndex1]
        return route

























