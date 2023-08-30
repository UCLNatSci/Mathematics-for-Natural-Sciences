#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objs as go
import plotly

#the start and end point for each line
#pairs = [(0,6), (1,7)]


p1 = [1, -2, 3]
v1 = [1, -1, 2]

p2 = [4, 2, 4]
v2 = [3, 4, 1]

a = p1 + -2*np.array(v1)
b = p1 + 2*np.array(v1)

c = p2 + -2*np.array(v2)
d = p2 + 2*np.array(v2)

x_lines = [a[0], b[0], None, c[0], d[0]]
y_lines = [a[1], b[1], None, c[1], d[1]]
z_lines = [a[2], b[2], None, c[2], d[2]]

trace2 = go.Scatter3d(
    x=x_lines,
    y=y_lines,
    z=z_lines,
    mode='lines',
    name='lines'
)



fig = go.Figure(data=[trace2])
plotly.offline.iplot(fig, filename='simple-3d-scatter')

