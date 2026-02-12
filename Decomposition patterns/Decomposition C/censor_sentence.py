def censor_sentence(sentence, target_words):
    words = sentence.split(" ")
    result = []

    for word in words:
        if word in target_words:
            censored = change_to_star(word)
            result.append(censored)
        else:
            result.append(word)

    return " ".join(result)


def change_to_star(word):
    stars = ""
    for _ in word:
        stars += "*"
    return stars


print(censor_sentence('where the heck is my celery', ['heck', 'celery']))
print(censor_sentence('why you little sweetheart', ['sweetheart', 'salad']))
