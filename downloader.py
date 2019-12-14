import requests
import os
import urls
from os import listdir


def verify_checksum(iso_type, iso_url):
    checksums = urls.Checksums.keys()
    if iso_type in checksums:
        print("Verifying checksum...")
        cheksum_url = urls.Checksums[iso_type]
        cheksum_name = cheksum_url.split('/')[-1]
        download(cheksum_url, cheksum_name)
        os.system("curl https://getfedora.org/static/fedora.gpg | gpg --import")
        check_checksum = os.popen("sha256sum -c *-CHECKSUM").read()
        iso_filename = iso_url.split('/')[-1]
        valid_checksum = iso_filename + ": OK"
        if valid_checksum in check_checksum:
            return True
        else:
            return False
    else:
        return False


def download(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            print("Downloading %s" % filename)
            total_length = r.headers.get('content-length')
            if total_length is None:  # no content length header
                f.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        dl += len(chunk)
                        f.write(chunk)
                        done = int(50 * dl / total_length)
                        print("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))


def download_iso(url):
    local_filename = url.split('/')[-1]
    root_dir = os.path.abspath(os.curdir)
    files = [f for f in listdir(root_dir)]
    while True:
        if local_filename in files:
            rerun = input("ISO I'm about to download already exists. Do you want to re-download it? (Y/n): ")
            if rerun == "y":
                break
            elif rerun == "n":
                return local_filename
        else:
            break
    download(url, local_filename)

    return local_filename

