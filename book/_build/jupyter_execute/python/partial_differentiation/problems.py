#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import numpy as np

X0 = np.arange(-1.5, 1.5, 0.1)
Y0 = np.arange(-1, 2.5, 0.1)
X, Y = np.meshgrid(X0, Y0)
Z = Y**3 + 3 * X**2*Y -3 * X**2 - 3 * Y**2 + 2

# fig = go.Figure(data=go.Surface(z=Z,x=X, y=Y))

# fig.show()

fig = go.Figure(data=go.Contour(z=Z,x=X0, y=Y0, contours=dict(
            type="levels", 
            start=Z.min(),
            end=Z.max(),
            size=.2)))

fig.show()

