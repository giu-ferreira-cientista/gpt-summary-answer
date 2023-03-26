import streamlit as st
from requests_html import HTMLSession
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import Image

SITE_URL = "https://dbd.puc-rio.br/TecnicasAvancadasNLP.html"
API_URL = "https://8080-giuferreira-gptsummarya-kxk348b5zkl.ws-us92.gitpod.io"
QUESTION_ROUTE = "answer" 
SUMMARY_ROUTE = "summary"

sess = HTMLSession()
        
def get_data(route, url, question):    
    api_url = f"{API_URL}/{route}?url={url}&question={question}"
    course_json = sess.get(api_url).text
    print(course_json)
    return course_json

with st.sidebar:
    add_radio = st.radio(
        "Escolha uma opção:",
        ("Responder perguntas sobre o Curso", "Resumir o conteúdo do Curso")
    )    

if add_radio == "Responder perguntas sobre o Curso":
    disabled = False
else:
    disabled = True

image = Image.open('./images/logo.jpg')
st.image(image, width=100)
st.title('Stack Academy')
st.title('Assistente de Cursos')
question = st.text_input("O que deseja saber?", "Do que se trata esse curso?", disabled=disabled)
if st.button("Run"):        
    with st.spinner('Mágica em andamento...'):
        if add_radio == "Responder perguntas sobre o Curso":
            answer = get_data(QUESTION_ROUTE, url=SITE_URL, question=question)
        else:
            answer = get_data(SUMMARY_ROUTE, url=SITE_URL, question=question)    

    st.markdown("## Resposta")
    st.markdown("---")
    text = answer
    t = st.empty()
    for i in range(len(text) + 1):
        t.markdown("## %s" % text[0:i])
        time.sleep(0.04)



