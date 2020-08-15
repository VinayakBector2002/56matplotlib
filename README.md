# 56matplotlib
Matplotlib Codes
Owing to my love for graphs I was introduced to this amazing world of Conic Sections, commonly known Conics. As I explored, pondered and discovered new and quite exciting stuff in maths, I eventually decided to take a very bold step and Extrapolate this interest of mine, in my CS project. 
It started as a  parametric Equation of circle, which could be printed using Trig Ratios in Matplotlib. Then slowly I watched a few lessons and courses on Youtube to expand my knowledge and understanding of the topic. With multiple drafts and code reviews, and help from all my well-wishers I was able to dexterously craft a 250 line code, with 3 nested while loops and multiple if loops within it.
The programme offers you many different choices. 
First, it introduces you with a Menu, bombarding you with multiple options, so that you can print your favourite conic section.

# I have used many modules in my code, a brief description of each is provided as follows :

# Numpy Meshgrid function
The numpy.meshgrid function is used to create a rectangular grid out of two given one-dimensional arrays representing the Cartesian indexing or Matrix indexing. Meshgrid function is somewhat inspired from MATLAB.
Consider the above figure with X-axis ranging from -4 to 4 and Y-axis ranging from -5 to 5. So there are a total of (9 * 11) = 99 points marked in the figure each with a X-coordinate and a Y-coordinate. For any line parallel to the X-axis, the X-coordinates of the marked points respectively are -4, -3, -2, -1, 0, 1, 2, 3, 4. On the other hand, for any line parallel to the Y-axis, the Y-coordinates of the marked points from bottom to top are -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5. The numpy.meshgrid function returns two 2-Dimensional arrays representing the X and Y coordinates of all the points.
 
# Numpy Linspace
The NumPy linspace function (sometimes called np.linspace) is a tool in Python for creating numeric sequences.
The NumPy linspace function creates sequences of evenly spaced values within a defined interval.
Essentally, you specify a starting point and an ending point of an interval, and then specify the total number of breakpoints you want within that interval (including the start and end points). The np.linspace function will return a sequence of evenly spaced values on that interval.
To illustrate this, here’s a quick example. (We’ll look at more examples later, but this is a quick one just to show you what np.linspace does.)

np.linspace(start = 0, stop = 100, num = 5)


# Axhline:
Matplotlib.pyplot.axhline (Value)
Literally means an axis line (straight line) with is Horizontal in nature; this is where ‘h’ in axhline is derived from.
Similarly 
Axvline:
Matplotlib.pyplot.axvline (Value)
Produces a vertical line on the grid(i.e graph output). 

# Contour:
Contour function, which is usually used to represent a 3-d array on a 2-d platform.
In the code you’ll observe that I used the meshgrid X and Y coordinates and in place of Z coordinates, the equation of conic. The Z coordinate array, in this case the equation of conic, has a parameter [Value, to satisfy the equation] to make the equation of conics mathematically sound. 
Contour has many benefits, first and foremost being the ease with which you  can print complex graphs, along with features like adding colors and label lines with different altitudes/ heights (called contour). 
This will also help us in the future to add multiple conics on the same graphs, with different altitudes to add a parallax effect, which will help us, differentiate these graphs with ease.  
