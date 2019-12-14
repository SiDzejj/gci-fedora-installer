from os import listdir
import os


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def filter_sdx(in_list):
    if "sd" in in_list:
        if has_numbers(in_list) is True:
            return False
        else:
            return True
    else:
        return False


def check_disk(chosen_disk):
    bus_check_command = "udevadm info --query=all --name={} | grep ID_BUS".format(chosen_disk)
    disk_bus = os.popen(bus_check_command).read()
    if "E: ID_BUS=usb" in disk_bus:
        bus_correct = True
    else:
        bus_correct = False
    return bus_correct


def get_drive_list():
    files = [f for f in listdir("/dev")]
    filtered_list = filter(filter_sdx, files)
    return list(filtered_list)
