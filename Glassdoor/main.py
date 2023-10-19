import requests
from bs4 import BeautifulSoup


def get_interview_questions(company, role):
    base_url = f"https://www.glassdoor.com/Interview/data-scientist-interview-questions-SRCH_KO0,14.htm"
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        question_tags = soup.find_all("div", class_="interviewQuestion")

        questions = []
        for question_tag in question_tags:
            question = question_tag.find("span", class_="questionText").text.strip()
            questions.append(question)

        return questions
    else:
        print("Failed to retrieve interview questions.")
        return []


# Example usage
company_name = "Amazon"
role_name = "Data Science"

interview_questions = get_interview_questions(company_name, role_name)

# Save questions to a text file
with open("interview_questions.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(interview_questions))

print("Interview questions have been saved to 'interview_questions.txt'.")
