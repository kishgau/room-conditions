#!/usr/bin/env python3
#############################################################################
# Filename    : Data.py
# Description :	Capture the temperature and humidity data of Sensors.py
# Author      : freenove
# modification: 2018/08/03
########################################################################
import csv
from pathlib import Path
#Dummy data
humidity = 70.0
temperature = 21.1

def datalogger(humidity,temperature):
    cwd = Path(__file__).resolve().parents[1]
    dataLogger = cwd / 'data' / 'sensor.out'
    print(dataLogger)
    with open( dataLogger, 'w+', newline='') as csvfile:
        dataWritter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dataWritter.writerow([humidity,temperature])


