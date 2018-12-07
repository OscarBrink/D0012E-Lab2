from random import randint, choice, random

nops = 0

def max_div(lst, start=0, end=None):
    global nops
    nops = 0

    if end is None:
        end = len(lst) - 1

    size = end - start + 1

    if size <= 1:
        raise ValueError

    # Base Case 1
    elif size == 2:
        if lst[start] < lst[end]:
            return (lst[start], lst[end], (lst[start], lst[end], lst[end] / lst[start]))
        else: 
            return (lst[end], lst[start], (lst[start], lst[end], lst[end] / lst[start]))

    # Base Case 2
    elif size == 3:
        mid = start + 1
        min_val = lst[start]
        max_val = lst[start]
        for num in lst[mid], lst[end]:
            if num < min_val: min_val = num
            if num > max_val: max_val = num

        # Select which division to pick from list [a, b, c]
        if lst[start] <= lst[mid] <= lst[end]:      # a <= b <= c : c / a
            return (min_val, max_val, (lst[start], lst[end], lst[end] / lst[start]))
        elif lst[start] > lst[mid] <= lst[end]:     # a > b <= c  : c / b
            return (min_val, max_val, (lst[mid], lst[end], lst[end] / lst[mid]))
        else:                                       # b > c       : b / a
            return (min_val, max_val, (lst[start], lst[mid], lst[mid] / lst[start]))
        

    split = start + (size // 2) - 1

    # Recursion
    lower = max_div(lst, start, split)
    upper = max_div(lst, split + 1, end)


    # Determine new max and min values
    min_val = lower[0]
    max_val = lower[0]
    for num in (lower[1], upper[0], upper[1]):
        if num < min_val: min_val = num
        if num > max_val: max_val = num

    # Determine best fraction
    best_div = lower[2] if lower[2][2] >= upper[2][2] else upper[2]
    new_div = (lower[0], upper[1], upper[1] / lower[0])
    if new_div[2] > best_div[2]:
        best_div = new_div

    return (min_val, max_val, best_div)


def slow_max(lst):
    max_val = (-1, -1, -1)
    best_divs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] / lst[i] > max_val[2]:
                best_divs = []
                max_val = (lst[i], lst[j], lst[j] / lst[i])
                best_divs.append(max_val)
            elif lst[j] / lst[i] == max_val[2]:
                best_divs.append((lst[i], lst[j], lst[j] / lst[i]))
    return best_divs


def min_max(lst, start=0, end=None):
    global nops

    if end is None:
        end = len(lst) - 1

    size = end - start

    if size < 1:
        raise ValueError
    elif size < 2:
        nops += 1
        return (lst[start], lst[end]) if lst[start] < lst[end] else (lst[end], lst[start])

    split = start + size // 2

    nops += 1
    lower = min_max(lst, start, split)
    upper = min_max(lst, split, end)

    print(lst[start:end+1])
    print("lower:", lower)
    print("upper:", upper)

    return (
           lower[0] if lower[0] <= upper[0] else upper[0],
           lower[1] if lower[1] >= upper[1] else upper[1]
    )


def generate_list(size):
#    lst = []
#    for i in range(size):
#        r = list(range(1, size * 10))
#        lst.append(r.pop(choice(list(range(len(r))))))
#    return lst
   return [randint(1, size * 10) * random() for i in range(size)]


lst = []
for i in range(0, 8):
    newint = randint(1, 100)
    while newint in lst:
        newint = randint(1,100)
    lst.append(newint)


failures = 0
try:
    for i in range(20):
        size = randint(2, 1025)
        pr_str = str(i) + " " + str(size)
        l = generate_list(size)
        print(pr_str, "cac ", end=" ")
        cac = max_div(l)
        print(pr_str, "slow", end=" ")
        slow = slow_max(l)
        verified = False
        for m in slow:
            if cac[2][0] == m[0] and cac[2][1] == m[1]:
                verified = True
                break
        if not verified:
            failures += 1
            print("FAIL:")
            print(cac[-1])
            print(cac)
            print(*slow)
            print()

            input()
        else:
            print("SUCCESS" + " "*8, end="\r")
except KeyboardInterrupt:
    print("interrupted")

if failures > 0:
    print(failures, "failed.")


lst = generate_list(8)
print(lst)
print(max_div(lst))
print(slow_max(lst))
#m_m = min_max(lst)
#print(lst)
#print(sorted(lst))
#print(m_m)
#print("lst:", len(lst), "nops:",  nops)

