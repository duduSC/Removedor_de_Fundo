import streamlit as st
from PIL import Image

# 1. Título de teste
st.title("🚀 Teste de Sanidade do Servidor")
st.write("Se você está vendo esta tela, significa que o Streamlit está a funcionar perfeitamente na nuvem!")

# 2. Teste de Upload
arquivo_enviado = st.file_uploader("Faça o upload de uma imagem de teste", type=["png", "jpg", "jpeg"])

if arquivo_enviado is not None:
    # Lê e mostra a imagem
    imagem = Image.open(arquivo_enviado)
    st.image(imagem, caption="Upload feito com sucesso!", use_container_width=True)
    st.success("Tudo certo com a interface e o processamento de imagens base!")
