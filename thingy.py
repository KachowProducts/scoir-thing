import json
import urllib.request
import streamlit as st

headers = {
    "Authorization": f"Bearer {st.secrets["TOKEN"]}"
}


def get_results(major, school, year):
    with open('blah.json', 'r') as file:
        data = json.load(file)["Schools"]
        data = [{x["Name"]: x["Scid"]} for x in data]

    id = None
    for x in data:
        for key in x:
            # print(key)
            if school.lower() in key.lower():
                id = x[key]
                # print(id)
                break
    URL = f"https://app.scoir.com/api/highschools/5e922e7f0925986577dd7b66/prospects/assessments?scid={id}&fromYear=2016&toYear=2024"
    # print(URL)
    req = urllib.request.Request(URL, headers=headers)
    with urllib.request.urlopen(req) as response:
        data2 = json.loads(response.read())["Applications"]
        
        if year <= 2019:
            major_applicants = [a for a in data2 if major in a["Major"] and a["GraduationYear"] == year]
            accepted_applicants = [a for a in major_applicants if a.get("ResultCode") == "Accepted"]
        else:
            major_applicants = [a for a in data2 if major in a["Major"] and a["GraduationYear"] == year]
            accepted_applicants = [a for a in major_applicants if a.get("Accepted", False) == True]
        
        st.write(f"Number of applicants who applied to that major: {len(major_applicants)}")
        st.write(f"Number of those accepted: {len(accepted_applicants)}")
        if(len(accepted_applicants) > 0):
            avg_un = sum(float(a.get("UnweightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants)
            avg_w = sum(float(a.get("WeightedGPA", 0)) for a in accepted_applicants) / len(accepted_applicants)
            st.write(f"Average GPA {avg_un}/{avg_w}")
            st.write(f"Percentage {len(accepted_applicants) / len(major_applicants)}")


st.title("Sandwich Stats")
st.write("Made by Michael, Derek, and Karthik - BISV College Applicants (2016-2024)")
major = st.text_input("Major", value="Computer Science")
school = st.text_input("School", value="Berkeley")
year = st.number_input("Year", value=2024)
if st.button("Get Results"):
    get_results(major, school, year)
