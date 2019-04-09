string=input("Enter string:")
count=0
if len(string)<2:
    print("String length should be 2 or more")
else:    
    for i in string:
        if string[0] == string[-1]:
            count=count+1
    print("Length of the string is:")
    print(count)