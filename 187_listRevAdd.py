n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
    #print(list)
list1=list[:]
list.reverse()
l=[list[i]+list1[i] for i in range(len(list))]
print(l)    