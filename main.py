import os
# from downloader import download_file
from installer import flash_iso

DIR = "/dev"
ROOT_DIR = os.path.abspath(os.curdir)
ISO = "Fedora-Workstation-Live-x86_64-31-1.9.iso"
ISO_DIR = ROOT_DIR + "/" + ISO


# flash_iso(ISO_DIR, DIR)
