import os


def flash_iso(iso_dir, disk_dir):
    command = 'dd if={} of={} bs=4096'.format(iso_dir, disk_dir)
    # os.system(command)
    print(command)
