# PART 1 - IMPORT MATPLOTLIB
# Before drawing any chart you need to import the matplotlib libary.
# matplotlib.pyplot is the drawing tool ---"plt" is its short nickname.
import matplotlib.pyplot as plt

# PART 2 - YOUR DATA
# days holds the x-axis labels -- the days of your school week.
# savings holds the y-axis values -- your quiz savings for each day.
# Every savings pairs up with the day in the same position.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
savings = [70, 85, 60, 125, 75, 150, 128]

# PART 3 - PLOT YOUR FIRST LINE GRAPH
# plt.plot(x, y) draws a line through all your data points.
# plt.show() opens the chart window -- call it at the end of every chart.
plt.plot(days, savings)
plt.show()

# PART 4 - ADD LABELS AND A TITLE
# plt.title() -- adds a heading at the top of the chart.
# plt.xlabel() -- labels the x-axis (across the bottom).
# plt.ylabel() -- labels the y-axis (up the side).
# plt.grid(True) -- adds faint gridlines so values are easier to read.
# plt.ylim(0, 150) -- locks the y-axis from 0 to 150 so savings fit neatly.
plt.plot(days, savings)
plt.title('My savings Progress Chart')
plt.xlabel('Day of the week')
plt.ylabel('savings')
plt.grid(True)
plt.ylim(0, 150)
plt.show()

# PART 5 - STYLE YOUR LINE CHART
# color='blue' -- changes the line colour.
# marker='o' -- puts a filled dot on every data point.
# linestyle='dashed' -- draws the line as dashes instead of solid.
# linewidth=2 -- makes the line thicker so it stands out.
# All four style options go inside the same plt.plot() call.
plt.plot(days, savings, color='green', marker='o', linestyle='dashed', linewidth=2)
plt.title('My savings Progress Chart')
plt.xlabel('Day of the week')
plt.ylabel('savings')
plt.grid(True)
plt.ylim(0, 150)
plt.show()

# PART 6 - DRAW A BAR CHART
# plt.bar(x, y) draws a bar chart -- one bar per day rising to its score.
# Bar charts are great for comparing values side by side.
# color='orange' fills every bar with orange.
# The same title, labels, and ylim commands work exactly the same way.
plt.bar(days, savings, color='lightblue')
plt.title('My savings Progress Chart')
plt.xlabel('Day of the week')
plt.ylabel('savings')
plt.grid(True)
plt.ylim(0, 150)
plt.show()