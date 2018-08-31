
def rmv_vowel():
    letter = ["a", "e", "i", "o", "u"]
    new_letters = []
    sentense = input("Type out a sentence to be returned the same sentence without vowels. ")
    new_sent = []
    for g in sentense:
        if g in letter:
            new_sent.append("-")
        else:
            new_sent.append(g)
    print("".join(new_sent))



rmv_vowel()

