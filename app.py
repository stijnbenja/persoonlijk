import streamlit as st 
import requests
from projecten import project





st.header('Stijn van Leeuwen')
st.caption('Data-Driven Web App Developer voor MKB')

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    'Voorstelronde',
    'Diensten',
    'Projecten', 
    'Werkwijze', 
    'Contact'
    ])

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
    st.write('ed')
    
    
with tab3:
    st.subheader('Projecten') 
    project(
        'Inventory Labelling Automation', 
        'https://images.unsplash.com/photo-1616401784845-180882ba9ba8?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=3600',
        'bla bla',
        'eoijf4'
        )
    
    project(
        'Bol.com product finder', 
        'https://www.aholddelhaize.com/media/gcslpvhf/rsz_1_1.jpg',
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
        
with tab4:
    st.subheader('Werkwijze')  
    st.caption('Elk project heeft zijn eigenschappen maar het process blijft dezelfde 6 stappen:')
    
    stappen = [
        ['🔍 Orientatie', 'Hier gaan wij samen kijken naar de manieren waarop ik waarde kan toevoegen aan uw onderneming. Als u al een duidelijk idee heeft voor een oplossing, dan slaan wij stap 2 over.'],
        ['💡 Ideatie', 'Na het eerste gesprek ga ik aan de slag met het inkaart brengen van mogelijke oplossingen en verbeteringen.'],
        ['📊 Offerte per idee','Nadat er een selectie gemaakt is van de beste oplossingen, is het tijd voor het kostenplaatje per idee. Hierbij kan er een selectie worden gemaakt van de features die de oplossing moet hebben. Dit zorgt ervoor dat alleen datgene geimplementeerd wordt waar daadwerkelijk behoefte aan is. Projecten worden vooraf voor een vast bedrag gefactureerd. Er komen dus geen onverwachte kosten bij na de overeenkomst.'],
        ['🛠️ Implementatie','Nadat er een akkoord is over de offerte, is het tijd voor het maken van de tool. Hierbij maak ik een planning voor de oplossing en vraag ik om de benodigde materialen van uw kant. Hoelang een project duurt hangt af van de omvang. Ik zal wekelijks de voortgang rapporteren. Hoe transparanter de voortgang hoe beter.'],
        ['📦 Overdracht','Hier wordt de tool/oplossing opgeleverd zoals afgesproken. Vervolgens gaan samen het eind resultaat doorlopen zodat alles duidelijk is.'],
        ['⛑️ Nazorg','Voor vragen kunt u altijd gratis contact opnemen. Als iets niet werkt zoals afgesproken, dan los ik dat vrijblijvend op. Heeft u nieuwe ideëen voor features, verbeteringen of nieuwe projecten? Dan hoor ik die graag en doorlopen wij een nieuw process vanaf stap 2.']
    ]
    
    
    stap1, stap2, stap3 = st.columns(3, border=True)
    stap4, stap5, stap6 = st.columns(3, border=True)
    
    for i, stap in enumerate([stap1, stap2, stap3, stap4, stap5,  stap6]):
        with stap:
            st.subheader(i+1)
            with st.popover(stappen[i][0]):
                st.subheader(stappen[i][0])
                st.write(stappen[i][1])
            
    
    st.write("")
    
    
        
             





with tab5:
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
cols1[0].link_button('✉️', 'mailto:stijnvanleeuwen3@gmail.com')
cols1[1].link_button('in', 'https://www.linkedin.com/in/stijnvleeuwen')