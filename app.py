import streamlit as st 
import requests
from projecten import project

st.title('Stijn van Leeuwen')
st.caption('Data-Driven Web App Developer voor MKB')

tab1, tab2, tab3 = st.tabs(['Voorstelronde','Projecten','Stuur een verzoekje'])

with tab1:
    with st.container(border=True):
        coller = st.columns([1,2])
        
        with coller[0]:
            st.image('https://media.licdn.com/dms/image/v2/D4E03AQH5nbViTB-BWw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1703247502158?e=1742428800&v=beta&t=7-bsirj_mRwiYDdfEVQctLeyYuCechaNYPED0i7JWLM')
        
        with coller[1]:
            st.write('Hallo mijn naam is Stijn, ik maak web apps op aanvraag.')
            st.write("Ik heb 8 jaar ervaring in data-systemen en het bouwen van web applicaties voor zowel individuen als bedrijven.")
            st.write('Ik zorg ervoor dat software ideeën effectief\nworden omgezet in werkende applicaties.')
            
        skills = ["Python", "Databases",'Process Optimalisatie', "Data science", 'Dashboards', "Automatisering","APIs",'SQL']
        st.pills("Skills", skills, selection_mode="single", disabled=False)
    
with tab2:
    project(
        'Inventory Labelling Automation', 
        'https://images.unsplash.com/photo-1616401784845-180882ba9ba8?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600',
        'bla bla',
        'eoijf4'
        )
    
    project(
        'Bol.com product finder', 
        'https://file.notion.so/f/f/7fb81830-a837-4391-8eb3-ebbfd0a02dbc/861f892f-6637-445a-ac1f-949ced096043/bol.avif?table=block&id=cf5486bd-fb7e-43e4-b581-5768e36e7b12&spaceId=7fb81830-a837-4391-8eb3-ebbfd0a02dbc&expirationTimestamp=1737223200000&signature=vg3FxhkDfNx0H23rKLC7gEBs_lDfeyv2gXyKXze2P_0',
        'bla bla',
        'rjbif'
        )
    
    project(
        'Food Nutritions', 
        'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600',
        'bla bla',
        'rjbif'
        )
    
    
    project(
        'ABN Amro Insights', 
        'https://images.unsplash.com/photo-1550565118-3a14e8d0386f?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600',
        'bla bla',
        'rjbif'
        )
        
        

with tab3:
    st.subheader('Neem contact op')
    
    with st.form("my_form", clear_on_submit=False):
        hulp_vraag = st.text_area('Waar zou ik mee kunnen helpen?')
        
        col_form = st.columns(2)
        naam = col_form[0].text_input('Uw naam')
        
        email = col_form[1].text_input('Uw email adres')
        
         
        submitter = st.form_submit_button('Verstuur', disabled=False)
    
        if submitter:
            
            if len(naam)==0:
                st.error('Uw naam ontbreekt')
            elif len(email)==0:
                st.error('Uw email adres ontbreekt')
            elif len(hulp_vraag)==0:
                st.error('Uw vraag ontbreekt')
            else:
                
            
                requests.post(
                    "https://ntfy.sh/tspstijn",
                    headers={'Title':f"{naam} [{email}]"},
                    data=hulp_vraag)
                st.success(f'Bedant voor je vraag, {naam}. Ik ga ermee aan de slag!')
             



cols1 = st.columns([1,12])
cols1[0].button('✉️', )
cols1[1].button('in')