from pickle import load
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #dbd9d9; /* Color gris claro */
    }
    </style>
    """,
    unsafe_allow_html=True
)
model = load(open("/workspaces/c23-14-data/MVP/models.sav", "rb"))

#Título
st.markdown(
    """
    <style>
    .stApp h1 {
        color: #010369; /* Cambia este valor al color que desees */
        font-weight: bold; /* Opcional: pone el título en negrita */
        text-align: center; /* Opcional: centra el título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal de la aplicación
st.title('Alta hospitalaria')

#Subtitulos
st.markdown(
    """
    <style>
    /* Cambiar estilo de los títulos (labels) */
    .stRadio label, .stSlider label, .stCheckbox label {
        color: #010369; /* Cambiar color de los títulos */
        font-size: 50px !important;  
        font-weight: bold; !important;
        text-align: left !important; /* Opcional: alineación */
    }
    </style>
    """,
    unsafe_allow_html=True
)



#Variables
st.subheader("Edad:")
st.markdown(
    """
    <style>
    /* Cambiar el color de fondo y el color del texto */
    .stRadio label {
        color: #FF5733; /* Color de los textos de las opciones */
        font-size: 18px; /* Tamaño del texto */
        font-weight: bold; /* Negrita */
    }

    /* Cambiar el color de los botones seleccionados */
    .stRadio > div > div > div > label {
        background-color: #010369; /* Color de fondo de las opciones seleccionadas */
        border-radius: 5px;
    }

    /* Cambiar el color del texto al pasar el mouse por encima */
    .stRadio > div > div > div > label:hover {
        background-color: #010369; /* Color cuando el cursor pasa por encima */
        color: white; /* Color del texto cuando se selecciona */
    }
    </style>
    """,
    unsafe_allow_html=True
)
region =  st.radio(
    "", 
    ['Región de Ñuble',
 'Región del Biobio',
 'Región Metropolitana',
 'Región de Tarapacá',
 'Región de Los Rios',
 'Región del Libertador Gral Bernardo Ohiggins',
 'Región de La Araucania',
 'Región de Valparaiso',
 'Región de Los Lagos',
 'Región de Coquimbo',
 'Región del Maule',
 'Región de Arica y Parinacota',
 'Región de Antofagasta',
 'Región de Atacama',
 'Región de Magallanes y de la Antartica Chilena',
 'Región de Aysén del Gral Carlos Ibañez del Campo'],
    index=None)

st.subheader("Nivel socioeconómico:")

nivel_socioeconomico = st.radio(
    "",
    ['Bajo-medio', 'Bajo-medio-alto', 'Medio', 'Bajo', 'Alto', 'Medio-alto', 'Bajo-alto'],
     index= None)

st.markdown(
    """
    <style>
    /* Cambiar el color de fondo y el color del texto en el slider */
    .stSlider div {
        background-color: ##d9dadb; /* Color de fondo del slider */
        color: #010369; /* Color del texto */
        font-size: 16px; /* Tamaño del texto */
    }

    /* Personalizar el color del track y el botón del slider */
    .stSlider > div > div > div {
        background-color: #fffff; /* Color del track */
        height: 8px; /* Altura del track */
    }

    .stSlider > div > div > input {
        background-color: #010369; /* Color de la barra del slider */
        width: 20px; /* Ancho del slider */
    }
    </style>
    """,
    unsafe_allow_html=True
)






st.subheader("¿Cuántas personas viven con usted?:")

personas_por_hogar = st.slider('', min_value=1, max_value=13, step=1)

st.subheader("Edad:")

edad = st.slider('', min_value=15, max_value=100, step=1)

st.subheader("Estado civil:")

estado_civil = st.radio(
    "",
    ['Casado(a)','Separado(a)','Conviviente sin acuerdo de unión civil', 'Soltero(a)', 'Viudo(a)', 'Divorciado(a)','Anulado(a)', 'Conviviente civil'],
index= None)

st.subheader("Nivel educacional:")

nivel_educacional = st.radio(
    "",
    ['Básica', 'Técnica nivel superior', 'Media científico humanista', 'Técnica comercial industrial normalista', 'Media técnica profesional', 'Profesional', 'Diferencial', 'Ninguno', 'Magister', 'Doctorado'],
     index= None)

st.subheader("Previsión:")

prevision =  st.radio(
    "",
    ['FONASA','Isapre','FF.AA. y del Orden','Ninguno (particular)','Otro sistema'],
    index = None
)

#Diccionarios
region_dic = {'Región de ñuble': 0,
 'Región del Biobio' : 1,
 'Región Metropolitana' : 2,
 'Región de Tarapacá' : 3,
 'Región de Los Rios': 4,
 'Región del Libertador Gral Bernardo Ohiggins': 5,
 'Región de La Araucania': 6,
 'Región de Valparaiso': 7,
 'Región de Los Lagos': 8,
 'Región de Coquimbo':9,
 'Región del Maule':10,
 'Región de Arica y Parinacota': 11,
 'Región de Antofagasta': 12,
 'Región de Atacama':13,
 'Región de Magallanes y de la Antartica Chilena': 14,
 'Región de Aysén del Gral Carlos Ibañez del Campo': 15}

nivel_socioeconomico_dic = {
'Bajo-medio': 0,
 'Bajo-medio-alto': 1,
 'Medio': 2,
 'Bajo': 3,
 'Alto': 4,
 'Medio-alto': 4,
 'Bajo-alto': 6}

estado_civil_dic = {'Casado(a)': 0,
 'Separado(a)': 1,
 'Conviviente sin acuerdo de unión civil': 2,
 'Soltero(a)': 3,
 'Viudo(a)': 4,
 'Divorciado(a)': 5,
 'Anulado(a)': 6,
'Conviviente civil': 7}

nivel_educacional_dic= {'Básica': 0,
'Técnica nivel superior': 1,
'Media científico humanista': 2,
'Técnica comercial industrial normalista': 3,
'Media técnica profesional': 4,
'Profesional': 5,
'Diferencial': 6,
'Ninguno': 7,
'Magister': 8,
'Doctorado': 9}

prevision_dic= {
'FONASA': 0,
 'Isapre': 1,
 'FF.AA. y del Orden': 2,
 'Ninguno (particular)': 3,
'Otro sistema': 4}

#Botón final
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #010369; /* Color de fondo del botón (Azul) */
        color: white; /* Color del texto */
        font-size: 30px; /* Tamaño de la fuente */
        font-weight: bold; /* Negrita */
        border-radius: 10px; /* Bordes redondeados */
        border: none; /* Sin borde */
        padding: 15px 25px; /* Espaciado interno */
        transition: background-color 0.3s ease; /* Efecto de transición para el color de fondo */
    }

    .stButton>button:hover {
        background-color: #010369; /* Color de fondo cuando se pasa el mouse*/
    }
    </style>
    """, 
    unsafe_allow_html=True
)

if st.button('Haz clic aquí'):
    prediccion = model.predict([
        [region_dic[region], nivel_socioeconomico_dic[nivel_socioeconomico], personas_por_hogar, edad,
         prevision_dic[prevision], estado_civil_dic[estado_civil], nivel_educacional_dic[nivel_educacional]]
    ])
    st.write('Salario estimado:', prediccion)