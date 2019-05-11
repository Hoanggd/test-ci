number = [128, 2, 4, 16, 2, 128, 64, 4, 7, 4, 64]

number_dict= {}
for index, value in enumerate(number):
    for index_2, value_2 in enumerate(number):
        if index != index_2 and value*value_2 == 256:
            if value < value_2:
                number_dict[value] = value_2
for key, value in number_dict.items():
    print("{0} va {1} tai vi tri {2} va {3}".format(key, value, number.index(key) + 1, number.index(value)+ 1))