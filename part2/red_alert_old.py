from random import seed, randint
from time import time

# Generates a list of two tuples where the first value on every instance is lower than the second
def generate_dual_list(length):
    seed(time())
    output = []
    
    for i in range(length):

        a = randint(0, 1000 - len(output))        # The first instance in the tuple is randomized so that there cant 
                                                # be a shortage of numbers over a for b to inhabit, making it 
                                                # imposible to asign a value to b
        
        if not len(output):
            output.append((a, randint(a, 1000)))
        
        else:
            b = None
            
            while b is None:
                b = randint(a, 1000)              # Randomizes a value for b from a upwards, checks so that b is 
                                                # distinct from the already generated b values and apends it 
                                                # if it is
            
                for instance in output:
                    if instance[1] == b:
                        b = None
                        break
            
            output.append((a, b))

    return output


# An implementation of Mergesort where the maximum value of instance[1] - instance[0] is returned at every recursion
def red_alert(tiberium, start=0, end=None):
    if end is None:                                         # Generates the end for the first recursion call
        end = len(tiberium) 
    
    if end - start < 1:
        print("Something sent in an empty list")            # Some error handeling
        return -1;

    elif end - start == 1:                                  # Basecase, returns instance[1] - instance[0]
        print("Start: %d, End: %d, Result: %d" % (start, end, tiberium[start][1] - tiberium[start][0]))
        return tiberium[start][1] - tiberium[start][0]

    else:                                                   # Spits the list in half 

        return max(red_alert(tiberium, start, start + ((end - start) // 2)), red_alert(tiberium, start + ((end - start) // 2), end))

def kanes_wrath(tiberium):
    
    max_val = -1
    operationcounter = 0

    for instance in tiberium:
        if instance[1] > max_val:
            max_val = max(max_val, instance[1] - instance[0])
            operationcounter += 1
        operationcounter += 1

    return {"Max val": max_val, "Operationcounter": operationcounter}


def test():
    lst = generate_dual_list(1000)
    print(lst)

    print(kanes_wrath(lst))


test()
