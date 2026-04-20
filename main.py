import streamlit as st

st.title("🔍 Iniciando o Aplicativo...")

try:
    st.write("Passo 1: Tentando importar as ferramentas...")
    from src.interface import Interface
    
    st.write("Passo 2: Ferramentas importadas! Carregando a interface...")
    interface = Interface()
    
    st.write("Passo 3: Desenhando a tela do usuário...")
    interface.tela()
    
except Exception as erro:
    # Se algo der errado nos passos acima, a tela fica vermelha e mostra o erro!
    st.error(f"🚨 Ops, o radar detectou um erro: {erro}")