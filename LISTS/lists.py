numbers = [1,2,3,4,5,6,7,8]
numbers.append(9) #Add a number on last index
numbers.insert(0, 10) #Adds on a specified index
numbers.remove(5) #Removes a number from an list
#numbers.clear() #This removes all items in our list
isExist = 10 in numbers #Checks if 10 exists in numbers and returns a boolean value
length = len(numbers) #Returns a number of items in list
print(numbers)
print(isExist)
print("Length of list: "+ str(length))