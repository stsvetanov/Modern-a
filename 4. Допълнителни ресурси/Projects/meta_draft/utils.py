import random


def generate_random_solution(target):
    return [random.randint(0, 9) for _ in range(len(target))]


def generate_population(target, population_size):
    return [generate_random_solution(target) for _ in range(population_size)]


def estimate_solution(target, solution):
    return sum(abs(x - y) for (x, y) in zip(target, solution))


def selection(target, population: list) -> list:
    estimated_population = [(solution, estimate_solution(solution, target)) for solution in population]
    sorted_solutions = sorted(estimated_population, key=lambda el: el[1])
    return list((map(lambda x: x[0], sorted_solutions)))


def mutate_solution(solution):
    mutated_solution = [s for s in solution]
    num_low = 0
    num_len = len(solution)
    index = random.randint(num_low, num_len -1)
    mutated_solution.pop(index)
    mutated_solution.insert(index, random.randint(0, 9))
    return mutated_solution


def mutate_population(population):
    mutated_population = []
    for solution in population:
        mutated_population.append(mutate_solution(solution))
    return mutated_population


def crossover(selection):
    parent1 = selection[0]
    parent2 = selection[1]
    cross_point = int(len(parent1) / 2)
    offspring1 = parent1[:cross_point] + parent2[cross_point:]
    offspring2 = parent2[:cross_point] + parent1[cross_point:]
    return [offspring1, offspring2]











