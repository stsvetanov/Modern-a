import random
import string
from functools import reduce


def generate_solution(solution_size):
    return "".join((random.choice(string.ascii_letters + " " + string.digits) for _ in range(solution_size)))


def generate_population(target, population_size):
    solution_size = len(target)
    return [generate_solution(solution_size) for _ in range(population_size)]


def estimate_solution(solution: str, target: str) -> int: # In the context of Genetic Algorithms, this function is called "fitness"
    value = 0
    for index, ch in enumerate(solution):
        value += abs(ord(ch) - ord(target[index]))
    return value

    # return sum(abs(ord(ch_solution) - ord(ch_target)) for ch_solution, ch_target in zip(solution, target))
    # m = map(lambda x: abs(ord(x[0]) - ord(x[1])), zip(solution, target))
    # return reduce(lambda x, y: x + y, m)


def estimate_population(population: list, target: str) -> dict:
    return {solution: estimate_solution(solution, target) for solution in population}


def mutate_population(elite_solutions):
    return [mutate_solution(elite_solution) for elite_solution in elite_solutions]


def mutate_solution(solution):
    solution_len = len(solution)
    index_to_replace = random.randint(0, solution_len - 1)
    element_to_replace = random.choice(string.ascii_letters + " " + string.digits)
    return solution[:index_to_replace] + element_to_replace + solution[index_to_replace + 1:]


def select_population(estimated_population: dict):
    return sorted(estimated_population, key=lambda x: estimated_population[x])
