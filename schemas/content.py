from pydantic import BaseModel
from typing import Literal, Optional, List

class GenerateRequest(BaseModel):
    type: Literal["sales_script", "promotional_content", "product_description", "client_summary"]
    
    # Common fields
    product_name: Optional[str] = None
    product_features: Optional[List[str]] = None
    company_name: Optional[str] = None
    client_name: Optional[str] = None
    tone: Optional[str] = "professional"          # friendly, luxury, urgent, etc.
    target_audience: Optional[str] = None
    length: Optional[str] = "medium"              # short, medium, long
    
    source_language: str = "en"
    target_languages: Optional[List[str]] = None   # e.g. ["de", "fr", "es"]

class GenerateResponse(BaseModel):
    original: str
    translations: dict[str, str] = {}