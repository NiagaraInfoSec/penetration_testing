data = ''
with open("../data/commonsurnamesmetadata.txt", "r+") as _file:
    for line in _file.readlines():        
        data += line.split('\t')[0] + '\n'              
    with open("../data/commonsurnames.txt", "a") as _file:
        _file.write(data)
        _file.flush()
    