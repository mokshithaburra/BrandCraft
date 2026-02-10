from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import BrandRequest, BrandResponse, LogoRequest, LogoResponse
from services.gemini import generate_brand_content
from services.stable_diffusion import generate_logo_image
from config import ALLOWED_ORIGINS

app = FastAPI(title="BrandCraft API", version="1.0.0")

origins = ALLOWED_ORIGINS or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
@app.get("/")
def home():
    return {"message": "BrandCraft API is running"}


@app.post("/generate-brand", response_model=BrandResponse)
async def generate_brand(payload: BrandRequest):
    data = await generate_brand_content(payload.model_dump())

    # Normalize missing keys safely
    data.setdefault("personality", payload.brand_personality)
    data.setdefault("brand_score", 84)

    return BrandResponse(
        brand_name=data.get("brand_name", "BrandCraft"),
        tagline=data.get("tagline", "Craft a brand that blooms"),
        story=data.get("story", ""),
        personality=data.get("personality", ""),
        colors=data.get("colors", ["#F8C8DC", "#FFF2B2", "#111111"]),
        typography=data.get("typography", "Ballet + clean sans"),
        strategy=data.get("strategy", ""),
        workflow=data.get("workflow", ["Discovery", "Identity", "Visuals", "Launch"]),
        logo_prompt=data.get("logo_prompt", "Minimal modern floral logo"),
        brand_score=int(data.get("brand_score", 84)),
    )

@app.post("/generate-logo", response_model=LogoResponse)
async def generate_logo(payload: LogoRequest):
    image_url = await generate_logo_image(payload.model_dump())
    return LogoResponse(image_url=image_url)
