#!/usr/bin/env python3
#############################################################################
# Filename    : Data.py
# Description :	Capture the temperature and humidity data of Sensors.py
# Author      : freenove
# modification: 2018/08/03a
########################################################################
import csv
from pathlib import Path
#Dummy data
humidity = 70.0
temperature = 21.1

def datalogger(humidity,temperature):
    _cwd = Path(__file__).resolve().parents[1]
    _datalogger = _cwd / 'out' / 'sensor.out'
    with open( _datalogger, 'w+', newline='') as csvfile:
        data_writter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data_writter.writerow([humidity,temperature])


