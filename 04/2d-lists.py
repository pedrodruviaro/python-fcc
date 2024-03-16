number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

total = 0

for row in number_grid:
    for number in row:
        total += number    

print(total)