import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills`, and `description`.
            Only return valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def generate_required_skills(self, job_description):
        prompt_skills = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            Based on the job description above, generate a list of required skills that would be critical for this role.
            Return the result as a comma-separated string.
            ### REQUIRED SKILLS:
            """
        )
        chain_skills = prompt_skills | self.llm
        res = chain_skills.invoke({"job_description": job_description})
        return res.content.strip()

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are an applicant interested in this role. Write a cold email addressed to the HR of the company. 
            The email should explain how your experience and skillset (aligned with the job description) make you a strong fit for this position. 
            Include the most relevant portfolio links to showcase your work. 
            The email should be professional, personalized, and highlight your enthusiasm for joining the team. 
            Keep the tone polite and formal.
            ### EMAIL:
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
