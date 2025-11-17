# services/translator.py  ← NEW VERSION (NO GOOGLE, NO KEYS NEEDED)
import httpx
from utils.languages import SUPPORTED_CODES

# Using public LibreTranslate instance (free, no key, supports all EU languages)
LIBRETRANSLATE_URL = "https://libretranslate.de/translate"

async def translate_text(text: str, target_languages: list[str]):
    results = {}
    async with httpx.AsyncClient(timeout=30.0) as client:
        for lang in target_languages:
            if lang not in SUPPORTED_CODES or lang == "en":
                continue
            try:
                resp = await client.post(
                    LIBRETRANSLATE_URL,
                    json={
                        "q": text,
                        "source": "en",
                        "target": lang,
                        "format": "text"
                    }
                )
                resp.raise_for_status()
                results[lang] = resp.json()["translatedText"]
            except Exception as e:
                results[lang] = f"[Translation failed: {str(e)}]"
    return results