import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Temperature")
  
plt.xticks(rotation = 25)
plt.xlabel('Time')
plt.ylabel('Temperature(°C)')
plt.title('Temperature Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()