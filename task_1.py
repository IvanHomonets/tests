example_list = [1, 2, 3, 4, 5, 6]


# Now max complexity is O(n) because it depends on the length of list
def my_reverse(some_list):
    for i in range(len(some_list)//2):
        print(i)
        start_point = i
        end = -i-1
        some_list[start_point], some_list[end] = some_list[end], some_list[start_point]
    return some_list


f = my_reverse(example_list)
print(f)
