import os.path

from fileutilities import list_files

def extract_private_schools():
    source_dir = os.path.join("..", "data", "privateschools") 
    
    files = list_files(os.path.join(source_dir, "raw"))
    for filename in files:
        with open(filename, "r") as input_file:
            state = input_file.readline()[3:-1]
            for line_number in range(5): # skip misc. data
                line = input_file.readline()                
            print state
            school_filename = os.path.join(source_dir, "{}_school.txt".format(state))                
            with open(school_filename, "w") as output_file:
                for line in input_file.readlines():
                    #A0102965,ADVENTIST MALAMA ELEMENTARY SCHOOL,3,13,86-072 FARRINGTON HWY,WAIANAE,15003,003,HI,15,96792,8086963988,180,6.5,Yes,,,13,13,5,10,4,8,2,2,6,,,,,63,63,0,0,0,7,0,56,0,4,21,1,1,1,2,2,0,0,0,11.11,0,88.89,0,15.75,28,HONOLULU,Other religious school association(s),,,,,,,      
                    school_name = line.split(',', 2)[1]                       
                    output_file.write(school_name + "\n")
                output_file.flush()
            
if __name__ == "__main__":
    extract_private_schools()
    