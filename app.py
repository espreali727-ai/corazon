import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Para la mas hermosa :3", layout="centered")

# Título con estilo
st.markdown("<h1 style='text-align: center; color: red;'> TE AMO WAWI :33 </h1>", unsafe_allow_html=True)

# Control para que ella lo mueva
angulo = st.slider("Gira el corazón para verlo mejor", 0, 360, 45)

# Función del corazón (la misma que ya tienes)
def heart_3d(x,y,z):
    a = (x**2 + (9/4)*(y**2) + z**2 - 1)**3
    b = (x**2) * (z**3)
    c = (9/80) * (y**2) * (z**3)
    return a - b - c

fig, ax = plt.subplots(subplot_kw={"projection":"3d"}, figsize=(8,8))
fig.set_facecolor("black")
ax.set_facecolor("black")
ax.set_axis_off()

res = 40 
bbox = (-2,2)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
A = np.linspace(xmin, xmax, res)
B = np.linspace(xmin, xmax, res)
A1, A2 = np.meshgrid(A, A)

for z in B:
    X, Y = A1, A2
    Z = heart_3d(X, Y, z)
    ax.contour(X, Y, Z + z, [z], zdir="z", colors="#FF0000", linewidths=0.7)

# Aquí es donde ocurre la rotación según el slider
ax.view_init(elev=10, azim=angulo)

ax.set_zlim3d(zmin, zmax)
ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)

# Mostrar el gráfico
st.pyplot(fig)

st.write("Eres el amor de mia vida <3")
