import os.path

from fileutilities import list_files

def extract_names():
    source_dir = os.path.join("..", "data", "names") 
    files = list_files(os.path.join(source_dir, "raw"))  
    for filename in files:
        with open(filename, "r") as input_file:
            destination_filename = os.path.join(source_dir, os.path.split(filename)[-1])
            with open(destination_filename, 'w') as destination_file:
                for line in input_file.readlines():
                    name = line.split('\t', 1)[0]
                    destination_file.write(name + '\n')
                        
if __name__ == "__main__":
    extract_names()
        