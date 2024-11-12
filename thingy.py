import streamlit as st
import json
import requests
import urllib.parse


st.title("Scoir data viewer thingy!")
st.write(
    "placeholder"
)

headers = {
    "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6ImthcnNhYjM0M0BnbWFpbC5jb20iLCJGaXJzdE5hbWUiOiJLYXJ0aGlrIiwiSXNTaGFkb3ciOmZhbHNlLCJMYXN0TmFtZSI6IlNhYmhhbmF5YWthbSIsIl9pZCI6IjYxMTU0Nzg2MTQ2NzBjMDAwMTY3YjM5YyIsImV4cCI6MTczMTcwMjAwOCwianRpIjoiYjFkZGFiZjktYzFhNi00YmYwLWFjMjktODQzOGZhMWY3ZTVjIn0.vLhznXErGDxckeeaI6IUe8Kow041roW4AsUVrcKKce0"
}
# with open("Applications.json", "r") as file:
#     data = json.load(file)
# school_id = st.text_input("School ID: ", "")
school_name = st.text_input("School Name: ", "", placeholder="University of California Santa Cruz")
school_id = 0
if st.button("Search for school"):
    SEARCH_URL = f'https://app.scoir.com/api/search/college/{urllib.parse.quote(school_name)}?size=50'
    response = requests.get(SEARCH_URL, headers=headers)
    # st.write(response)
    # st.write(SEARCH_URL)
    if response:
        data = response.json()
        first_school = data[0]
        school_id = first_school["scid"]
        st.header(first_school["name"])
    
major = st.text_input("Major: ", "", placeholder="Computer Science")
years = st.multiselect("Years: ",
    [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
)

if st.button("Filter"):

    URL = "https://app.scoir.com/api/highschools/5e922e7f0925986577dd7b66/prospects/assessments?scid={school_id}&fromYear=2016&toYear=2024&applicationType="
    response = requests.get(URL, headers=headers)
    if response:
        data = response.json()
        filtered_data = []
        for app in data["Applications"]:
            if major:
                if school_name in app["SchoolName"] and major in app["Major"] and app["GraduationYear"] in years:
                    filtered_data.append(app)
            else:
                if school_name in app["SchoolName"] and app["GraduationYear"] in years:
                    filtered_data.append(app)


        
        st.write("Total Applications: ", len(filtered_data))
        st.write(filtered_data)
