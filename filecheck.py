from os import listdir
# from os.path import isfile, join
# from main import DIR

onlyfiles = [f for f in listdir("/dev")]


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def filter_sd(in_list):
    if "sd" in in_list:
        if has_numbers(in_list) is True:
            return False
        else:
            return True
    else:
        return False


filtered_list = filter(filter_sd, onlyfiles)


print(list(filtered_list))