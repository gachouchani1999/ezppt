from flask import request
def store_file(*file):
    for f in file:
        store_file.file_name =  str(f.filename)
    return store_file.file_name
