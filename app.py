import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Para la mas hermosa :3", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Te amitoo</h1>", unsafe_allow_html=True)

# Función del corazón 3D
def get_heart_coords(res=40):
    # Generamos una rejilla de puntos
    x = np.linspace(-2, 2, res)
    y = np.linspace(-2, 2, res)
    z = np.linspace(-2, 2, res)
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Ecuación del corazón
    F = (X**2 + (9/4)*(Y**2) + Z**2 - 1)**3 - (X**2)*(Z**3) - (9/80)*(Y**2)*(Z**3)
    return X, Y, Z, F

# Crear el gráfico con Plotly (mucho más fluido)
X, Y, Z, F = get_heart_coords()

# Creamos la superficie del corazón (Isosurface)
fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=F.flatten(),
    isomin=0,
    isomax=0,
    surface_count=1,
    colorscale=[[0, 'red'], [1, 'red']],
    showscale=False,
    caps=dict(x_show=False, y_show=False, z_show=False)
))

# Configuración del diseño (Fondo negro y sin ejes)
fig.update_layout(
    template="plotly_dark",
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='data'
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    # Configuración de la animación automática
    scene_camera=dict(
        eye=dict(x=1.5, y=1.5, z=0.8)
    )
)

# Mostrar en Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("<h3 style='text-align: center;'>Puedes tocarlo y girarlo jejeje </h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Eres el amor de mia vida<3</p>", unsafe_allow_html=True)
