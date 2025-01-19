import streamlit as st 

def project(title, image_url, description ,explanation):
    with st.container(border=True):
        
        cols_a = st.columns([1,2])
        
        with cols_a[0]:
            st.image(image_url)
        
        with cols_a[1]:
            st.write(title)
            st.caption(description)
            
            with st.popover('Hoe het werkt', help=None, icon=None, disabled=False, use_container_width=False):
                st.write(explanation)
    