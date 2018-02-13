"""usage: command | python dumptxt.py file_name.txt
    
   Writes the output from command to file_name.txt
   
   Example: python sqlmap.py --options | python dumptxt.py sqlmap_dump.txt"""
import sys

with open(sys.argv[1], 'wb') as _file:
    _file.write(sys.stdin.read())