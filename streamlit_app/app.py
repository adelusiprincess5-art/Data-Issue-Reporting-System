import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Data Issue Reporting System",
)


st.title("Data Issue Reporting System")


menu = st.sidebar.selectbox(
    "Menu",
    [
        "Report Issue",
        "View Issues",
        "Update Issue",
        "Delete Issue"
    ]
)



if menu == "Report Issue":

    st.header("Report a Data Issue")

    title = st.text_input("Issue Title")

    description = st.text_area("Description")

    issue_type = st.selectbox(
        "Issue Type",
        [
            "Missing Data",
            "Duplicate Data",
            "Invalid Data",
            "Incorrect Data"
        ]
    )

    severity = st.selectbox(
        "Severity",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    reported_by = st.text_input("Reported By")

    if st.button("Submit Issue"):

        data = {
            "title": title,
            "description": description,
            "issue_type": issue_type,
            "severity": severity,
            "reported_by": reported_by
        }

        response = requests.post(
            f"{API_URL}/issues/",
            json=data
        )

        if response.status_code == 200:
            st.success("Data issue reported successfully!")
        else:
            st.error("Failed to report issue.")



elif menu == "View Issues":

    st.header("All Data Issues")

    response = requests.get(
        f"{API_URL}/issues/"
    )

    if response.status_code == 200:

        issues = response.json()

        if issues:

            for issue in issues:

                st.subheader(
                    f"#{issue['id']} - {issue['title']}"
                )

                st.write(
                    f"**Description:** {issue['description']}"
                )

                st.write(
                    f"**Issue Type:** {issue['issue_type']}"
                )

                st.write(
                    f"**Severity:** {issue['severity']}"
                )

                st.write(
                    f"**Reported By:** {issue['reported_by']}"
                )

                st.write(
                    f"**Status:** {issue['status']}"
                )

                st.divider()

        else:
            st.info("No data issues found.")

    else:
        st.error("Could not connect to the backend.")



elif menu == "Update Issue":

    st.header("Update Issue Status")

    issue_id = st.number_input(
        "Issue ID",
        min_value=1,
        step=1
    )

    status = st.selectbox(
        "New Status",
        [
            "Open",
            "Investigating",
            "Resolved",
            "Closed"
        ]
    )

    if st.button("Update Status"):

        data = {
            "status": status
        }

        response = requests.put(
            f"{API_URL}/issues/{issue_id}",
            json=data
        )

        if response.status_code == 200:
            st.success("Issue status updated!")
        else:
            st.error("Issue not found.")



elif menu == "Delete Issue":

    st.header("Delete Data Issue")

    issue_id = st.number_input(
        "Issue ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Issue"):

        response = requests.delete(
            f"{API_URL}/issues/{issue_id}"
        )

        if response.status_code == 200:
            st.success("Issue deleted successfully!")
        else:
            st.error("Issue not found.")