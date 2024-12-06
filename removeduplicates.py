numbers=[10,20,30,40,10,45,20,30]

#listnumbers=set(numbers)

uniques=[]

for i in numbers:

    if i not in uniques:
        uniques.append(i)


print("uniques list: ", uniques)
