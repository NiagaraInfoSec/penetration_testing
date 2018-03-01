import itertools
import os.path

import fileutilities

SYMBOLS = [str(x) for x in range(10)]
FORMAT_STRING = "{}"
SEPERATOR = '-'
LENGTH = 8
SECTIONS = (3, 5)

def generate_phone_numbers(symbols=SYMBOLS, format_string=FORMAT_STRING, seperator=SEPERATOR, 
                           length=LENGTH, sections=SECTIONS):  
    for symbols in itertools.product(*(symbols for count in range(length))):
        symbols = ''.join(symbols)
        number = format_string
        _index = 0
        for subsection in sections:            
            section_numbers = symbols[_index:_index + subsection]
            number = number.format(section_numbers) + "-{}"
            _index += subsection            
        yield number[:-3]
        
def test_generate_phone_numbers():
    for phone_number in generate_phone_numbers():
        print phone_number
        
def write_phone_numbers_to_file(filename="../data/phonenumbers/phonenumbers.txt",
                                symbols=SYMBOLS, format_string=FORMAT_STRING, seperator=SEPERATOR,
                                length=LENGTH, sections=SECTIONS):
    fileutilities.ensure_folder_exists(os.path.split(filename)[0])
    with open(filename, 'w') as _file:
        for phone_number in generate_phone_numbers(symbols, format_string, seperator, length, sections):
            _file.write(phone_number + '\n')
        _file.flush()
        
if __name__ == "__main__":
    #test_generate_phone_numbers()
    write_phone_numbers_to_file()
    