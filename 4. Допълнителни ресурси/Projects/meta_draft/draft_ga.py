import random
from Other.Projects.meta_draft.utils import mutate_solution

TARGET = [0, 0, 0, 0]


def generate_random_solution(target):
    return [random.randint(0, 9) for _ in range(len(target))]


solution = generate_random_solution(TARGET)
print(solution)
mutate_solution(solution)
print(solution)



