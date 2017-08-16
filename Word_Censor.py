def some_function(sentence):
    bad_words = ["lame"]

    lister = []
    for i in sentence:
        lister.append(i)

    new_sent = "".join(lister)

    for a in bad_words:
        if a in new_sent:
            new_sent = new_sent.replace(a, "*" * len(a))

    print(new_sent)


some_function("It's so lame that today is already sunday night. I mean... What happened to our weekend?")