import os
import colorama
from hashIt import hash_file


colorama.init(autoreset=True)
print(f'[*]{colorama.Fore.GREEN} Run this program in the directory to be monitored')
print(f'[*]{colorama.Fore.GREEN} First run will hash any new file(s). Subsequent runs will verify changes')
input(f'[!] Press Enter to continue')


def capture_files() -> list:
    # Locate specified file extension, return file list for hashing
    files_in_dir = []

    # Files to monitor
    for f in os.listdir():
        if f.endswith('.txt'):
            files_in_dir.append(f)
    return files_in_dir


files_to_hash = capture_files()
each_hash = [hash_file(f) for f in files_to_hash]

# write hashes to a file line by line. Each run overwrites previous file
lines = each_hash
with open('store_hashes.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# open store_hashes.txt, and match against new_hashes.txt for changes

for f, h in zip(files_to_hash, each_hash):
    print(f'[+] {colorama.Fore.CYAN}File: {f} | {colorama.Fore.MAGENTA}Hash: {h}')
