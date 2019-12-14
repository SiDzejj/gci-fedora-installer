import os
import urls
from downloader import download_iso, verify_checksum
from installer import flash_iso
from filecheck import filter_sdx, check_disk, get_drive_list


while True:
    server_or_workstation = input("What version of Fedora do you want? \n1. Workstation \n2. Server \nYour choice: ")
    if server_or_workstation == "1":
        print("Which DE of Fedora do you want? (Type name)")
        workstation_list = urls.Workstations.keys()
        for workstation in workstation_list:
            print(workstation)
        distro_choice = input("Your choice:")
        if distro_choice in workstation_list:
            url = urls.Workstations[distro_choice]
            file_name = download_iso(url)
            checksum = verify_checksum("workstation", url)
            break
    elif server_or_workstation == "2":
        print("Which server version do you want? (Type name)")
        server_list = urls.Servers.keys()
        for server in server_list:
            print(server)
        distro_choice = input("Your choice: ")
        if distro_choice in server_list:
            url = urls.Servers[distro_choice]
            file_name = download_iso(url)
            checksum = verify_checksum(distro_choice, url)
            break

while True:
    if checksum is False:
        choice = input("Checksum appears to be not correct. Should we continue? (Y/n)")
        if choice == "n":
            raise ValueError("Checksum isn't correct")
        else:
            break
    else:
        break

drive_list = get_drive_list()
root_dir = os.path.abspath(os.curdir)
iso_dir = root_dir + "/" + file_name

while True:
    print("What drive is your Fedora destination? Type anything to refresh.")
    for drive in drive_list:
        print(drive)
    drive_choice = input("Your choice: ")
    if drive_choice in drive_list:
        is_usb = check_disk(drive_choice)
        if is_usb is True:
            flash_iso(iso_dir, drive_choice)
            break
        else:
            print(drive_choice + " appears to not be an USB storage device. Try again.")