import random

TARGET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
POPULATION_SIZE = 20
SCOUTS = 5
WORKERS = 50
LOCAL_SEARCH_ITER = 50


def generate_random_solution(target):
    return [random.randint(0, 9) for _ in range(len(target))]


def generate_population():
    population = [generate_random_solution(TARGET) for _ in range(POPULATION_SIZE)]
    return population


def generate_local_solution(solution):
    local_solution = [s for s in solution]
    num_low = 0
    num_len = len(solution)
    index = random.randint(num_low, num_len -1)
    local_solution.pop(index)
    local_solution.insert(index, random.randint(0, 9))
    return local_solution


def estimate_solution(target, solution):
    return sum(abs(x - y) for (x, y) in zip(target, solution))


def estimate_population(solutions):
    estimated_solutions = []
    for solution in solutions:
        estimated_solutions.append((estimate_solution(TARGET, solution), solution))
    return sorted(estimated_solutions)


def local_search(solution, iterations):
    for _ in range(iterations):
        if estimate_solution(TARGET, solution) == 0:
            print(f"Best solution: {solution}, iter: {iteration}")
            break
        next_solution = generate_local_solution(solution)
        iteration += 1
        if estimate_solution(next_solution, TARGET) < estimate_solution(solution, TARGET):
            solution = next_solution
            print(f"Current Solution: {solution}")


initial_population = generate_population()
estimated_population = estimate_population(initial_population)
selection = estimated_population[:4]




