'''
generate_population
selection
mutation (local search)
repeat
'''
from Other.Projects.meta_draft.utils import generate_population, selection, crossover, estimate_solution, mutate_population

TARGET = [0, 0, 0, 7, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 9, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0]
NUMBER_OF_ITERATIONS = 500
POPULATION_SIZE = 1000


def ga_search(target, number_of_iterations, population_size):
    best_solution = None
    initial_population = generate_population(target, population_size)
    number_of_elite_solutions = int(population_size/20)

    for iteration in range(1, number_of_iterations + 1):

        selected_population = selection(target, initial_population)

        elite_solutions = selected_population[:number_of_elite_solutions]
        parents = elite_solutions[:2]
        offsprings = crossover(parents)
        selected_offsprings = selection(target, offsprings)
        best_solution_in_iteration = selected_offsprings[0]
        print("Best solution in iteration {} is {} -> {}".format(iteration,
                                                                 best_solution_in_iteration,
                                                                 estimate_solution(target, best_solution_in_iteration)))

        if estimate_solution(target, best_solution_in_iteration) < estimate_solution(target, best_solution):
            best_solution = best_solution_in_iteration

        if estimate_solution(target, best_solution) == 0:
            break

        elite_solutions.append(best_solution)
        mutated_population = mutate_population(elite_solutions)
        for solution in mutated_population:
            elite_solutions.append(solution)
        initial_population = elite_solutions

    print("Best solution: {} -> {}".format(best_solution, estimate_solution(target, best_solution)))


# ga_search(TARGET, NUMBER_OF_ITERATIONS, POPULATION_SIZE)