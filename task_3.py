def update(id, meaning):
    array = [
            {'id': 1, 'state': True},
            {'id': 2, 'state': True},
            {'id': 8, 'state': False}
    ]

    for i in range(len(array)):
        get_id = array[i].get('id')
        if get_id == id:
            array[i] = {'id': id, 'state': meaning}
    return array


f = update(2, False)
print(f)
