from Other.Projects.meta_draft.utils import generate_population, selection


def abc_search(target, population_size):
    population = generate_population(target, population_size)
    selected_population = selection(target, population)

    print(selected_population)

