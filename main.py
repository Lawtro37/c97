
year = int(input("year to test: "))

if(year % 4 == 0) :
    print(year,"is a leap year")
else :
    print(year,"is not leap year")

cm = int(input("cm:"))

print("inches:", cm*0.394)
print("feat:", cm*0.0328)
