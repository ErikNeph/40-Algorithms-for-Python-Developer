import random
import matplotlib.pyplot as plt
from itertools import permutations
from time import perf_counter
from collections import Counter


all_tours = permutations


def distance_tour(a_tour):
    return sum(distance_points(a_tour[i - 1], a_tour[i]) for i in range(len(a_tour)))


a_city = complex


def distance_points(first, second):
    return abs(first - second)


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300
    random.seed(number_of_cities, seed)
    return frozenset(
        a_city(random.randint(1, width), random.randint(1, height))
        for c in range(number_of_cities)
    )


def brute_force(cities):
    return shortest_tour(all_tours(cities))


def shortest_tour(tours):
    return min(tours, key=distance_tour)


def visualize_tour(tour, style="bo-"):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
        start = tour[0:1]
        visualize_segment(tour + start, style)
        visualize_segment(start, "rD")


def visualize_segment(segment, style="bo-"):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis("scaled")
    plt.axis("off")


def X(city):
    "X axis"
    return city.real


def Y(city):
    "Y axis"
    return city.imag


def tsp(algorithm, cities):
    t_0 = perf_counter()
    tour = algorithm(cities)
    t_1 = perf_counter()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print(
        "{}: {} cities => tour.length {:.0f} (in {:.3f} sec)".format(
            name(algorithm), len(tour), distance_tour(tour), t_1 - t_0
        )
    )


def name(algorithm):
    return algorithm.__name__.replace("__tsp", "")


tsp(brute_force, generate_cities(10))
