def maxnumber(num):
    max=num[0] #1

    for i in num: 
         if i>max:
            max=i
    return max

listnumbers=[70,67,89,100,34,68]

result=maxnumber(listnumbers)
print(result)

modifylist=[x for x in listnumbers if x!=result]

secondhighest=maxnumber(modifylist)

print(secondhighest)