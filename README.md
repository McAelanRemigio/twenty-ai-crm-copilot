# Twenty AI CRM Copilot

An AI-powered CRM copilot built on top of Twenty CRM and Odysseus.

This project automatically retrieves company information from Twenty CRM, sends it to a local LLM through Odysseus, generates an AI sales analysis, and writes the generated summary directly back into the CRM.

---

## Features

- Retrieve company records from Twenty CRM
- Generate AI-powered company summaries
- Sales opportunity analysis
- Risk identification
- Recommended next actions
- Confidence scoring
- Automatically save AI output back into the CRM

---

## Architecture

```
                Twenty CRM
                     │
                     │ REST API
                     ▼
        ┌────────────────────────┐
        │   FastAPI Bridge       │
        │  (Python Backend)      │
        └────────────────────────┘
             │              │
             │              │
             ▼              ▼
      Twenty REST API   Odysseus API
                             │
                             ▼
                     Local LLM (Ollama)
```

---

## Tech Stack

- Python
- FastAPI
- Requests
- Twenty CRM
- Odysseus
- Ollama
- Llama 3.2
- REST APIs

---

## Example Workflow

1. User selects a company inside Twenty CRM.
2. The FastAPI bridge retrieves company information.
3. Company context is sent to Odysseus.
4. The local LLM generates:

- Executive Summary
- Sales Opportunities
- Risks
- Recommended Next Action
- Confidence Score

5. The generated summary is automatically written back into the company's **AI Summary** field inside Twenty CRM.

---

## Example Output

### Company

Housecall Pro

### AI Summary

- Executive Summary
- Sales Opportunities
- Potential Risks
- Recommended Next Action
- Confidence Score

---

## Installation

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

Run the bridge.

```bash
uvicorn app:app --reload
```

---

## API

Generate a summary.

```http
POST /generate-summary
```

Example request

```json
{
    "company_id": "YOUR_COMPANY_ID"
}
```

---

## Future Improvements

- AI lead scoring
- Meeting summarization
- Contact enrichment
- Email drafting
- Prospect research
- CRM chat assistant
- Multi-model support
- Workflow automation

---

## Inspiration

This project demonstrates how open-source AI can be integrated directly into an open-source CRM to create a self-hosted AI sales copilot using local language models.

---

## License

MIT
