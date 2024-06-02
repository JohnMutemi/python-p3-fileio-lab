def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as file_obj:
        file_obj.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as file_obj:
        file_obj.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as file_obj:
        return file_obj.read()
