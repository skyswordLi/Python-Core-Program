def sorted_numbers(input_list):
    num_list = []
    for item in input_list:
        num_list.append(int(item))
    return sorted(num_list, reverse=True)


def sorted_numbers_dict_order(input_list):
    new_list = []
    for item in input_list:
        new_list.append(str(item))
    new_list = sorted(new_list, reverse=True)
    for i, x in enumerate(new_list):
        new_list[i] = x
    return new_list
