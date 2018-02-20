import os.path

from fileutilities import list_files

def extract_streets():
    source_dir = os.path.join("..", "data", "streets") 
    files = list_files(os.path.join(source_dir, "raw"))  
    for filename in files:
        with open(filename, "r") as input_file:
            destination_filename = os.path.join(source_dir, os.path.split(filename)[-1])
            with open(destination_filename, 'w') as destination_file:
                streets = reversed(sorted(input_file.readlines()))
                destination_file.write(''.join(item.split('\t')[1] for item in streets))
                                            
if __name__ == "__main__":
    extract_streets()
        