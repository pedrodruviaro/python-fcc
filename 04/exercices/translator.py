# vowels -> g
    # cat -> cgt

vowels = ['a', 'e', 'i', 'o', 'u']

def translate_to_giraffe_lang(phrase):
    translation = ''

    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter

    return translation


print(translate_to_giraffe_lang('cat'))
print(translate_to_giraffe_lang('cAt'))
print(translate_to_giraffe_lang('owned'))
print(translate_to_giraffe_lang('Owned'))
print(translate_to_giraffe_lang('giraffe'))

print(translate_to_giraffe_lang(input("Enter a phrase: ")))