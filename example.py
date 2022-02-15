import csv
from sense_hat import SenseHat
from datetime import datetime
from time import time, sleep

sense = SenseHat()
sense.clear

timeStamp= datetime.now()

##create temperature data list
temperature_data = [ ]


counter = 0
while counter < 1800: ## run for 30 minutes
    temperature_data.append(timeStamp)
    temp = sense.get_temperature()
    temperature_data.append(temp)
    sense.show_message(str(round(temp, 1)) + "C")
    print(timeStamp)
    print(temperature_data)
    sleep(1)  ## run every 1 minute
    counter = counter + 1

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(temperature_data)




