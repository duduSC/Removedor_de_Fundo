import streamlit as st
st.title("Oi, eu estou vivo!") # <-- Nossa linha de teste

from src.interface import Interface

def main():
    interface = Interface()
    interface.tela()

if __name__ == "__main__":
    main()