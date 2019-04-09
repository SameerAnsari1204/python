n=int(input())
if (n%3==0 and n%5==0):
    print(str(n)+"fizzBuzz")
else:
    if(n%3==0):
        print(str(n)+"Fizz")
    else:
        if (n%5==0):
            print(str(n)+"Buzz")
        else:
            print(n)
    