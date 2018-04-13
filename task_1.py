example_list = [1, 2, 3, 4, 5]

def my_reverse(some_list):
    reverse_list = []
    for i in some_list:
        reverse_list.insert(0, i)
    return reverse_list


f = my_reverse(example_list)
print(f)
