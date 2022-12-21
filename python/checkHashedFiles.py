import filecmp
import colorama


colorama.init(autoreset=True)
# comp test 1
file1 = open(r'C:\Users\cyber\PycharmProjects\fimsuite\testFiles\stored_hashes')
file2 = open(r'C:\Users\cyber\PycharmProjects\fimsuite\testFiles\check_stored_hashes')
line_position = 0


for line1 in file1:
    line_position += 1

    for line2 in file2:
        if line1 == line2:
            print(f"{colorama.Fore.GREEN}Line {line_position} -> [+] MATCH")
            print(f"{line1}", end='')
            print(f"{line2}")
        else:
            print(f"{colorama.Fore.MAGENTA}Line {line_position} -> [!] FILE CHANGED")
            print(f"{line1}", end='')
            print(f"{line2}")
        break

file1.close()
file2.close()
