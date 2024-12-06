def add_list(listnumbers):
    sum=0

    for i in listnumbers:
        sum=sum+i

    print(sum)

def product(productnums):

    prod=1

    for i in  productnums:
        prod=prod*i
    print(prod)
    
odd=[x for x in range(2,11) if x%2!=0 ]

add_list(odd)

even=[y for y in range(2,11) if y%2==0 ]

add_list(even)

product(odd)

product(even)



















