def count_words(sentence):
    return len(sentence.split())

def main():
    sentence = "This is a test sentence."
    print("Word count is:", count_words(sentence))

if __name__ == "__main__":
    main()
