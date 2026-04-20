import streamlit as st
import io  # Ferramenta do Python para lidar com arquivos na memória
from src.remove_and_save import RemoveAndSave
from PIL import Image
from rembg import remove

def process(imagem) -> Image:
        try:
            new_image = remove(imagem)
            return new_image
        except Exception as error:
            print(error)

def read(path):
         return Image.open(path)
def tela():
    # 1. Título do aplicativo
    st.title("Removedor de Fundo de Eduardo Camargo")
    st.write("Faça o upload de uma imagem e clique no botão para retirar o fundo!")

    # 2. Cria o componente para o usuário escolher o arquivo do computador
    arquivo_enviado = st.file_uploader(
        "Escolha uma imagem", type=["png", "jpg", "jpeg"]
    )

    if arquivo_enviado is not None:

        image = read(arquivo_enviado)

        # Mostra a imagem original na tela
        st.image(image, caption="Sua Imagem Original", use_container_width=True)

        # botão de ação.
        if st.button("Remover Fundo da Imagem"):

            # Mostra um ícone de carregamento enquanto o computador pensa
            with st.spinner("Carregando..."):
                try:
        
                    imagem_sem_fundo = process(image)
                    if imagem_sem_fundo:
                        st.success("Fundo removido com sucesso!")
                        st.image(
                            imagem_sem_fundo,
                            caption="Resultado (sem fundo)",
                            use_container_width=True,
                        )
                        buffer = io.BytesIO()
                        imagem_sem_fundo.save(buffer, format="PNG")
                        # --- BÔNUS: Botão para baixar a nova imagem ---
        
                        st.download_button(
                            label="📥 Baixar Imagem Pronta",
                            data=buffer.getvalue(),
                            file_name="imagem_sem_fundo.png",
                            mime="image/png",
                        )
                except Exception as error:
                    st.error(f"Erro {error}")

tela()