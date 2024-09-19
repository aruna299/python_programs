print("enter 3 values:")
a=int(input())
b=int(input())
c=int(input())

print(a//b)
print(a/b)

if(a>b and a>c):
    print(f"{a} is big")
elif(b>a and b>c):
    print(f"{b} is big")
else:
    print(f"{c} is big")