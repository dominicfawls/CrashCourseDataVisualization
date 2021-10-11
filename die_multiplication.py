# This program shows what happens when you multiply
# the results of the die when rolled, instead of adding.
import pygal
from die import Die

# Create desired number of dice.
# Ex. Die():six-sided die, Die(10):ten-sided die
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
possible_results = []
die_1_sides = list(range(1, die_1.num_sides))
die_2_sides = list(range(1, die_2.num_sides))

# Creates a list with only the possible results of the dice multiplication.
for side1 in die_1_sides:
    for side2 in die_2_sides:
        mult_result = side1 * side2
        if mult_result not in possible_results:
            possible_results.append(mult_result)

max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    if value in possible_results:
        frequency = results.count(value)
        frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Multpilcation of the results from rolling one D6 "
hist.title += "and one D10 50,000 times."
hist.x_labels = possible_results
hist.x_title = "Result"
hist.y_title =  "Frequency of Result"

hist.add('D6 * D10', frequencies)
hist.render_to_file('dice_multiplication.svg')
