def remove_duplicates(num_list):

    new_list = []
    for l in num_list:
        new_list.append(l)

    len_list = len(new_list)
    for n in range(len_list):
        for item in new_list:
            if (new_list.count(item) > 1):
                new_list.remove(item)

    print(new_list)

remove_duplicates([5,5,5,2,54,54,54,5])
