#!/usr/bin/python3
import configparser
from pathlib import Path

 
def config(filename='database.ini', section='DEFAULT'):
    cwd = Path(__file__).resolve().parents[1]
    dbconfig = cwd / 'cfg' / filename
    parser = configparser.ConfigParser()
    parser.read(dbconfig)
    dbparams = {}

    if parser.has_section('postgresql'):
        dbparams = parser['postgresql']

    # Returns an error if a parameter is called that is not listed in the initialization file
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        
    return dbparams


if __name__ == '__main__':
   config()


