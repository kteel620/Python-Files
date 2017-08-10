def some_function(sent):
    curse_words = ["lame"]

    lister = []
    for i in sent:
        lister.append(i)

    new_sent = "".join(lister)

    for a in curse_words:
        if a in new_sent:
            new_sent = new_sent.replace(a, "*" * len(a))

    print(new_sent)


some_function("It's so lame that today is sunday night. I mean... What happened to our weekend?")