import os
import os.path
import errno

def list_files(dir_name): 
    files = []
    for filename in os.listdir(dir_name):    
        source_file = os.path.join(dir_name, filename)
        if os.path.isfile(source_file):
            files.append(source_file)
    return files
    
def ensure_folder_exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise    