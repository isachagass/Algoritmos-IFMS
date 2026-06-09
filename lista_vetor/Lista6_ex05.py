a = []
b = []
for i in range(1,7):
    a.append((i*0.5))
    b.append(i*0.8)
print(a, "\n", b)
for i in range(len(a)):
    a[i] = a[i] + b[i]
print(a, "\n", b)
