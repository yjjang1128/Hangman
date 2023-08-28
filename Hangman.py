import random
words = ['dog', 'chicken', 'mouse']
def game_start():
    # Choice a random word from 'words'.
    word = list(random.choice(words))
    answer = ['_'] * len(word)

    # Loop that does not end until the 'word' is matched.
    while word != answer:
        # Input the word you guess.
        char = input("input character > ")

        # Loop through the list and check if 'char' is equal.
        for i in range(len(word)):
            if word[i] == char:
                answer[i] = char
            else:
                continue

        # Show current status.
        print(" ".join(answer))
        print()

    # Show you are correct.
    return print("Correct! The answer was \"{}\"!".format("".join(word)))

game_start()
