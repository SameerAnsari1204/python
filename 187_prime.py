n = int(input("Enter no:\n"))
flag = 0
if n==1:
    print("Not Prime\n")
for i in range(2,int((n/2)+1)):
    if(n%i==0):
        flag = flag + 1
if(flag>=1):
    print("Not Prime")
else:
    print("Prime no")