import os


dir = "/dev/disk2"
ROOT_DIR = os.path.abspath(os.curdir)
iso = "Fedora-Workstation-Live-x86_64-31-1.9.iso"
iso_dir = ROOT_DIR + "/" + iso


def flash_iso(iso_dir, disk_dir):
    command = 'dd if={} of={} bs=4096'.format(iso_dir, disk_dir)
    # os.system(command)
    print("I have printed the command! \n {}").format(command)




