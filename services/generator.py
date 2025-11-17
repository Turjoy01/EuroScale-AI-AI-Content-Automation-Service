# services/generator.py   ← FINAL VERSION (copy-paste this whole file)
from openai import OpenAI
from config import settings
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Change only this line for quality vs cost
MODEL = "gpt-4o"          # ← cheap & fast
# MODEL = "gpt-4o"             # ← uncomment for 100 % perfection (costs ~3× more)

# All 25+ European languages you need
EU_LANGUAGES = {
    "en", "de", "fr", "es", "it", "nl", "pt", "pl", "sv", "da", "no", "fi",
    "cs", "hu", "ro", "el", "bg", "sk", "sl", "lt", "lv", "et", "mt", "hr",
    "ru", "uk"
}

# Content-type specific instructions (add more anytime)
CONTENT_INSTRUCTIONS = {
    "sales_script":
        "Write a short, friendly cold-outreach sales email with Subject line, greeting [Name], 3-5 sentences, clear soft CTA (15-minute call or quick reply), and sign-off.",

    "promotional_content":
        "Write punchy, high-converting promotional copy (social media post, ad, landing page hero). Max 120 words. Very energetic and benefit-focused.",

    "product_description":
        "Write a compelling, SEO-friendly product description for an e-commerce or SaaS page. 150-250 words. Highlight benefits, use natural keywords.",

    "client_summary":
        "Write a concise internal executive summary about the client. Bullet-point format, neutral and professional tone. Include key facts and opportunities."
}

def generate_and_translate(request: dict):
    content_type = request.get("type", "sales_script")
    target_langs = [lang for lang in request.get("target_languages", []) if lang in EU_LANGUAGES]

    instruction = CONTENT_INSTRUCTIONS.get(content_type, CONTENT_INSTRUCTIONS["sales_script"])

    # Build translation list for the prompt
    translation_block = ""
    if target_langs:
        translation_block = "\n\nThen translate the exact same text into these languages (keep formatting, tone, and length identical):\n"
        for code in target_langs:
            translation_block += f"- {code.upper()}: full text in {code}\n"

    user_prompt = f"""
You are an expert B2B copywriter and translator.

Task: {instruction}

Product / Topic: {request.get('product_name') or 'our solution'}
Key features / points to mention naturally: {', '.join(request.get('product_features', []))}
Company: {request.get('company_name') or 'our company'}
Tone: {request.get('tone', 'professional')}
Target audience: {request.get('target_audience', 'decision makers')}

{translation_block}

Return ONLY valid JSON in this exact structure (use \\n\\n for line breaks):
{{
  "original": "Full English text here",
  "translations": {{
    "de": "Full German text...",
    "fr": "Full French text...",
    ... only the languages listed above
  }}
}}
Never skip any requested language.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": user_prompt}],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=4000
    )

    result = json.loads(response.choices[0].message.content.strip())

    original = result.get("original", "")
    translations = result.get("translations", {})

    # Final safety filter – only return requested languages
    translations = {k: v for k, v in translations.items() if k in target_langs}

    return original, translations