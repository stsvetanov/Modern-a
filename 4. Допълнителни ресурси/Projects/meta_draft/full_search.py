import itertools
from Other.Projects.meta_draft.utils import estimate_solution


def full_search(target):
    # solutions = itertools.permutations(range(10), len(target))
    count = 0

    solutions = itertools.product(range(10), repeat=len(target))
    solution = solutions.__next__()
    estimation = estimate_solution(target, solution)
    print(f"Initial Solution: {solution} -> {estimation}")

    for solution in solutions:
        new_solution = solution
        new_estimation = estimate_solution(target, new_solution)
        # print("Next Solution: {} -> {}".format(solution, estimation))
        if new_estimation < estimation:
            solution = new_solution
            estimation = new_estimation

        if estimation == 0:
            break

    print("Best Solution: {} -> {}".format(solution, estimation))
    print("Number of Iterations {}".format(count))