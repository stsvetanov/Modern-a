from Experts.Lecture_67_Meta.utils import generate_population, estimate_population, select_population, estimate_solution
from Experts.Lecture_67_Meta.local_search import local_search

import time
start_time = time.time()


def abc_search(target, number_of_iterations=50, population_size=100):
    scouts = int(population_size/10)
    workers = population_size - scouts
    best_solution = None
    global_solutions = generate_population(target, scouts)

    for iterations_counter in range(number_of_iterations):
        estimated_global_solutions = estimate_population(global_solutions[:scouts], target)
        selected_global_solutions = select_population(estimated_global_solutions)
        local_solutions = workers_activity(target, workers, selected_global_solutions[:15])
        estimated_local_solutions = estimate_population(local_solutions, target)
        selected_local_solutions = select_population(estimated_local_solutions)
        elite_solutions = selected_local_solutions[:10]
        best_solution_in_generation = selected_local_solutions[0]
        best_solution_in_generation_score = estimate_solution(best_solution_in_generation, target)

        print("Best solution in iter {} is {} -> {}".format(iterations_counter, best_solution_in_generation, best_solution_in_generation_score))

        if best_solution is None:
            best_solution = best_solution_in_generation

        if estimate_solution(best_solution_in_generation, target) < estimate_solution(best_solution, target):
            best_solution = best_solution_in_generation

        if estimate_solution(best_solution, target) == 0:
            break

        global_solutions = elite_solutions

    print("Best solution: {} -> {}".format(best_solution, estimate_solution(best_solution, target)))
    print("--- %s seconds ---" % (time.time() - start_time))


def workers_activity(target, workers, selected_global_solutions):
    solutions = []
    counter = len(selected_global_solutions)
    for s in selected_global_solutions:
        for _ in range(workers):
            solutions.append(local_search(target, counter, s))
        counter = int(counter/3)
        if counter < 2:
            break
    return solutions

