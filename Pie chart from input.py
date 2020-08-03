import matplotlib.pyplot as plot

# is it possible to ask how many variables, then according to that, give input for that number of variables?
a = input_str=input('input variables in the following way\n name1,value1,name2,value2,....')
a.split(',')

figureObject, axesObject = plot.subplots()
# Draw the pie chart
axesObject.pie(a,
               labels=a,
               autopct='%1.2f',
               startangle=90)
axesObject.axis('equal')

plot.show()
#i