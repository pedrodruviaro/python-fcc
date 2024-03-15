friends = ['Mary', 'John', 'Matthew']

print(friends)

friends[1] = 'John Doe'

print(friends)

print(friends.index("Mary")) # 0
# print(friends.index("Pedro")) # error

print(friends[-1]) # Matthew
print(friends[1:]) # ['John', 'Matthew']
print(friends[1:2]) # ['John']


# ------------ List Methods ------------
print("------- List Methods -------")

friends2 = ['Mary', 'John', 'Matthew']
nums = [4, 8, 15, 16, 23, 41, 1]

# friends2.extend(nums) # add 2 lists

friends2.append("Creed")
friends2.insert(0, 'Michael') # michael add to pos 0
friends2.insert(3, 'Pam') # pam add to pos 3

friends2.remove("Pam")

# friends2.clear() # []

friends2.pop() # remove last element

print(friends2.index('Michael')) # 0

print(friends2.count("Michael")) # 0 -> return the count of the item

friends2.sort()
nums.sort() # not return the list, only sort
print(nums)
print(friends2)
 
nums.reverse() # not return the list, only reverse
print(nums)

friends3 = friends2.copy() # copy the entire list

print(friends3)
