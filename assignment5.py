# Creating an empty list.
lst = []
print("Enter 5 elements in the list:")
# Iterating till the range.(5)
for i in range(0, 5):
    ele = int(input())
    # Adding the element.
    lst.append(ele) 
# Printing the entered list.(List created)   
print("Your Entered List:",lst)

#(1)Printing Sum of all the elements in the list.
print("\nSum of all the elements in the list =",sum(lst))

#(2)Printing the smallest number in the list.
print("\nThe smallest element(number) in the list =",min(lst))

#(3)Printing the largest number in the list.
print("\nThe largest element(number) in the list =",max(lst))

#(4)Display list in ascending order.
lst.sort()
print("\nlist in ascending order:",lst)

#(5)Display list in descending order.
lst.reverse()
print("\nlist in descending order:",lst)

#Sorted the list to bring the Orignal list back.
lst.sort()

#(6)Convert list into tuples.
T1=tuple(lst)
print("\nResulted Tuple after conversion:",T1)

#(7)Delete the list.
del lst
print("\nList after deletion:",lst)