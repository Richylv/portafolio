import streamlit as st

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