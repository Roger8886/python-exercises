#讓使用者輸入兩個數字 代表一個區間
a = int(input("Input a number: "))
b = int(input("Input another number: "))

# 找出符合 Self-Dividing Number的所有數
def SelfDividingNumber(left, right):
    res = []
    for n in range(left, right+1):
        if '0' in str(n):
            continue
        for i in str(n):
            if n % int(i) != 0:
                break
        else:
            res.append(n)
    return res
c = SelfDividingNumber(a, b)

#將差距最大的Self-Dividing Number 兩數印出
def gap(l):
    temp = 0
    for i in range(len(l)-1):
        dist = l[i+1] - l[i]
        if dist > temp:
            temp = dist
            res = [l[i], l[i+1]]
            continue
    return res
d = gap(c)
print(d)
