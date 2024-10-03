# JobMender: AI-Powered Cold Email Generator

JobMender is an AI-driven tool built using Groq, LangChain, and Streamlit that helps users generate personalized cold emails to hiring managers. It extracts job listings from a company's career page and crafts tailored emails for applying based on the job description. The tool also suggests relevant portfolio links from a vector database based on required skills.

## Key Features:
- **Job Listing Extraction**: Input the URL of a company's careers page, and the tool automatically extracts job postings.
- **Skills Analysis**: Extracts and identifies the key skills required for each job.
- **Personalized Cold Email Generation**: Generates customized cold emails for each job description, targeting hiring managers.
- **Portfolio Integration**: Suggests the most relevant portfolio links from a vector database that match the job description.

## How It Works:
1. **Input the URL**: Enter the career page URL of a company.
2. **Job Listings Extraction**: The tool scrapes the page and extracts job postings, identifying the role, experience, skills, and description.
3. **Cold Email Generation**: JobMender then crafts a personalized cold email for the hiring manager, mentioning the user's skills, company profile, and portfolio links.
4. **Portfolio Suggestion**: Based on the skills mentioned in the job posting, the tool suggests the most relevant portfolio links sourced from the vector database.

## Imagine This Scenario:
Nike needs a Principal Software Engineer, and a company like Atliq offers dedicated software engineers. JobMender helps Atliq's business development executive, Mohan, send a cold email to Nike’s HR department, showcasing how Atliq can meet Nike’s software development needs. It also includes links to relevant portfolio projects to further validate Atliq's expertise.

## Architecture Diagram:
![Architecture Diagram](img.png)

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jobmender.git
