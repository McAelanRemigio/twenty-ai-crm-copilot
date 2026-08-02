from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from http.cookiejar import MozillaCookieJar

load_dotenv()

app = FastAPI(title="Twenty AI Bridge")

TWENTY_URL = os.getenv("TWENTY_URL")
TWENTY_API_KEY = os.getenv("TWENTY_API_KEY")

ODYSSEUS_URL = os.getenv("ODYSSEUS_URL")
ODYSSEUS_SESSION = os.getenv("ODYSSEUS_SESSION")


class SummaryRequest(BaseModel):
    company_id: str


@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Twenty AI Bridge"
    }


@app.post("/generate-summary")
def generate_summary(request: SummaryRequest):

    # ---------------------------
    # Get company from Twenty
    # ---------------------------
    headers = {
        "Authorization": f"Bearer {TWENTY_API_KEY}"
    }

    response = requests.get(
        f"{TWENTY_URL}/rest/companies/{request.company_id}",
        headers=headers
    )

    response.raise_for_status()

    company = response.json()["data"]["company"]

    company_context = f"""
Company Name: {company.get("name")}
Website: {company.get("domainName", {}).get("primaryLinkUrl")}
Location: {company.get("address", {}).get("addressCity")}
LinkedIn: {company.get("linkedinLink", {}).get("primaryLinkUrl")}
"""

    # ---------------------------
    # Build AI Prompt
    # ---------------------------
    prompt = f"""
You are an AI CRM strategist.

Analyze this company:

{company_context}

Provide:

1. Executive Summary
2. Sales Opportunities
3. Potential Risks
4. Recommended Next Action
5. Confidence Score

Format the response using Markdown.
"""

    # ---------------------------
    # Load Odysseus cookies
    # ---------------------------
    cookiejar = MozillaCookieJar("cookies.txt")
    cookiejar.load(ignore_discard=True, ignore_expires=True)

    session = requests.Session()
    session.cookies.update(cookiejar)

    # ---------------------------
    # Ask Odysseus
    # ---------------------------
    ai_response = session.post(
        f"{ODYSSEUS_URL}/api/chat",
        json={
            "message": prompt,
            "session": ODYSSEUS_SESSION
        }
    )

    ai_response.raise_for_status()

    summary = ai_response.json()["response"]

    # ---------------------------
    # Update Twenty AI Summary
    # ---------------------------
    update_response = requests.patch(
        f"{TWENTY_URL}/rest/companies/{request.company_id}",
        headers=headers,
        json={
            "aiSummary": {
                "blocknote": None,
                "markdown": summary
            }
        }
    )

    update_response.raise_for_status()

    # ---------------------------
    # Return success
    # ---------------------------
    return {
        "success": True,
        "company": company.get("name"),
        "summary": summary
    }