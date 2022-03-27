def ClimbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    s1, s2 = 1, 2
    for i in range(2, n):
        s1, s2 = s2, s1 + s2
    return s2

n = int(input("Please input a number: "))
d = ClimbingStairs(n)
print(d)
