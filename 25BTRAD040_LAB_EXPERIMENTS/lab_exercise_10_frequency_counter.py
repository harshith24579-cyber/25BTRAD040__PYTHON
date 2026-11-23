# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# LAB EXPERIMENT - 3
# Lab Exercise 10: Frequency Counter Using Dictionaries

def frequency_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\n--- WORD FREQUENCY ---")
    for word, count in frequency.items():
        print(word, ":", count)


if __name__ == "__main__":
    frequency_counter()
