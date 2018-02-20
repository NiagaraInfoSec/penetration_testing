import os.path

from fileutilities import list_files

def extract_schools():
    source_dir = os.path.join("..", "data", "schools") 
    
    files = list_files(os.path.join(source_dir, "raw"))
    for filename in files:
        with open(filename, "r") as input_file:
            for line_number in range(10): # state identifier is on the 10th line        
                line = input_file.readline()
            #"SEARCH CRITERIA: State: ""Maine"" School Description: ""Regular, Special Education, Vocational, Other/Alternative""",,,,,,,,,,,,,,,,,,,,,,,,,        
            line = line.split(':', 2)[-1] # remove SEARCH CRITERIA: State: ...
            start_index = line.index('""') + 2
            end_index = line.index('""', start_index)
            state = line[start_index:end_index]
            _disclaimer = input_file.readline()
            _layout = input_file.readline()             
            school_filename = os.path.join(source_dir, "{}_school.txt".format(state))                
            with open(school_filename, "w") as output_file:
                for line in input_file.readlines():
                    # 2.30282E+11,ME-42-45,2302820,ME-42,PK,03,Abraham Lincoln School,Bangor Public Schools,Penobscot County,45 Forest Avenue,Bangor,ME,04401,,(207)941-6280,13,City: Small,No,No,Yes,Yes,220.00000,17.70000,12.4000000,111.00000,10.00000
                    school_name = line.split(',', 7)[6]            
                    school_name = school_name.replace("Elem ", "Elementary ")
                    school_name = school_name.replace("Elem\n", "Elementary\n")
                    output_file.write(school_name + "\n")
                output_file.flush()
            
if __name__ == "__main__":
    extract_schools()
    