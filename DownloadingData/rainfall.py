import csv
import numpy
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

filename = 'seattle_2020.csv'

# Get precipitation data from csv file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rainfall = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            precip = row[5]
        except ValueError:
            print(current_date, 'missing data')
            print(precip)
        else:
            dates.append(current_date)
            rainfall.append(precip)

# Plot data.
fig = plt.figure(dpi = 128, figsize=(10,6))
plt.bar(dates, rainfall, alpha=0.75, label='Daily Rainfall\nVienna, VA')

# Format plot.
myFmt = DateFormatter("%b %Y")
title = "Daily precipitation - 2011\nSeattle, WA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (in.)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xlim([dates[0], dates[-1]])
plt.yticks(numpy.arange(0, float(max(rainfall)), .5)) # have to work on the tick spacing still...
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()

plt.show()
