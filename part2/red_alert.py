from random import seed, randint
from time import time

def generate_list(length):
    seed(time())
    return [randint(0, 5) for i in range(length)]


def calculate_b(lst):

    indexparser = generate_indexparser(lst)
    output = [None] * len(lst)

    last_index = None
    for index in indexparser:
        if index == indexparser[0]:
            output[index] = lst[index] + 1
        else:
            output[index] = max(output[last_index] + 1, lst[index] + 1)

        last_index = index
   
    print('a:', lst)
    print('a sorted:', [lst[indexparser[i]] for i in range(len(lst))])
    
    print('b:', output)
    print('b sorted:', [output[indexparser[i]] for i in range(len(output))])  

    return output

def generate_indexparser(lst):
    return sorted( list(range(len(lst))), key=lambda i : lst[i] )

    
calculate_b(generate_list(10))
