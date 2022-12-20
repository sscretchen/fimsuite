import hashlib


def hash_file(filename):
    # capture files and return the SHA-1 hash
    hash = hashlib.sha1()

    # open file in BIN read mode, loop through file 1mb at a time
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()
