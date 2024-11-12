import json
import streamlit as st

def get_results(major, school):
    with open('2024.json', 'r') as file:
        data = json.load(file)["Applications"]

        major_applicants = [a for a in data if major in a["Major"] and school in a["SchoolName"]]
        accepted_applicants = [a for a in major_applicants if a.get("Accepted", False) == True]

        st.write(f"Number of applicants who applied to that major: {len(major_applicants)}")
        st.write(f"Number of those accepted: {len(accepted_applicants)}")
        if(len(accepted_applicants) > 0):
            avg_un = sum(float(a.get("UnweightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants)
            avg_w = sum(float(a.get("WeightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants)
            st.write(f"Average GPA {avg_un}/{avg_w}")
            st.write(f"Percentage {len(accepted_applicants) / len(major_applicants)}")
        # st.write([a["CounselorName"] for a in accepted_applicants])

st.title("Sandwich Stats - Results of BISV College Applicants (2023-2024)")
st.write("Made by Michael, Derek, and Karthik")
major = st.text_input("Major", value="Computer Science")
school = st.text_input("School", value="Los Angeles")

if st.button("Get Results"):
    get_results(major, school)
