from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
from get_highs_lows_func import get_highs_lows

# Get dates, low, and high temperatures from file.
filename1 = 'death_valley_2018_full.csv'
filename2 = 'sitka_weather_2018_full.csv'
dates_ca, highs_ca, lows_ca = get_highs_lows(filename1, 6, 7)
dates_ak, highs_ak, lows_ak = get_highs_lows(filename2, 8, 9)

# Plot data.
fig = plt.figure(dpi = 128, figsize=(10,6))
plt.plot(dates_ca, highs_ca, c='red', alpha=0.5)
plt.plot(dates_ca, lows_ca, c='blue', alpha=0.5)
plt.plot(dates_ak, highs_ak, c='crimson', alpha=0.5)
plt.plot(dates_ak, lows_ak, c='deepskyblue', alpha=0.5)
plt.fill_between(dates_ca, highs_ca, lows_ca, facecolor='blue', alpha=0.1,
    label='Death Valley, CA')
plt.fill_between(dates_ak, highs_ak, lows_ak, facecolor='crimson', alpha=0.1,
    label='Sitka, AK')

# Format plot.
myFmt = DateFormatter("%b %Y")
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
title += " and Sitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim([0, 150])
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()

plt.show()
