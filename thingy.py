import json
import streamlit as st

def get_results(major, school, year):
    with open('master.json', 'r') as file:
        data = json.load(file)["Applications"]

        major_applicants = [a for a in data if major in a["Major"] and school in a["SchoolName"] and a["GraduationYear"] >= year]
        accepted_applicants = [a for a in major_applicants if a.get("Accepted", False) == True]

        st.write(f"Number of applicants who applied to that major: {len(major_applicants)}")
        st.write(f"Number of those accepted: {len(accepted_applicants)}")
        st.write(f"Percentage {len(accepted_applicants) / len(major_applicants)}")
        # st.write([a["CounselorName"] for a in accepted_applicants])

st.title("Sandwich Stats")
st.write("Made by Michael, Derek, and Karthik - BISV College Applicants (2016-2024)")
major = st.text_input("Major", value="Computer Science")
school = st.text_input("School", value="Berkeley")
year = st.text_input("Since Year", value="2024")

if st.button("Get Results"):
    get_results(major, school, year)

