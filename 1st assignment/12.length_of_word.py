inp="Python is fun"
inp_words=inp.split()
length=[]

for i in inp_words:
    length.append(len(i))

print(length)