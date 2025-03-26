# 🚀 

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project aims to automate the triage of servicing requests received via email. The current manual process is slow, error-prone, and inefficient at high volumes. By leveraging AI-powered classification, intent detection, and data extraction, the system streamlines request processing, improving accuracy and response time.

## 🎥 Demo
🔗 (#) (if applicable)  
📹 (#) (if applicable)  
🖼️ Screenshots:
![image](https://github.com/user-attachments/assets/82e919cc-9114-4148-9652-7041ba6383be)
![image](https://github.com/user-attachments/assets/ec6971c9-f853-44e4-8158-f1bb8f5035a6)
![image](https://github.com/user-attachments/assets/827ae753-56ee-4d02-9edb-75aff71565a3)


## 💡 Inspiration
The inspiration for this project comes from the inefficiencies of manual email triage. Businesses often struggle with sorting, classifying, and responding to large volumes of emails, leading to delays and errors. Automating this process reduces workload and enhances productivity.

## ⚙️ What It Does
- Ingests incoming emails (including attachments) into a servicing platform.
- Identifies email intent and classifies request types and sub-types.
- Extracts key attributes for service request creation.
- Assigns requests to appropriate teams or individuals based on predefined roles and skills.
- Integrates with existing service management platforms for seamless operations.

## 🛠️ How We Built It
- **Backend**: Python with machine learning models for classification and data extraction.
- **Data Processing**: NLP techniques for email content analysis.
- **Integration**: API-based interaction with email servers and service management platforms.

## 🚧 Challenges We Faced
- Accurately classifying diverse email formats and request types.
- Extracting structured data from unstructured email content.
- Ensuring compatibility with various email clients and attachments.
- Balancing automation with human oversight for critical cases.

## 🏃 How to Run
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd project-directory
   ```

2. Install dependencies and Run:

pip install -r requirements.txt
Start the API server:

python main.py
Use the /process-email/ endpoint to classify emails.


## 🏗️ Tech Stack
- **Programming Language**: Python
- **Machine Learning**: NLP-based classification models
- **Frameworks**: Flask/FastAPI (for API integration)
- **Database**: PostgreSQL/MongoDB (for storing extracted data)
- **Cloud Services**: AWS/GCP (for deployment, if applicable)

## 👥 Team
- **Ramesh
- **Chandra
- **Shravan
- **Srikanth
- **Kavya

