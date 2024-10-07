import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import pandas as pd


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Email Generator for HR")

    # Initialize session state variables
    if 'job_roles' not in st.session_state:
        st.session_state['job_roles'] = []
    if 'selected_role' not in st.session_state:
        st.session_state['selected_role'] = None
    if 'email_generated' not in st.session_state:
        st.session_state['email_generated'] = False

    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit URL")

    if submit_button:
        try:
            # Load and clean the webpage content
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Extract job postings
            jobs = llm.extract_jobs(data)

            if not jobs:
                st.warning("No job postings were found on the webpage.")
                return

            # Save extracted job details to a CSV file
            job_data = []
            for job in jobs:
                job_data.append({
                    "Job Title": job.get('role', 'Unknown Role'),
                    "Responsibilities": job.get('description', 'No Description Available'),
                    "Skills Required": llm.generate_required_skills(job.get('description', ''))
                })
            job_df = pd.DataFrame(job_data)
            job_df.to_csv('job_details.csv', index=False)
            st.success("Job details have been saved to job_details.csv")

            # Store job roles in session state to avoid resetting on rerun
            st.session_state['job_roles'] = [job.get('role', 'Unknown Role') for job in jobs]
            st.session_state['jobs'] = jobs
            st.session_state['email_generated'] = False  # Reset email generated state

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

    # If job roles have been extracted, allow user to select a role
    if st.session_state['job_roles']:
        st.subheader("Available Job Roles:")
        selected_role = st.selectbox("Select a job role to generate an email for:", st.session_state['job_roles'])

        # Update session state with the selected role
        st.session_state['selected_role'] = selected_role

        # Button to generate the email
        generate_email_button = st.button("Generate Email")

        if generate_email_button:
            # Check if the user has selected a job role
            if st.session_state['selected_role']:
                try:
                    # Find the selected job from the list of jobs
                    selected_job = next(job for job in st.session_state['jobs'] if job.get(
                        'role') == st.session_state['selected_role'])

                    # Generate skills and portfolio links for the selected job
                    skills = llm.generate_required_skills(selected_job.get('description', ''))
                    portfolio.load_portfolio()
                    links = portfolio.query_links(skills)

                    # Generate cold email for the selected job
                    email = llm.write_mail(selected_job, links)
                    st.session_state['email_generated'] = True
                    st.session_state['email'] = email

                except Exception as e:
                    st.error(f"An Error Occurred: {e}")
            else:
                st.warning("Please select a job role before generating the email.")

    # Display the generated email only if it has been generated
    if st.session_state.get('email_generated', False):
        st.subheader("Generated Cold Email:")
        st.code(st.session_state['email'], language='markdown')


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator for HR", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
