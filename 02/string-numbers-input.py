print("Day\n02")
print("Day \"02\"")


print("------------- STRINGS -------------")

phrase = 'Giraffe'
print(phrase + ' is cool')

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper()) # False
print(phrase.upper().isupper()) # True

print(len(phrase)) # 7

print(phrase[1]) # i
print(phrase.index('G')) # 0
print(phrase.index('f')) # 4 (primeiro encontrado)
print(phrase.index('ffe')) # 4
# print(phrase.index('z')) # error

print(phrase.replace('G', 'g')) # giraffe
print(phrase.replace('ff', 'FF')) # GiraFFe


print("------------- NUMBERS -------------")

print(2)
print(3.14)
print(3 + 3 * 3)
print(10 / 5)
print(2 % 2)
print(3 % 2)


print(abs(-10.2)) # 10.2
print(pow(2, 3)) # 2 ** 3 == 8
print(max(4, 6)) # 6
print(min(10, 20, 1, 100)) # 1

print(round(3.2)) # 3
print(round(3.9)) # 4

from math import *

# floor e ceil vem de math
print(floor(3.7)) # 3
print(ceil(10.1)) # 10


print("------------- INPUT -------------")

# name = input("What's your name? ")
# age = input("Enter your age: ")
# print("Hello, " + name + "!")

# if(int(age) >= 18):
#     print("You can drive!")
# else:
#     print("You cannot drive!")

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)

# print(round(result))


