import json
import streamlit as st

def get_results(major, school, year):
    with open('Full.json', 'r') as file:
        data = json.load(file)[0]["Applications"]
    
    if year <= 2020:
        st.warning("We can't search by major prior to 2021 - it's not available to us.")
        major_applicants = [a for a in data if school.lower() in a["SchoolName"].lower() and year == a["GraduationYear"]]
        accepted_applicants = [a for a in major_applicants if a.get("Accepted", False) == True]
        st.write(f"Number of applicants who applied to that school: {len(major_applicants)}")
    else: 
        major_applicants = [a for a in data if major.lower() in a["Major"].lower() and school.lower() in a["SchoolName"].lower() and a["GraduationYear"] == year]
        accepted_applicants = [a for a in major_applicants if a.get("Accepted", False) == True]
        st.write(f"Number of applicants who applied to that major: {len(major_applicants)}")
    
    st.write(f"Number of those accepted: {len(accepted_applicants)}")
    if(len(accepted_applicants) > 0):
        avg_un = round(sum(float(a.get("UnweightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants), 2)
        avg_w = round(sum(float(a.get("WeightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants), 2)
        st.write(f"Average GPA {avg_un}/{avg_w}")
        st.write(f"Percentage {round(len(accepted_applicants) / len(major_applicants), 2)}")

st.title("Sandwich Stats")
st.write("Made by Michael, Derek, and Karthik '25 - A bad tool to view results of BISV college applicants (2016-2024)")
st.image("maps.png", caption="The colleges we go to", width=700)
major = st.text_input("Major", value="Computer Science")
school = st.text_input("School", value="Berkeley")
year = st.number_input("Year", min_value=2016, max_value=2024, value=2024)
if st.button("Get Results"):
    get_results(major, school, year)
