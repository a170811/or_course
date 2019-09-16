from tsp import sa_method
import random
import time

i = 0
def target(temper, cool, max_iter, times):
    avg = 0
    save = 0
    update = 0
    for _ in range(times):
        dis, _, log = sa_method(temper, cool, max_iter)
        avg += dis
        save += log[0]
        update += log[1]
    avg /= times
    rate = save/update

    global i
    i += 1
    print('{}. temperature:{}, cooling rate:{}, max_iterations:{}'.format(i, temper, cool, max_iter))
    print('result = {}, rate = {:.2}'.format(avg, rate))
    print()

def test1():
    target(100, 0.95, 1000, 40) #1
    target(50, 0.95, 1000, 40) #2
    target(10, 0.95, 1000, 40) #3
    target(100, 0.95, 1000, 40) #4
    target(100, 0.97, 1000, 40) #5 **
    target(100, 0.99, 1000, 40) #6
    target(100, 0.95, 5000, 40) #7 **
    target(100, 0.97, 5000, 40) #8 **
    target(100, 0.99, 5000, 40) #9 **
    target(500, 0.95, 1000, 40) #10
    target(700, 0.95, 1000, 40) #11
    target(100, 0.7, 1000, 40) #12
    target(100, 0.8, 1000, 40) #13
    target(100, 0.9, 1000, 40) #14
    target(100, 0.99, 1000, 40) #15

if '__main__' == __name__:
    test1()
