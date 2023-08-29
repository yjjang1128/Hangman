import random
words = ['dog', 'chicken', 'mouse']

def game_start():
    # Choice a random word from 'words'.
    word = list(random.choice(words))
    answer = ['_'] * len(word)
    life = 6
    # Number of misspelled words.
    misspell = answer.count('_')

    # Loop that does not end until the 'word' is matched.
    while word != answer:
        # Input the word you guess.
        char = input("Input character >>> ")

        # Loop through the list and check if 'char' is equal.
        for i in range(len(word)):
            if word[i] == char:
                answer[i] = char
            # Guess word at once.
            elif "".join(word) == char:
                return print("Correct! The answer was \"{}\"!".format("".join(word)))
            else:
                continue
        
        # Compare present 'answer' and past 'answer' to change 'life'.
        if misspell == answer.count('_'):
            life -= 1
            # Condition of gameover.
            if life == 0:
                return print("Game Over")
            print("That character does not exist in the word.")
        else:
            misspell = answer.count('_')


        # Show current status.
        print(" ".join(answer), "       Life: {}".format(life))
        print()

    # Show you are correct.
    return print("Correct! The answer was \"{}\"!".format("".join(word)))

game_start()
