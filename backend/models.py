from pydantic import BaseModel, Field
from typing import List, Optional

class BrandRequest(BaseModel):
    business_idea: str = Field(..., min_length=3)
    industry: str = Field(..., min_length=2)
    target_audience: str = Field(..., min_length=2)
    brand_personality: str = Field(..., min_length=2)

class BrandResponse(BaseModel):
    brand_name: str
    tagline: str
    story: str
    personality: str
    colors: List[str]
    typography: str
    strategy: str
    workflow: List[str]
    logo_prompt: str
    brand_score: int

class LogoRequest(BaseModel):
    logo_prompt: str
    style_hint: Optional[str] = None

class LogoResponse(BaseModel):
    image_url: str
