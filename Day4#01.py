#回傳n+1
def add1(n):
    return (n+1)

#判斷n是否為質數
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

#map function
def map(F, L):
    list = []
    for i in L:
        list.append(F(i))
    return list

L = [1, 2, 3, 4, 5, 6]
F = add1
# L = [2, 3, 4, 5, 6, 6]
# F = isPrime

print(map(F, L))
