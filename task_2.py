example_str = "agcdcgia"
print(example_str)


def filter_1(some_str):
    filter_letters = []
    for letter in some_str:
        if some_str.count(letter) > 1 and letter not in filter_letters:
            filter_letters.append(letter)
    filter_str = ''.join(filter_letters)
    return filter_str

f = filter_1(example_str)
print(f) # print 'agc'
