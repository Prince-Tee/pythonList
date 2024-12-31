#step 1: create an emptylist
mylist = []

#2: Append elements 10, 20, 30, 40 to list

mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)

#3: insert the value 15 at the second position(index 1)

mylist.insert(1, 15)

#4: extend the list with another list [50, 60, 70]
mylist.extend([50, 60, 70])

#5: remove the last element from the list
mylist.pop()

#6: Sort the list in ascending and descending order
mylist.sort(reverse=True)
mylist.sort()

#7 find and print the index of the value 30 in mylist

indexof30 = mylist.index(30)
print(f'the index value of 30 in my list is {indexof30}' )



print(mylist)
