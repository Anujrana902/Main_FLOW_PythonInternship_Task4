def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

def main():
    sentence = "I love programming in Python"
    print("Longest word is:", longest_word(sentence))

if __name__ == "__main__":

    main()