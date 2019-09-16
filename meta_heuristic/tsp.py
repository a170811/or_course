import random
import math
from sys import argv
import time

with open('./gr17_d.txt', 'r') as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split())))

assert len(matrix)>0

def path_len(route):
    total = 0
    for line in range(len(route) - 1):
        total += matrix[route[line]][route[line + 1]]
    return total

def new_route(route):
    i, j = random.sample(range(1, len(route) - 1), 2)
    tmp_route = route[:]
    tmp_route[i], tmp_route[j] = tmp_route[j], tmp_route[i]
    return tmp_route, path_len(tmp_route)

def sa_method(temperature = 100, rate = 0.96, max_iter = 5000):

    route = [i for i in range(len(matrix[0]))]
    route.append(route[0])
    curr_len = path_len(route)

    __save = 0
    __update = 0
    __drop = 0

    for i in range(max_iter):
        tmp_route, tmp_len = new_route(route)
        delta = tmp_len - curr_len

        if delta >= 0:
            if random.random() > math.exp(-float(delta)/temperature):
                __drop += 1
                continue
            else:
                __save += 1

        __update += 1
        route = tmp_route
        curr_len = tmp_len
        temperature *= rate


    return curr_len, route, (__save, __update, __drop)

if '__main__' == __name__:
    print('This program implements Simulated Annealing method,')
    print('to solve Traveling Salesman Problem\n')
    t1 = time.time()
    if len(argv) < 4:
        print('----default arguments----')
        print('***you can also use')
        print('python3 tsp.py [temperature] [annealing rate] [max iterating time]')
        print('to set arguments***\n')

        print('temperature : {}'.format(100))
        print('annealing rate : {}'.format(0.96))
        print('maximum iterate time : {}'.format(5000))

        print('\nresult(shortest path): {}\nroute: {}'.format(*(sa_method()[:2])))
    else:
        argv[1:4] = [int(argv[1]), float(argv[2]), int(argv[3])]
        print('temperature : {}'.format(argv[1]))
        print('annealing rate : {}'.format(argv[2]))
        print('maximum iterate time : {}'.format(argv[3]))

        print('\nresult(shortest path): {}\nroute: {}'.format(*(sa_method(argv[1],
            argv[2], argv[3])[:2])))
    print('cost {:.2} seconds'.format(time.time() - t1))
