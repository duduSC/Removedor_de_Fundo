import streamlit as st
import io
from PIL import Image

st.title("Removedor de Fundo de Eduardo Camargo")
st.write("Faça o upload de uma imagem e clique no botão para retirar o fundo!")

arquivo_enviado = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if arquivo_enviado is not None:
    # Lemos a imagem
    image = Image.open(arquivo_enviado)
    st.image(image, caption="Sua Imagem Original", use_container_width=True)

    if st.button("Remover Fundo da Imagem"):
        with st.spinner("Carregando a Inteligência Artificial (versão leve) e processando..."):
            try:
                # Importamos as ferramentas
                from rembg import remove, new_session
                
                # O GRANDE SEGREDO: Criamos uma "sessão" pedindo o modelo leve ('u2netp')
                sessao_leve = new_session("u2netp")
                
                # Passamos a imagem E a sessão leve para a função remove
                imagem_sem_fundo = remove(image, session=sessao_leve)
                
                # Mostramos o resultado!
                st.success("Fundo removido com sucesso!")
                st.image(imagem_sem_fundo, caption="Resultado (sem fundo)", use_container_width=True)
                
                # Botão de download
                buffer = io.BytesIO()
                imagem_sem_fundo.save(buffer, format="PNG")
                
                st.download_button(
                    label="📥 Baixar Imagem Pronta",
                    data=buffer.getvalue(),
                    file_name="imagem_sem_fundo.png",
                    mime="image/png",
                )
                
            except Exception as error:
                st.error(f"Ocorreu um erro no processamento: {error}")