import streamlit as st
import pandas as pd
from urllib.error import URLError
import matplotlib.pyplot as plt

# Importamos los datasets que vamos a utilizar.
folder = 'data'
archivo_data = '12DB_6FP.csv'
data = pd.read_csv(folder + '/' + archivo_data, sep=',')


# Definimos las clases que vamos a utilizar y reemplazamos su valor numérico con una inicial.
nombre_clases = {0:"DB",1:"SS",2:"SW",3:"A",4:"I",5:"B"}

d = data.copy()
d['FlowPattern'] = d['FlowPattern'].replace(nombre_clases) # Reemplazamos los valores numéricos por las clases.
caracteristicas = d.drop(['FlowPattern'], axis=1) # Definimos las características que vamos a utilizar.
etiquetas = d['FlowPattern']



st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """
    Vamos a visualizar los datos que tiene la base de datos
    """
)
# Mostrar el DataFrame en Streamlit
st.dataframe(d.head())


# Como realizar el conteo de las clases que hay en la base de datos.
conteo = d["FlowPattern"].value_counts()
st.dataframe(conteo)

indices = conteo.index.tolist() # Estas son las clases

# Graficar el conteo de las clases en un gráfico de torta
fig, ax = plt.subplots()
ax.pie(list(conteo.values), labels=indices, autopct='%1.1f%%')
ax.axis('equal')  # Para asegurar que el gráfico sea circular

# Mostrar el gráfico en Streamlit
st.pyplot(fig)