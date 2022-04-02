'''
Generate string that is closer to the target.
To calculate the distance between strings, compare each digits.
Example:
    Target = 1234
    Test = 2235
    Estimation: 1 + 0 + 0 + 1 = 2

    Implemented methods:
        random_search
        combinations
        ga_search
'''
from Other.Projects.meta_draft.random_search import random_search
from Other.Projects.meta_draft.full_search import full_search
from Other.Projects.meta_draft.local_search import local_search
from Other.Projects.meta_draft.ga_search import ga_search
from Other.Projects.meta_draft.abc_search import abc_search

TARGET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
NUMBER_OF_ITERATIONS = 500
POPULATION_SIZE = 1000


def main():
    user_input = int(input("Type: \n 1 for Random Search \n 2 for Full Search \n 3 for Local Search \n 4 for GA Search \n 5 for ABC Search  \n"))
    print('Target solution: {}'.format(TARGET))

    if user_input == 1:
        random_search(TARGET, NUMBER_OF_ITERATIONS)
    elif user_input == 2:
        full_search(TARGET)
    elif user_input == 3:
        local_search(TARGET, NUMBER_OF_ITERATIONS)
    elif user_input == 4:
        ga_search(TARGET, NUMBER_OF_ITERATIONS, POPULATION_SIZE)
    else:
        abc_search(TARGET, POPULATION_SIZE)


if __name__ == '__main__':
    main()




