import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title = "Isa's Portfolio",
                        page_icon=':page_with_curl:',
                        initial_sidebar_state='expanded')

    st.title('Hey there!  :wave:')
    st.subheader('Welcome to my CV / Portfolio')
    welcome = '''
                > This page was created using a Streamlit application in Python. I'll be gradually adding projects I've been developing here.              
                '''
    st.markdown(welcome)
    st.markdown('---')

    # SIDEBAR
    image = Image.open('./selfie.jpg')
    st.sidebar.image(image)
    st.sidebar.write("## __Isabela Noronha__")

    st.sidebar.write("__Where to find me:__")
    st.sidebar.markdown(":briefcase: [LinkedIn](https://www.linkedin.com/in/isabela-noronha/)")
    st.sidebar.markdown(":space_invader: [Git Hub](https://github.com/noronha-isa)")
    st.sidebar.write(":e-mail: noronha13@gmail.com")

    st.sidebar.markdown('''__Main competences:__  
                        | Interdisciplinarity
                        | Adaptability
                        | Critical thinking | ''')
    
    st.sidebar.markdown('''__Main skills:__  
                        | ArcGIS
                        | Python
                        | Microsoft Office | ''')
  
# Tabs
    tab1, tab2 = st.tabs(['##### :page_with_curl: CV', '##### :globe_with_meridians: Portfolio'])
    with tab1:

        st.write('### About')
        about = '''I'm Isa, an environmental engineer currently delving into the world of data science, with a rich interdisciplinary background.  
        I am passionate about addressing socio-environmental problems, and I strongly believe that an effective approach to these issues require a
        broad range of knowledges and skills. 
        I have strong skills and experience in geoprocessing and Geografic Information Systems (GIS). 
        I am also a PhD researcher in Environment and Society at Unicamp. My journey has given me the hability comprehend the complex links between environmental problems 
        and social-political systems, and I am commited to apply this expertise to promote sustainable solutions.
        '''

        st.markdown(about)
        st.markdown('---')

        # LEARNING
        st.write('#### :books: Currently learning')

        with st.expander('Geoprocessing tools'):
            st.markdown('''
            - I'm taking the course *Geospatial Data Science* at Udemy
            - Main skills: **ArcGIS | GeoPandas | QGIS**
                        ''')
            
        with st.expander('Data science tools'):
            st.markdown('''
                - I'm taking a Data Science course at EBAC.
                - Main skills: **Python | Pandas | Numpy | Matplotlib | Seaborn | Scikitlearn | Streamlit| SQL | CRISP-DM**
                        ''')
        


        # PROFESSIONAL
        st.write('#### :coffee: Projects and Professional Experience')
        # with st.expander('*In progress*: income prediction model (short project)'):
        #     st.markdown('''  Project developed as a side assignment to the Ebac Data Scientist Course.
        #                It consists in appliying machine learning libraries to create a model that predicts the income of some
        #                 clients, using a database of socio-economic informations from a bank.                 
                    
        #                 ''')

        with st.expander('GIS Analyst at Geonoma'):
            st.markdown(''' *From December 2023 - Present (freelance)*                            
                I develop technical maps for environmental reports using data from fieldwork.          
            Activities:   
                        - Creating technical maps for environmental studies using ArcGIS and QGIS. 
                        - Analyzing raw field data. 
                        - Automating geoprocessing tools with Python/arcpy.
                    ''')
            
        with st.expander('PowerBI (short project)'):
            st.markdown('''After a short course about PowerBI, I tried do create a dashboard using open data about mining dams in Brazil.  
                        It was my first experience using this program besides the assignments of the course, but I managed to implement the ETL process, use DAX language
                        and create some visualizations about the distribution and caracteristics of mining damns.   
                        I wrote a short post about it here: [Linkedin PowerBI post](https://www.linkedin.com/feed/update/urn:li:activity:7086705995762081793/)
                        ''' )
            bi1 = Image.open('./bi1.jpg')
            bi2 = Image.open('./bi2.jpg')
            colbi1, colbi2 = st.columns(2)
            with colbi1:
                st.image(bi1)
            with colbi2:
                st.image(bi2)
                
        with st.expander('Learning Tutor at Univesp'):
            st.markdown(''' *From September 2022 - Present*                            
                I provide support and supervise some grad students and it's academic projects at 
                Univesp (Virtual Univesity of São Paulo).          
            Activities:   
                        - Preparation of content and holding review classes, group orientation meetings for project development.   
                        - Project management and guidance.   
                        - Preparation of monthly reports on activities carried out and project progress.
                    ''')
            
        with st.expander('Agroforestry Consultant at Instituto Maracá'):
            st.markdown(''' *From September 2021 - February 2022*   
                        Work developed with an indigenous community.   
                        Activities:   
                    - Field visits to diagnose and survey community demands.   
                    - Preparation of a project to restore the community’s seedling nursery.   
                    - Coordination of the project developed together with the community.   
                    - Analysis of soil environmental quality to support future projects.
                        ''')
        
        with st.expander('Teaching Assistant at Unicamp'):
            st.markdown(''' *During 3 diferent semesters, between 2017-2021*                       
                Teaching Internship Program carried out during postgraduate studies in three disciplines: 
                'Social Studies of Science and Technology', 'Nature and Technology' and 'Society and Environment'               
            Activities:   
            - Conducting review classes and complementary topics.   
            - Application and correction of assignments.   
                        ''')
            
        with st.expander('Internship at Odebrecht'):
            st.markdown(''' *From January - March 2013*     
                Internship at the Environmental Management Sector of the Santo Antonio hidroelectric power plant
                in Porto Velho, Rondonia.   
                        Activities:   
                - Verification of environmental quality standards in the field.   
                - Compilation and processing of results.   
                - Preparation of diagnostic reports for the areas. 
                            ''')
        
        # ACADEMY
        st.write('#### :mortar_board: Academic Background')
        with st.expander('PhD in Environment and Society'):
            st.markdown('''*2018 - Present*                        
        In my doctoral program at Unicamp, I am conducting research on the production, management, and impacts 
        of mining waste.                  
        Activities:    
        - Planning, writing and executing a research project.   
        - Collection of quantitative and qualitative data in the field, carrying out interviews,   
        observations and documentary research.   
        - Preparation of articles, projects and reports based on the interpretation and discussion of the data collected.   
        - Analysis and systematization of results.   
        - Participation in seminars and other events for oral presentation of the research and discussion of results. ''')
        
        with st.expander('Master Degree in Interdisciplinarity and Social Sciences'):
            st.markdown('''*From March 2016 - February 2018*  
                                        
    During this period, I developed a research around women farmers, gender issues and agroecology.  
        I wrote an article about my dissertation, and it can be found here:   
        https://periodicos.ufpb.br/ojs2/index.php/artemis/article/view/53701''')
            
        
        st.write('#### :airplane: International Experience')
        with st.expander('Denmark, 2022'):
            st.markdown('''I lived 7 months in Aarhus, Denmark, as a visiting PhD reasearcher at the Aarhus University.  
                        There I presented my research, received rich comments and inputs, and lived in a strongly diversified environment. 
                        I also taught a seminar on environmental justice in Latin America, and managed to improve my communication skills in english.''')
            aarhus = Image.open('./aarhus.jpg')
            copenhague = Image.open('./copenhague.png')
            col1, col2 = st.columns(2)
            with col1:
                st.image(aarhus, caption='Aarhus University')
            with col2:
                st.image(copenhague, width=255, caption='Cold and rain in Copenhagen')
        
        with st.expander('Germany, 2020'):
            st.markdown('''I stayed in Berlin between February and June.   
                        Unfortunately, the pandemic hindered me to learn some german, but I still want to resume my classes. ''')
            dresden = Image.open('./dresden.jpg')
            st.image(dresden, caption="Old grey buildings")
            
        
        with st.expander('Colombia, 2012'):
            colombia = ('''Between December 2011-January 2012 I lived in Santa Marta, Colombia.   
                                I worked as a volunteer at an NGO called *Santa Marta Sin Limites*, where we created and implemented environmental education projects involving
                                children and adults from dispriviledged neighborhoods.
                        Additionally, I learned to understand spanish y hablar portuñol.''')
            st.markdown(colombia)


        with st.expander('#### :loop: Random ~ bookbinding and other interests'):
            st.write("I've always loved literature and handcrafts! As a side effect, I'm also interested in bookbinding techniques and books history :)")
            st.write("Between 2019 and 2022 I've maintained an bookbinding atelier called 'Sibila Atelie'. I produced and sold many handcrafted and personalized notebooks.")
            col5, col6 = st.columns(2)
            caderno1 = Image.open('./caderno0.jpg')
            caderno2 = Image.open('./caderno11.jpg')
            with col5:
                st.image(caderno1, width=280)

            with col6:
                st.image(caderno2, width=400)


 ####  Portfolio / MAPS 
    with tab2:
        st.write("#### Here are some maps I've made :) ")

       # st.write("Maps I've created using QGIS or ArcGIS for practice purposes.")
    # tab1, tab2, tab3, tab4 = st.tabs(["Map 1", "Map 2", "Map 3", "Map 4"])
        mapa1 = Image.open('./mapa1.jpg')
        mapa2 = Image.open('./mapa2.jpg')
        mapa3 = Image.open('./mapa3.jpg')
        mapa4 = Image.open('./mapa4.jpg')
        mapa5 = Image.open('./mapa5.jpeg')
        mapa6 = Image.open('./mapa6.jpg')
        mapa7 = Image.open('./mapa7.jpeg')
        mapa8 = Image.open('./mapa8.jpg')
        mapa9 = Image.open('./mapa9.jpeg')
        
        st.markdown("1. Location maps: ")
        #container = st.container(border=True)
        #container.write("Two hipsometric maps")
        st.image(mapa1)
        st.image(mapa2)
        st.image(mapa3)
        st.image(mapa4)
        st.image(mapa5)
        st.image(mapa6)
        st.image(mapa7)
        
        st.markdown('---')

        st.markdown("2. Other maps: ")
        #container2 = st.container(border=True)
        #container2.write("Two location maps")
        st.image(mapa8)
        st.image(mapa9)
     

if __name__=='__main__':
    main()