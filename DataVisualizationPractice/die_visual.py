import pygal
from die import Die

# Create desired number of dice.
# Ex. Die():six-sided die, Die(10):ten-sided die
die_1 = Die()
die_2 = Die(10)
die_3 = Die(12)

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6, one D10, and one D12 50,000 times."
x_labels = list(range(3, max_result+1))
hist.x_labels = [str(x) for x in x_labels]
hist.x_title = "Result"
hist.y_title =  "Frequency of Result"

hist.add('D6 + D10 + D12', frequencies)
hist.render_to_file('dice_visual.svg')
