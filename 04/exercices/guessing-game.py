SECRET_WORD = 'giraffe'

guess = input("Make a guess: ")
tries = 0
max_tries = 3
out_of_guesses = False

while (guess != SECRET_WORD) and not(out_of_guesses):

    if tries < max_tries:
        print("You have ", max_tries - tries, ' tries left')
        guess = input("Make another guess: ")
        tries += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of guesses... you lose\nThe word is: " + SECRET_WORD)

else:
    print("You win!")

