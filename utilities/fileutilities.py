import os.path

def list_files(dir_name): 
    files = []
    for filename in os.listdir(dir_name):    
        source_file = os.path.join(dir_name, filename)
        if os.path.isfile(source_file):
            files.append(source_file)
    return files