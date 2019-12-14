import os

root_dir = os.path.abspath(os.curdir)


def flash_iso(iso_dir, disk):
    disk_dir = "/dev/" + disk
    command = 'dd if={} of={} bs=4096'.format(iso_dir, disk_dir)
    print("Burning iso to " + disk)
    os.system(command)
