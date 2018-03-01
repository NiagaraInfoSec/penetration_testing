import itertools
import os.path

import fileutilities

LENGTH = 5
SYMBOLS = [str(x) for x in range(10)]

def generate_zip_codes(length=LENGTH, symbols=SYMBOLS):
    """usage: generate_zip_codes(length=LENGTH, symbols=SYMBOLS) => iterator of zip codes
       usage: for zip_code in generate_zip_codes(): ...
    Produces an iterator which yields zip codes of the specified form.
    length is an integer that indicates the quantity of symbols in each zip code string, which defaults to 5
    symbols is a sequence of strings which indicates the symbol set used in the zip codes, which defaults to 0-9
        - Alternative zip codes may incorporate A-Z as well as 0-9"""
    for entry in itertools.product(*(symbols for count in range(length))):
        yield ''.join(entry)
        
def test_generate_zip_codes():
    for zip_code in generate_zip_codes():
        print zip_code
        
def write_zip_codes_to_file(filename="../data/zipcodes/zipcodes.txt",
                            length=LENGTH, symbols=SYMBOLS):
    fileutilities.ensure_folder_exists(os.path.split(filename)[0])
    with open(filename, 'w') as _file:
        for zip_code in generate_zip_codes(length, symbols):
            _file.write(zip_code + '\n')
        _file.flush()
        
if __name__ == "__main__":
    #test_generate_zip_codes()
    write_zip_codes_to_file()
    