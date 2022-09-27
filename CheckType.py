def check_type_of_character(bien_so):
    count = 0
    for i in bien_so:
        if i.isnumeric() == True:
            count += 1
    return count