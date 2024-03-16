is_male = True
is_tall = False

if (is_male and is_tall):
    print("Is male and tall")

elif is_male and not(is_tall):
    print("Is male but not tall")

elif not(is_male) and is_tall:
    print("Is not male but are tall")

else:
    print("Is not male or tall!")