l, r = map(int, input().split())  
if(l+r != 0 ):
    if l == r:
        print("Even", l * 2)
    else:
        if r > l:
            print("Odd", r * 2)
        else:
            print("Odd", l * 2)
else:
    print("Not a moose")
