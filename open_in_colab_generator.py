import streamlit as st
import streamlit.components.v1 as components

st.title("Open in Colab Generator")

link = st.text_input('Github link: ','')
link = link.replace("https:/","") # Removing https:/
link = link.replace(".com","") # Remving .com

colab = f'<a href="https://colab.research.google.com{link}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
st.code(colab)
components.markdown(colab,unsafe_allow_html=True)
