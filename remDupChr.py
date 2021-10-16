s = input("Enter your string: ")
s1 = " "
i = 0
for x in s:
    if(s.index(x)==i):
        s1+=x
    i+=1
print(s1)