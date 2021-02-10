Blake Hartung - bhartung@uw.edu

Data: I scraped my data from 
https://en.wikipedia.org/wiki/Lists_of_Atlantic_hurricanes
and cleaned it in python to create a csv file with the data i wanted.
I then made the visualizations in R using ggplot2.


Ehtical File: violin_density_bh.png

This visualization aims to answer any questions about atlantic hurricane
occurence density based on the Saffir-Simpson Scale and year of appearance.
A common question associated with Hurricane occurrence is "Is climate change
causing hurricanes to get stronger?" Here, I created a horizontal violin plot
with data separations based on Saffir-Simposon category, showing the increase
(or decrease) of specific strength hurricanes over time. I chose an
increased saturation Green to represent each bin, offering a look into the relative
power of each storm. To increase clarity, I created a small histogram capturing the
occurence count throughout the timeline. I added median dots and standard deviation
whiskers to the violin plot to show a slight tendency for stronger storms during
the 21st century. Overall, the violin plots do a great job of showing time-related
density data, where a continuous length value would represent the ratio data.

Unethical File: yearly_averages_bh.png

This visualization aims to offer an answer to "How have storms changed over time?"
I used yearly summary statistics to plot against a specific stat in an opaque
red color to not create a cluttered looking visualization. I then added a
loess smoothing line to the visualization to show a trend throughout the shown
timeline. Here, the visualizations are deceptive as data from before 1950
has no values for category 5 hurricanes, something that inevitably happened.
These hurricanes will skew data in the later years as they are the most polarizing
stats within the dataset. Next, my Y-axis limits are heavily constrained, 
with wind speed range starting at 80 mph, where a more ethical graph would
probably begin at 74 mph (the min wind for hurricane classification). This
constraint is better defined on the pressure graph, where aa range from
930-995 mbar is shown, where a more ethical graph would show something like
882 mbar (lowest pressure recorded in atlantic) to at least 1013 mbar
(average sea level pressure). These constrains prove to show much higher looking
wind vals, and lower pressures, in the 21st century, both stats typically
offer a clue into storm strength.


