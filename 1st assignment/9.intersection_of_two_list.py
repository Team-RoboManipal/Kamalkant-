l1=[1,2,3,4,5]
l2=[4,5,6,7]

intersection=[]

for i in l1:
    for j in l2:
        if (i==j):
            intersection.append(i)

print(intersection)