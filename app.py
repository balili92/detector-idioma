import streamlit as st  # Librería para crear interfaces web interactivas
from langdetect import detect  # Función para detectar el idioma de un texto
import pandas as pd  # Librería para manipular datos en forma de tabla
from langdetect import DetectorFactory

# Asegura resultados reproducibles
DetectorFactory.seed = 0

# Cargar archivo CSV con abreviaturas de idiomas y sus nombres
df = pd.read_csv('idiomas.csv')
idioma_dict = df.set_index('Abreviatura')['Nombre'].to_dict()

# Función que traduce la abreviatura de idioma a su nombre completo
def reconocer_idioma(abreviatura):
    nombre_idioma = idioma_dict.get(abreviatura)
    return nombre_idioma

# Configuración de la página en Streamlit
st.set_page_config('Detector de Idioma', page_icon='🌍', layout='wide')
st.title('Detector de idioma')

# Inicializar el texto en el estado de la sesión
if 'texto' not in st.session_state:
    st.session_state.texto = ''

# Función para limpiar el área de texto
def limpiar_text_area():
    st.session_state.texto = ''

# Formulario para ingresar el texto
with st.form(key='form_texto'):
    texto_usuario = st.text_area(label='Introduce aquí tu texto', key='texto')
    detectar = st.form_submit_button('Detectar idioma')

# Botón para borrar el texto manualmente
borrar_texto = st.button('Borrar texto', on_click=limpiar_text_area)

# Procesamiento del texto cuando se pulsa el botón "Detectar idioma"
if detectar:
    if st.session_state.texto.strip() == '':
        st.warning('Por favor, introduce algo de texto.')
    else:
        abreviatura = detect(st.session_state.texto)
        idioma = reconocer_idioma(abreviatura)
        if idioma is not None:
            st.success(f'El texto está escrito en el idioma: {idioma}')
        else:
            st.error('Idioma no reconocido')


