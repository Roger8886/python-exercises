import itertools

str = input("Input a string: ")
s = sorted(set(str))
perm = list(itertools.permutations(s))
d = [''.join(row) for row in perm]
print(d)
