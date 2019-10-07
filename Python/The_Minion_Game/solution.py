"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
def minion_game(string):
    string_len = len(string)
    vowels = ('A', 'E', 'I', 'O', 'U')

    stuart = 0
    kevin = 0

    for i in range(string_len):
        if string[i] in vowels:
            kevin += string_len - i
        else:
            stuart += string_len - i

    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif stuart > kevin:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)