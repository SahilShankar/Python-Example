secret_word = "Hello World"
guess = ""
tries = 0;
loose = False

while secret_word != guess and not loose :
    if tries >= 3:
        loose = True;
    else:
        guess = input("Enter Guess: ")
        tries += 1

if not loose:
    print("You win")
else:
    print("YOU LOOSE")
