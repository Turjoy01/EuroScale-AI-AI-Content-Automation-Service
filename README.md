# EuroScale AI – AI Content Automation Service

**One API → 4 Content Types → 25+ European Languages in a single call**  
Built for multi-vendor / multi-company B2B SaaS platforms targeting the entire European market.

### Features (100% Complete & Production-Ready – November 2025)

- Generate 4 content types instantly:
  - `sales_script` → Cold outreach emails with subject + CTA
  - `promotional_content` → Ads, LinkedIn, social posts
  - `product_description` → E-commerce / SaaS landing pages
  - `client_summary` → Internal executive briefs (bullet points)
- Translate into **25+ European languages** in the same API call
- Any tone: friendly, luxury, urgent, technical, playful…
- Powered **only** by OpenAI (gpt-4o-mini or gpt-4o) → no Google, no DeepL
- Returns perfect JSON → ready for CRM, email tools, frontend
- FastAPI + Swagger → test in 5 seconds

### Quick Start

```bash
git clone https://github.com/yourname/euroscale-ai-content.git
cd euroscale-ai-content
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open → http://127.0.0.1:8000/docs

### 4 Real-Life Test Examples (Copy-Paste into Swagger)

#### 1. Sales Script (German + French + Polish)
```json
{
  "type": "sales_script",
  "product_name": "CloudERP Pro",
  "product_features": ["KI-Automatisierung", "100% DSGVO-konform", "Echtzeit-Reporting"],
  "company_name": "EuroTech Solutions",
  "tone": "friendly",
  "target_audience": "CFOs in Germany, France & Poland",
  "target_languages": ["de", "fr", "pl"]
}
```

#### 2. Promotional Content (Swedish + Italian + Spanish)
```json
{
  "type": "promotional_content",
  "product_name": "SolarFlow Home",
  "product_features": ["Noll förskottskostnad", "30% lägre elräkning", "10-års garanti"],
  "company_name": "GreenFuture Energy",
  "tone": "exciting",
  "target_audience": "Homeowners in Scandinavia & Southern Europe",
  "target_languages": ["sv", "it", "es"]
}
```

#### 3. Product Description (Dutch + Portuguese + Czech)
```json
{
  "type": "product_description",
  "product_name": "StyleAI Pro",
  "product_features": ["AI-trendvoorspelling", "Automatische voorraadoptimalisatie", "3D virtuele samples"],
  "company_name": "FashionTech Studio",
  "tone": "luxury",
  "target_audience": "Fashion brands in Benelux & Southern Europe",
  "target_languages": ["nl", "pt", "cs"]
}
```

#### 4. Client Summary (Danish + Hungarian + Greek)
```json
{
  "type": "client_summary",
  "client_name": "Nordic Logistics A/S",
  "product_features": ["450 employees", "Multi-warehouse SaaS needed", "Strong ESG & GDPR focus", "Budget €180k/year"],
  "company_name": "EuroTech Solutions",
  "tone": "neutral",
  "target_audience": "Internal sales team",
  "target_languages": ["da", "hu", "el"]
}
```

### Tech Stack
- FastAPI 0.115 + Uvicorn
- OpenAI gpt-4o-mini / gpt-4o
- Pydantic v2
- Python 3.11+

### Upcoming Modules (already designed)
- AI Customer Chat Assistant (multilingual widget)
- AI Proposal → PDF Generator
- Predictive Lead Scoring
- Multi-Tenant System (company isolation)

Made with Turjoy in Bangladesh for the entire European market

![AI Content Generation Automation](images/ai_content_generation_automation.png)
