import os

dir = "/dev/sdb"
ROOT_DIR = os.path.abspath(os.curdir)
iso = "Fedora-Workstation-Live-x86_64-31-1.9.iso"

iso_dir = ROOT_DIR + "/" + iso

command = 'dd if={} of={} bs=2048'.format(iso_dir, dir)


os.system(command)


