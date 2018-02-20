import os.path

from fileutilities import list_files

def extract_streets():
    source_dir = os.path.join("..", "data", "streets") 
    files = list_files(os.path.join(source_dir, "raw"))  
    for filename in files:
        with open(filename, "r") as input_file:
            destination_filename = os.path.join(source_dir, os.path.split(filename)[-1])
            with open(destination_filename, 'w') as destination_file:
                street_list = []
                for street in input_file.readlines():
                    frequency, street = street.split('\t', 1)
                    street_list.append((int(frequency), street))
                                
                for frequency, street in reversed(sorted(street_list)):                              
                    destination_file.write(street)
                                                            
if __name__ == "__main__":
    extract_streets()
        