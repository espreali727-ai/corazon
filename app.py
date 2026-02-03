import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Para mi novia ❤️", layout="centered")
st.title("Un regalito para ti... ❤️")

# Reducimos a 40 para que cargue rápido en la web
res = 40 

fig, ax = plt.subplots(subplot_kw={"projection":"3d"}, figsize=(8,8))
fig.set_facecolor("black")
ax.set_facecolor("black")
ax.set_axis_off()

def heart_3d(x,y,z):
    a = (x**2 + (9/4)*(y**2) + z**2 - 1)**3
    b = (x**2) * (z**3)
    c = (9/80) * (y**2) * (z**3)
    return a - b - c

bbox = (-2,2)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
A = np.linspace(xmin, xmax, res)
B = np.linspace(xmin, xmax, res)
A1, A2 = np.meshgrid(A, A)

for z in B:
    X, Y = A1, A2
    Z = heart_3d(X, Y, z)
    ax.contour(X, Y, Z + z, [z], zdir="z", colors="#FF0000", linewidths=0.5)

ax.set_zlim3d(zmin, zmax)
ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)

# Mostrar en la web
st.pyplot(fig)
st.write("### Eres el 'import' de mi vida 💘")