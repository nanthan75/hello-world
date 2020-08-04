import matplotlib.pyplot as plt
input_str = input('input variables in the following way: var1, val1, var2,val2,.....')

data = input_str.split(',')
labels = data[0:-1:2]
values = data [1::2]
print("look at taskbar for matplotlib chart")
plt.pie(values, labels=labels, startangle=90, autopct='%1.1f%%')

plt.axis('equal')
