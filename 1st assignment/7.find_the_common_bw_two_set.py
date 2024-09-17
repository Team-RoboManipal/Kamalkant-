s1={1,2,3,4}
s2={3,4,5,6}
common=set()
for i in s1:
    for j in s2:
        if (i==j):
            common.add(i)

print(common)