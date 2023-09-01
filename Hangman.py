import random
words = ['dog', 'chicken', 'mouse']

def game_start():
    # Choice a random word from 'words'.
    word = list(random.choice(words))
    answer = ['_'] * len(word)
    life = 6
    # Number of misspelled words.
    misspell = answer.count('_')
    # List of current status.
    img = ["""
   LIFE: {}
   ________
   |      |
   O      |
  /|\\     |
  / \\     |
          |
         ---
   {}
    """,
    """
   LIFE: {}
   ________
   |      |
   O      |
  /|\\     |
  /       |
          |
         ---
   {}
    """,
    """
   LIFE: {}
   ________
   |      |
   O      |
  /|\\     |
          |
          |
         ---
   {}
    """,
    """
   LIFE: {}
   ________
   |      |
   O      |
  /|      |
          |
          |
         ---
   {}
    """,
    """
   LIFE: {}
   ________
   |      |
   O      |
   |      |
          |
          |
         ---
   {}
    """,
    """
   LIFE: {}
   ________
   |      |
   O      |
          |
          |
          |
         ---
   {}
    """]

    # Loop that does not end until the 'word' is matched.
    while word != answer:
        # Show current status.
        print(img[6 - life].format(life, " ".join(answer)))
        # Input the word you guess.
        char = input("Input character >>> ")

        # Guess word at once.
        if char == "".join(word):
            return print("""
   |￣￣￣￣￣￣￣￣￣￣￣￣|
           Correct!
        The answer was
         >>> {} <<<
   |＿＿＿＿＿＿＿＿＿＿＿＿|
    """.format("".join(word)))

        # Loop through the list and check if 'char' is equal.
        for i in range(len(word)):
            if word[i] == char:
                answer[i] = char
            else:
                continue

        # Compare present 'answer' and past 'answer' to change 'life'.
        if misspell == answer.count('_'):
            life -= 1
            # Condition of gameover.
            if life == 0:
                return print("""
   |￣￣￣￣￣￣￣￣￣|
        Game Over
   |＿＿＿＿＿＿＿＿＿|""")
            print()
            print("\"{}\" does not exist in the word.".format(char))
        else:
            misspell = answer.count('_')

    # Show you are correct.
    return print("""
   |￣￣￣￣￣￣￣￣￣￣￣￣|
           Correct!
        The answer was
        >>> {} <<<
   |＿＿＿＿＿＿＿＿＿＿＿＿|
    """.format("".join(answer)))

game_start()
