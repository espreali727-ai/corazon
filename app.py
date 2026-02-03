import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Para la mas hermosa :3", layout="centered")

# Título
st.markdown("<h1 style='text-align: center; color: red;'>Te amitoo</h1>", unsafe_allow_html=True)

# Creamos un lugar vacío para el gráfico
placeholder = st.empty()

# Función del corazón
def heart_3d(x,y,z):
    a = (x**2 + (9/4)*(y**2) + z**2 - 1)**3
    b = (x**2) * (z**3)
    c = (9/80) * (y**2) * (z**3)
    return a - b - c

# Preparación de datos (fuera del bucle para que sea rápido)
res = 35 # Bajamos un poco la resolución para que el giro sea fluido
bbox = (-2,2)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
A = np.linspace(xmin, xmax, res)
A1, A2 = np.meshgrid(A, A)

# Bucle de animación
# Esto hará que el corazón gire continuamente
for i in range(0, 360, 10):
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"}, figsize=(7,7))
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_axis_off()

    for z in A:
        X, Y = A1, A2
        Z = heart_3d(X, Y, z)
        ax.contour(X, Y, Z + z, [z], zdir="z", colors="#FF0000", linewidths=0.6)

    ax.view_init(elev=10, azim=i) # Aquí cambiamos el ángulo en cada paso
    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)

    # Actualizamos el gráfico en el mismo lugar
    with placeholder.container():
        st.pyplot(fig)
    
    plt.close(fig) # Cerramos la figura para no saturar la memoria
    time.sleep(0.01) # Pequeña pausa para controlar la velocidad

st.write("Eres el amor de mia vida")
