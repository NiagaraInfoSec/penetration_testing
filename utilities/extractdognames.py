import os.path

from fileutilities import list_files

def extract_dognames():
    source_dir = os.path.join("..", "data", "petnames") 
    files = list_files(os.path.join(source_dir, "raw"))  
    for filename in files:
        with open(filename, "r") as input_file:
            destination_filename = os.path.join(source_dir, os.path.split(filename)[-1])
            with open(destination_filename, 'w') as destination_file:
                for line in input_file.readlines():
                    #1. Bailey (2*)	1. Bella (1*)
                    name1 = line.split(' ', 1)[1].split('\t')[0]
                    name2 = line.split('\t', 1)[1].split(' ', 1)[1]
                    destination_file.write(name1 + '\n')
                    destination_file.write(name2)
                        
if __name__ == "__main__":
    extract_dognames()
        