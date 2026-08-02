# 🤖 Twenty AI CRM Copilot

An AI-powered CRM copilot that automatically generates strategic company insights inside Twenty CRM using a local large language model.

Built with **FastAPI**, **Twenty CRM**, **Odysseus**, and **Ollama**.

---

## 📌 Overview

Twenty AI CRM Copilot extends Twenty CRM by generating AI-powered company intelligence directly within CRM records.

Instead of manually researching companies, users can trigger an automated workflow that:

1. Retrieves company information from Twenty CRM
2. Sends the data to a local AI model through Odysseus
3. Generates strategic business insights
4. Writes the results directly back into the company's **AI Summary** field

Everything runs locally, allowing organizations to keep sensitive CRM data under their own control.

---

## ✨ Features

- 🤖 AI-generated executive summaries
- 💼 Sales opportunity identification
- ⚠️ Potential risk analysis
- ✅ Recommended next actions
- 📊 Confidence scoring
- 🔄 Automatic updates to Twenty CRM
- 🔒 Local-first architecture using Ollama
- ⚡ FastAPI integration layer
- 🧠 Llama 3.2 powered analysis

---

# Architecture

```
                    +----------------------+
                    |     Twenty CRM       |
                    +----------+-----------+
                               |
                      REST API |
                               |
                               ▼
                   +-----------------------+
                   |    FastAPI Bridge     |
                   +-----------+-----------+
                               |
                 Company Data  |
                               ▼
                    +----------------------+
                    |      Odysseus        |
                    +-----------+----------+
                                |
                          Prompt |
                                ▼
                     +----------------------+
                     |   Ollama (Llama3.2)  |
                     +-----------+----------+
                                 |
                       AI Response|
                                 ▼
                    +-----------------------+
                    | Update AI Summary     |
                    +-----------+-----------+
                                |
                                ▼
                        Twenty CRM Record
```

---

# Example Workflow

```
Company selected

↓

Retrieve company information

↓

Generate AI prompt

↓

Send prompt to Odysseus

↓

Llama 3.2 analyzes company

↓

Receive AI-generated report

↓

Update AI Summary inside Twenty CRM
```

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | API Bridge |
| Twenty CRM | CRM Platform |
| Odysseus | AI Orchestration |
| Ollama | Local LLM Runtime |
| Llama 3.2 | Language Model |
| REST API | CRM Integration |

---

# Project Structure

```
twenty-ai-crm-copilot
│
├── bridge
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
│
├── screenshots
│
├── README.md
│
└── .gitignore
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/McAelanRemigio/twenty-ai-crm-copilot.git
```

Install dependencies.

```bash
pip install -r bridge/requirements.txt
```

Create a `.env` file.

```env
TWENTY_URL=http://localhost:2020
TWENTY_API_KEY=YOUR_API_KEY

ODYSSEUS_URL=http://127.0.0.1:7000
ODYSSEUS_SESSION=YOUR_SESSION_ID
```

Run the API.

```bash
uvicorn app:app --reload
```

---

# API Endpoint

Generate an AI summary for a company.

```
POST /generate-summary
```

Example request

```json
{
  "company_id": "YOUR_COMPANY_ID"
}
```

---

# Example Output

The AI automatically generates insights including:

- Executive Summary
- Sales Opportunities
- Potential Risks
- Recommended Next Action
- Confidence Score

The response is automatically written back into the company's **AI Summary** field inside Twenty CRM.

---

# Roadmap

- [x] Connect to Twenty CRM REST API
- [x] Generate AI summaries
- [x] Automatically update CRM records
- [ ] One-click "Generate Summary" button inside Twenty
- [ ] Company enrichment from external sources
- [ ] AI-generated outreach emails
- [ ] Lead scoring
- [ ] Multi-model support

---

# Why I Built This

Traditional CRMs store data but often require users to manually interpret it before taking action.

This project explores how local AI models can augment CRM workflows by transforming company data into actionable insights while keeping sensitive business information under the user's control.

---

# License

MIT License
