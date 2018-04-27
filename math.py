'''
duckdo
Jen Yu and Alessandro Cartegni
2018-04-27
K #16: Ready, Set, Math!
Period 7 SoftDev 
'''

def intersection(a, b):
    if len(a) > len(b):
        return intersection(b,a)
    return [x for x in a if x in b]

def union(a, b):
    i = intersection(a, b)
    return [x for x in a+b if x not in i] + i

def set_diff(a, b):
    return [x for x in a if x not in b]

def sym_diff(a, b):
    return set_diff(a, b) + set_diff(b, a)

def cartesian(a, b):
    return [[x, y] for x in a for y in b]

a = [1, 2, 3, 4]
b = [2, 4, 6, 8]


print intersection(a, b) #[2, 4]
print union(a, b) #[1, 2, 3, 4, 6, 8] (may be in different order)
print set_diff(a, b) #[1, 3]
print sym_diff(a, b) #[1, 3, 6, 8]
print cartesian(a, b) #set of all possible combinations

a = [1, 2, 3]
b = [2, 3, 1, 2, 3, 1]
print intersection(a, b) #[1, 2, 3]
