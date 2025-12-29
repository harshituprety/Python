x = [1,3,5,7]
print(x)
x.append(9)
print(x)
x.sort(reverse=True)
print(x.index(3))
print(x.count(5))
a=x.copy()
print(a)
x.insert(1,13)
print(x)
c = [121,131,111]
d = x+c
x.extend(c)
print(x)
print(d)
