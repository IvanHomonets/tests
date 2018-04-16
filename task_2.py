example_str = "agcdcgia"
#ex = [1, 1, 3, 4, 6, 6]
print(example_str)


def filter_1(some_str):
    filter_str = ''
    for i in some_str:
        if i not in filter_str and some_str.count(i) > 1:
            filter_str += i
    return filter_str


f = filter_1(example_str)
print(f) # print 'agc'
