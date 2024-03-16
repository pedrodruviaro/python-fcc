
for letter in 'pedro':
    upper = letter.upper()
    print(upper)


friends = ['Jim', 'Karem', 'Kevin']

for friend in friends:
    print(friend)


for index in range(10): # 0 to 10 not including 10
    print(index)

for index in range(3, 10): # print bewteen 3 and 10 not including 10
    print(index)


for i in range(len(friends)):
    print(friends[i])


for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print(index)