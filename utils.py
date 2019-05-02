
import io

def readauthfile(filename):
    tokens = []

    file = open(filename, "r", encoding="utf-8")

    for line in file:
        # cut the newline
        tokens.append(line[:-1])

    return tokens
