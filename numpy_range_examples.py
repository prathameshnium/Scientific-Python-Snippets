"""
Demonstration of NumPy Array Generation Methods.

This script serves as a reference for creating numerical sequences (arrays and lists)
in Python using different NumPy functions. It showcases two common approaches
for generating a range of numbers with a fixed step or increment.

Example 1 (np.arange):
  - Uses `np.arange` to create an array with a specified start, stop, and step size.
  - Demonstrates converting the resulting NumPy array into a standard Python list.

Example 2 (np.linspace):
  - Shows a method to calculate the required number of data points to simulate
    a step size using `np.linspace`. This is useful when you need to guarantee
    the inclusion of both the start and end points in the sequence.

This script is for demonstration purposes and prints its output to the console.
"""

#print(np.arange(-10, 10, 0.5))
a=np.arange(-10, 10, 0.5)
l1=[]
for x in a:
  l1.append(x)

print(l1)

#-------------------------------------------

#jugad

I=10
import math
Inc=0.5

div=(2*I)/(Inc)
np.linspace(-I,I,math.ceil(div))

