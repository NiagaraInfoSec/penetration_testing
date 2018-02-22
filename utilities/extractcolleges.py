import os.path

from fileutilities import list_files

def extract_colleges():
    source_dir = os.path.join("..", "data", "colleges") 
    files = list_files(os.path.join(source_dir, "raw"))  
    for filename in files:
        with open(filename, "r") as input_file:
            lines = input_file.readlines()[1:-3] # remove the lines without school information
            line = lines[0].split(',', 1)[1]       
            end_of_address = line.index('"', 1)
            address = line[1:end_of_address]
            state_and_zip = address.split(',', 2)[-1][1:]                 
            state = state_and_zip.split(' ', 1)[0]            
            destination_filename = os.path.join(source_dir, "{}.txt".format(state))
            with open(destination_filename, 'w') as destination_file:
                for line in lines:
                    school = line.split(',', 1)[0][1:-1] # remove quotes                           
                    destination_file.write(school + '\n')
             
if __name__ == "__main__":
    extract_colleges()
        