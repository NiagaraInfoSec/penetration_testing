import os.path
import itertools
import json

from fileutilities import list_files

def extract_books():
    source_dir = os.path.join("..", "data", "books") 
    
    files = list_files(os.path.join(source_dir, "raw"))
    for input_filename in files:
        file_size = os.path.getsize(input_filename)
        with open(input_filename, "r") as input_file:
            output_filename = os.path.join(source_dir, "books.txt")
            with open(output_filename, "w") as output_file:
                            
                line = input_file.readline()                
                progress = 0.0
                while line:                
                    for progress_counter in xrange(100000):
                        json_data = line.split('\t', 4)[-1]
                        book_info = json.loads(json_data)
                        try:
                            book_name = book_info["title"].encode("utf-8")
                        except KeyError:                        
                            if not line:                                
                                break
                            else:                                       
                                line = input_file.readline()
                                continue
                        else:
                            output_file.write(book_name + "\n")
                            progress += len(line)
                            line = input_file.readline()       
                            #print "Next line"
                    output_file.flush()
                    print("Progress: {}/{} = {}%".format(progress, file_size, progress / file_size))    
    
if __name__ == "__main__":
    extract_books()
    