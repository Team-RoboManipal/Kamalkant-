s1="Listen"
s2="Silent"
s1=s1.upper()
s2=s2.upper()
s1_list=[]
s2_list=[]

for i in s1:
    s1_list.append(i)

for i in s2:
    s2_list.append(i)

s1_list.sort()
s2_list.sort()
if (s1_list==s2_list):
    print("its an anagram")
else:
    print("its not a anagram")

