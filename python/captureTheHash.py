import os
import colorama
from hashIt import hash_file


colorama.init(autoreset=True)
hash_file_check = os.path.exists('testFiles/stored_hashes')
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

if hash_file_check:
    # Check new file against any stored hashes
    with open('C:/Users/cyber/PycharmProjects/fimsuite/testFiles/check_stored_hashes', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

else:
    # Overwrite any existing file, or create new one
    with open('C:/Users/cyber/PycharmProjects/fimsuite/testFiles/stored_hashes', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

# compare lists for match
for f, h in zip(files_to_hash, each_hash):
    print(f'[+] {colorama.Fore.CYAN}File: {f} | {colorama.Fore.MAGENTA}Hash: {h}')
