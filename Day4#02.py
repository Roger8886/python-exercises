s = 'Here are UPPERCASE and lowercase chars.'
dict = {}
for index,i in enumerate(s):
    if i not in dict:
        dict[i] = [index+1]
    else:
        dict[i].append(index+1)
print(dict)
