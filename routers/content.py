# routers/content.py
from fastapi import APIRouter, HTTPException
from schemas.content import GenerateRequest, GenerateResponse
from services.generator import generate_and_translate
from utils.languages import SUPPORTED_CODES

router = APIRouter(prefix="/content", tags=["AI Content Automation"])

@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    if request.target_languages:
        invalid = [l for l in request.target_languages if l not in SUPPORTED_CODES]
        if invalid:
            raise HTTPException(400, f"Unsupported languages: {invalid}")

    original, translations = generate_and_translate(request.dict())
    
    return GenerateResponse(
        original=original,
        translations=translations
    )