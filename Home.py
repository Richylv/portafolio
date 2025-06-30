import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('img/photo.jpg')

with col2:
    st.title('Ricardo Lozano')
    content = '''
        Ingeniero de sistemas con experiencia en el diseño y la ejecución de pruebas manuales
        y automatizadas en plataformas web, móviles y API. Experto en automatización de pruebas 
        con Selenium, Pytest, SQL y pruebas de API con Postman. 
    '''
    st.info(content)

text = 'Below you can find some of the apps I have build. Feel free to contact me!'
st.write(text)

col3, empy_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv',sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('img/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('img/' + row['image'])
        st.write(f"[Source Code]({row['url']})")