# Date generator
# xx/yy/zzzz
import os.path
import datetime

from fileutilities import ensure_folder_exists

_now = datetime.datetime.now()
YEAR = _now.year
MONTH = _now.month
DAY = _now.day
del _now

DAYS = range(1, 32)
MONTHS = range(1, 13)
YEARS = [item for item in reversed(range(YEAR + 1))]
ORDERING = ("month", "day", "year")
SEPERATOR = '/'

def date_generator(days=DAYS, months=MONTHS, years=YEARS, ordering=ORDERING, separator=SEPERATOR):
    """usage: date_generator(days=DAYS, months=MONTHS, years=YEARS,
                             ordering=ORDERING, separator=SEPARATOR) => iterator of dates
       usage: for date in date_generator(): ...
       
       Produces an iterator which yields dates of the specified configuration
       days is a sequence of numbers which indicates the range of days to be produced, which defaults to 1-31
       months is a sequence of numbers which indicates the range of months to be produced, which defaults to 1-12
       years is a sequence of numbers which indicates the range of years to be produced, which defaults to 0-current year
       ordering is a sequence of ("month", "day", "year") which indicates the ordering of the values
            - default produces dates of the form mm/dd/yyyy, alternative configurations might be dd/mm/yyyy
       separator is a string indicating the delimiter between months/days/years
       
       Values generated this way are not guaranteed to indicate valid calendar days 
            - e.g. 02/30/2000 would indicate February 30th, which is not a valid date
            - If only valid calendar dates are required, then the caller should filter the results"""
    # just ignore months having different numbers of days - it would be slower and complilcated to go through them properly
    variables = locals()
    leftmost = variables[ordering[0] + 's']
    middle = variables[ordering[1] + 's']
    rightmost = variables[ordering[2] + 's']
    format_string = "{{}}{}{{}}{}{{}}".format(separator, separator)
    assert format_string == "{}/{}/{}"
    for right in rightmost:
        for _middle in middle:
            for left in leftmost:
                yield format_string.format(left, _middle, right)

def test_date_generator():
    for date in date_generator():
        print date
        
def write_dates_to_file(filename="../data/dates/dates.txt",
                        days=DAYS, months=MONTHS, years=YEARS, ordering=ORDERING, separator=SEPERATOR):
    ensure_folder_exists(os.path.split(filename)[0])
    with open(filename, 'w') as _file:
        for date in date_generator():
            _file.write(date + '\n')
        _file.flush()
        
if __name__ == "__main__":
    #test_date_generator()
    write_dates_to_file()
    