import itertools
import os.path

import fileutilities

SYMBOLS = [str(x) for x in range(10)]
FORMAT_STRING = "{}"
SEPARATOR = '-'
LENGTH = 8
SECTIONS = (3, 5)

def generate_phone_numbers(symbols=SYMBOLS, format_string=FORMAT_STRING, separator=SEPARATOR, 
                           length=LENGTH, sections=SECTIONS):  
    """usage: generate_phone_numbers(symbols=SYMBOLS, format_string=FORMAT_STRING,
                                     separator=SEPARATOR, length=LENGTH, 
                                     sections=SECTIONS) => iterator of phone numbers
       usage: for phone_number in generate_phone_numbers(): ...
        Generates an iterator that yields phone numbers of the specified configuration.
        symbols is a sequence of characters that indicates the symbol set used in the number, typically 0-9
        format_string is the base string that symbols will be inserted into
            - Alternative configurations may use "({})" instead of "{}" to generate phone numbers with parenthesis surrounding the area code
        separator is the string delimiter between blocks, which defaults to '-'
        length is an integer that represents the total quantity of symbols in the phone number, which defaults to 8
            - sum(sections) must equal length
        sections is a collection of integers which indicates how many symbols are in each section of the phone number
            - Default is (3, 5), which produces numbers of the form xxx-xxxxx
            - Alternatively, to include area codes, set sections to (3, 3, 5) (and ensure that length is set to 11)"""
    if sum(sections) != length:
        raise ValueError("sum(sections) must equal length; sections: {}; length: {}".format(sections, length))
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
                                symbols=SYMBOLS, format_string=FORMAT_STRING, separator=SEPARATOR,
                                length=LENGTH, sections=SECTIONS):
    fileutilities.ensure_folder_exists(os.path.split(filename)[0])
    with open(filename, 'w') as _file:
        for phone_number in generate_phone_numbers(symbols, format_string, separator, length, sections):
            _file.write(phone_number + '\n')
        _file.flush()
        
if __name__ == "__main__":
    #test_generate_phone_numbers()
    write_phone_numbers_to_file()
    