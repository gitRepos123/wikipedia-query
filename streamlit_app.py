import streamlit as st
import wikipedia as wk

st.header('Wiki Search')

def publish_output(search: str) -> None:
    page = wk.page(title = search)
    if page != None:
        st.subheader(page.title)
        st.subheader('Summary')
        st.write(page.summary)
        st.subheader('Content')
        st.write(page.content)
        st.subheader('Images')
        for image in page.images:
            st.image(image)
        st.subheader('Links')
        for link in page.links:
            st.page_link(link)
        st.subheader('References')
        for reference in page.references:
            st.write(reference)

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
