# Variables

x = 5
y = 'Sam'

print('My name is %s and %s are friends' % ('Tharani', 456))
print(y)

thisset = {"apple", "cherry","banana"}

#x = thisset.pop()

for i in range(len(thisset)):
    print('------')
    x = thisset.pop()
    print(x) #removed item

print(thisset) #the set after removal

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}



print(x.symmetric_difference(y))