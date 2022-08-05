from matplotlib.pyplot import ginput
import streamlit as st

st.set_page_config(page_title="About Us", page_icon="🔥")

with open("images/github.txt", "r") as f:
    github = f.read()
with open("images/linkedin.txt", "r") as f:
    linkedin = f.read()


st.title("About Us")
st.markdown("---")

_, col, _ = st.columns([1, 1, 1])
with col:
    st.image("images/yasin.jpg", caption="Yasin Tarakçı")

_, col1, col2, _ = st.columns([3, 1.5, 0.8, 3])
with col1:
    st.markdown(f"[![Foo]({github})](https://github.com/ysntrkc)")
with col2:
    st.markdown(f"[![Foo]({linkedin})](https://www.linkedin.com/in/yasintarakci)")
st.markdown("---")

_, col, _ = st.columns([1, 1, 1])
with col:
    st.image("images/uftade.jpg", caption="Üftade Bengi Erolçay")

_, col1, col2, _ = st.columns([3, 1.5, 0.8, 3])
with col1:
    st.markdown(f"[![Foo]({github})](https://github.com/uftadeerolcay)")
with col2:
    st.markdown(
        f"[![Foo]({linkedin})](https://www.linkedin.com/in/uftade-bengi-erolcay)"
    )
st.markdown("---")

_, col, _ = st.columns([1, 1, 1])
with col:
    st.image("images/baranalp.jpeg", caption="Baranalp Özkan")

_, col1, col2, _ = st.columns([3, 1.5, 0.8, 3])
with col1:
    st.markdown(f"[![Foo]({github})](https://github.com/baranalpozkan)")
with col2:
    st.markdown(f"[![Foo]({linkedin})](https://www.linkedin.com/in/baranalpozkan)")
st.markdown("---")
