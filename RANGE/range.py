numbers = range(5) # We are going to have numbers from 0 to 4 since 5 is excluded
for number in numbers:
    print(number)

otherNumbers = range(5,10) # Here also we are going to begin from 5 to 9 since 10 is excluded
for number in otherNumbers:
    print(number)

otherNumbers2 = range(5,10,2) #Here it works like otherNumbers but we are skipping the 2 means skip two steps
for number in otherNumbers2:
    print(number)