n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
    #print(num)
num = [x for x in num if x%2!=0]
print(num)