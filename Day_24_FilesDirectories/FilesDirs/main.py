

def basic_open_read_file():
    file = open("data.txt")
    content = file.read()
    print(content)
    file.close()


def open_red_file_using_with():
    with open("data.txt") as file:
        content = file.read()
        print(content)
        # Do not need to close


def write_to_file_using_with():
    mode = "a"
    with open("data.txt", mode) as file:
        file.write("\nNew text")

# ========= ===============================================================
# Character Meaning
# --------- ---------------------------------------------------------------
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)
# ========= ===============================================================


def create_new_file_and_write_to_file():
    mode = "w"
    with open("new-data.txt", mode) as file:
        file.write("Some text")
