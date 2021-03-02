def vars(a,b,c):
    if(a>=b):
        return True
    elif(a==b):
        return False
    elif(b>=c):
        return True
    elif(b<=c):
        return False
    elif(c>=a):
        return False
    else:
        return a
a="nothing brother";
answer=vars(1,2,3);
print(answer);