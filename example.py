import csv
from sense_hat import SenseHat
from datetime import datetime
from time import time, sleep

sense = SenseHat()
sense.clear


##create time data list
time_data = []

##create temperature data list
temp_data = []


counter = 0
while counter < 60: ## run for 1 minute
    timeStamp= datetime.now()
    time_data.append(timeStamp)
    tempValue = sense.get_temperature()
    temp_data.append(tempValue)
    sense.show_message(str(round(tempValue, 1)) + "C")
    print(timeStamp)
    print(temp_data)
    sleep(1)  ## run every 1 minute
    counter = counter + 1

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for w in range(len(time_data)):
        writer.writerow([time_data[w], temp_data[w]])




