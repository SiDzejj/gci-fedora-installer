import requests
import os

workstation_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso"

server_x86_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/31/Server/x86_64/iso/Fedora-Server-dvd-x86_64-31-1.9.iso"
server_aarch64_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/31/Server/aarch64/iso/Fedora-Server-dvd-aarch64-31-1.9.iso"


def download_file(url):
    local_filename = url.split('/')[-1]
    clear = lambda: os.system('clear')
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            print("Downloading %s" % local_filename)
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
                        print("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                        clear()

    return local_filename


download_file(workstation_url)
