import matplotlib.pyplot as plt

a = input("name of variable 1")
b = input("name of variable 2")
c = input("name of variable ")
d = input("name of variable 4")

labels = [a, b, c, d]

colors = ['blue', 'yellow', 'green', 'orange']

e = input("value of v1")
f = input("value of v2")
g = input("value of v3")
h = input("value of v4")
sizes = [e, f, g, h]

plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')

plt.axis('equal')

plt.show()
