import random

TARGET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def estimate_solution(target, solution):
    return sum(abs(x - y) for (x, y) in zip(target, solution))


def generate_random_solution(target):
    return [random.randint(0, 9) for _ in range(len(target))]


solution = generate_random_solution(TARGET)
print(solution)


while True:
    if estimate_solution(TARGET, solution) == 0:
        print(f"Best solution: {solution}")
        break
    print(f"Current solution: {solution}")
    solution = generate_random_solution(TARGET)
