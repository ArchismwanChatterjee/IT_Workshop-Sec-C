d1={"A":100,"B":200,"C":300}
d2={"D":400,"E":500,"F":600}
for i in d2.keys():
    d1[i]=d2[i]
print(d1)

#{'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500, 'F': 600}