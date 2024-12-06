def leapyear(year):
    return (year % 4==0 and year % 100 ! == 0) or (year % 400==0)
year=int(input("enter a year: "))


if leapyear(year):
    print(year,"is leap year")

else:
    print(year, "is not leap year")