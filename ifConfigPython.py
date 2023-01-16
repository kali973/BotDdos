import os
import subprocess
from pathlib import Path


def get_ifconfig():
    output = subprocess.run(["ifconfig"], capture_output=True)
    return output.stdout.decode()

def existIpFile():
    path_to_file = 'ip.txt'
    path = Path(path_to_file)
    if path.is_file():
        os.remove(path_to_file)
    else:
        file = open("ip.txt", "w")
        file.close()
def main():
    ifconfig_output = get_ifconfig()
    print(ifconfig_output)
    existIpFile()
    input("Press Enter to continue...")


if __name__ == "__main__":
    main()
