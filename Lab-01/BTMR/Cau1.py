from itertools import permutations

def print_permutations(lst):
    perms = permutations(lst)
    for perm in perms:
        print(perm)

lst = [1, 2, 3]
print_permutations(lst)
