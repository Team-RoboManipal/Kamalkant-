def insert(x):
    l.append(x)

def delete(x):
    l.pop(x)

def traverse():
    for i in l:
        print(i)

l=[]
insert(1)
insert(2)
insert(3)
delete(2)
traverse()