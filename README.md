# JobMender: AI-Powered Cold Email Generator

JobMender is an AI-driven tool built using **Groq**, **LangChain**, and **Streamlit** that assists users in crafting personalized cold emails for hiring managers. By extracting job listings from a company's career page, it automatically generates customized emails for job applications based on the job description. It also recommends relevant portfolio links from a vector database that align with the required skills.

## Key Features:
- **Job Listing Extraction**: Enter the URL of a company's careers page, and JobMender scrapes and extracts job listings automatically.
- **Skills Analysis**: Identifies and analyzes the key skills required for each extracted job.
- **Personalized Cold Email Generation**: Generates tailor-made cold emails for each job posting, addressing the hiring manager directly.
- **Portfolio Integration**: Suggests the most relevant portfolio projects from a vector database, mapped to the job description’s required skills.
- **AI-Powered Relevance Matching**: The AI engine ensures that the email content and portfolio suggestions are highly relevant to the job requirements, improving the chances of a response.

## How It Works:
1. **Input Career Page URL**: Provide the URL of a company's careers page.
2. **Job Listings Extraction**: JobMender scrapes and extracts the relevant job postings, highlighting key details such as job title, experience, skills, and the job description.
3. **Cold Email Generation**: The tool uses AI to generate a customized cold email that introduces the user, mentions relevant skills, and includes a well-structured application targeted at the hiring manager.
4. **Portfolio Suggestions**: Based on the identified skills, JobMender suggests relevant portfolio projects from a vector database, including links to showcase expertise directly in the email.

## Example Use Case:
Imagine a scenario where **Nike** is hiring a Principal Software Engineer, and **Atliq Technologies** offers a team of highly skilled software engineers. Using JobMender, **Mohan**, a business development executive at Atliq, can quickly craft and send a compelling cold email to Nike’s HR team, showcasing Atliq’s capabilities in software engineering. The email will include links to relevant portfolio projects that demonstrate Atliq's expertise, thereby increasing the likelihood of engagement.

## Architecture Diagram:
The following diagram provides an overview of the architecture of JobMender, illustrating how different components interact to generate the personalized emails:

![Architecture Diagram](imgs/architecture.png)

## Installation:
To set up and run JobMender locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/JobMender.git

2. Navigate to the project directory:
   ```bash
   cd JobMender

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
