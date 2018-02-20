import os
import os.path

from fileutilities import list_files
    
def find_missing_files():    
    source_dir = os.path.join("..", "data", "schools") 
    files1 = [item.rsplit('.', 1)[0].rsplit('\\', 1)[-1] for item in list_files(source_dir)]
    
    source_dir = os.path.join("..", "data", "schools", "alreadydone")
    files2 = [item.rsplit('.', 1)[0].rsplit('\\', 1)[-1] for item in list_files(source_dir)]
    
    print '\n'.join(sorted(list(set(files2).difference(files1))))
    
if __name__ == "__main__":
    find_missing_files()
    