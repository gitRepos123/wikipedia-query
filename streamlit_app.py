import streamlit as st
import wikipedia as wk

st.header('Wiki Search')

def publish_output(search: str) -> None:
    try:
        page = wk.page(search, auto_suggest = False)
        if page != None:
            st.header(page.title)
            st.subheader('Summary')
            st.write(page.summary)
            st.subheader('Content')
            st.write(page.content)
            st.subheader('Images')
            for image in page.images:
                st.image(image)
    except:
        st.write('Content Not Found')

def init_app():
    search = None
    submitted = None
    with st.form('input-form'):
        st.write('Query Form')
        search = st.text_input(label = 'Search Query', placeholder = 'Type your Query Here...')
        submitted = st.form_submit_button('Search')
    if submitted:
        publish_output(search)

init_app()
