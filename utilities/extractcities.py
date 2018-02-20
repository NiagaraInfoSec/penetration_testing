import os.path

from fileutilities import list_files

def extract_cities():
    source_dir = os.path.join("..", "data", "cities") 
    files = list_files(os.path.join(source_dir, "raw"))
    destination_file1 = os.path.join(source_dir, "citystatecountry.txt")
    destination_file2 = os.path.join(source_dir, "cities.txt")
    for filename in files:
        with open(filename, "r") as input_file:
            with open(destination_file1, 'w') as output_file:
                with open(destination_file2, 'w') as output_file2:
                    for line in input_file.readlines():                               
                        location = line.split(',', 2)[-1]
                        try:
                            end_index = location.index('"', 1)
                        except ValueError:
                            location = location.split(',', 1)[0]
                        else:
                            location = location[1:end_index]
                        output_file.write(location + '\n')
                        output_file2.write(location.split(',', 1)[0] + '\n')
                        
if __name__ == "__main__":
    extract_cities()
        